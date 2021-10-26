from adminpart import forms
from django.contrib.auth import authenticate, login,logout
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from adminpart.models import *
from django.contrib.auth.hashers import *
from . import forms
import requests
# Create your views here.

def index(request):
    us=request.session.get("user")
    if request.method == "POST":
        uname = request.POST['username']
        pas = request.POST['password']

        print(f"Username:{uname}")
        print(f"Password:{pas}")
        us=AllocateHouseDetail.objects.filter(username=uname,password=pas)
        print(us)
        if us:
            # login(request, us)
            request.session['user'] = uname
            print("Login Successfully!")
            a = AllocateHouseDetail.objects.get(username = uname)
            # return redirect('/')
            return render(request,'default/index.html',{'sname':SocietyDetail.objects.all(),'title':'home','us':us,'user':a})
        else:
            return redirect('/')
    if us:
        a = AllocateHouseDetail.objects.get(username = us)
        return render(request,'default/index.html',{'sname':SocietyDetail.objects.all(),'title':'home','us':us,'user':a})
    else:
        return render(request,'default/index.html',{'sname':SocietyDetail.objects.all(),'title':'home','us':us})

def user_logout(request):
    logout(request)
    return redirect('/')

def societylist(request,pk):
    us=request.session.get("user")
    print(us)
    if request.method == "POST":
        uname = request.POST['username']
        pas = request.POST['password']

        print(f"Username:{uname}")
        print(f"Password:{pas}")
        us=AllocateHouseDetail.objects.filter(username=uname,password=pas)
        print(us)
        if us:
            # login(request, us)
            request.session['user'] = uname
            print("Login Successfully!")
            a = AllocateHouseDetail.objects.get(username = uname)
            # return redirect('/')
            # return render(request,'default/index.html',{'sname':SocietyDetail.objects.all(),'title':'home','us':us,'user':a})
            return render(request,'default/societylist.html',{'sname':SocietyDetail.objects.all(),'id':pk,'data':HouseDetail.objects.all(),'title':'Society list','us':us,'user':a})
        # else:
        #     return redirect('/')
    
    if us:
        a = AllocateHouseDetail.objects.get(username = us)
        return render(request,'default/societylist.html',{'sname':SocietyDetail.objects.all(),'id':pk,'data':HouseDetail.objects.all(),'title':'Society list','us':us,'user':a})
    else:
        return render(request,'default/societylist.html',{'sname':SocietyDetail.objects.all(),'id':pk,'data':HouseDetail.objects.all(),'title':'Society list','us':us})

def my_account(request):
    us = request.session.get('user')
    a = AllocateHouseDetail.objects.get(username = us)
    dct = {'title':'My Account','us':us,'user':a,'sname':SocietyDetail.objects.all()}
    return render(request,'default/my_account.html',dct)

def my_home(request):
    us = request.session.get('user')
    a = AllocateHouseDetail.objects.get(username = us)
    b = HouseDetail.objects.get(blockno = a.blockno ,sname = a.sname)
    dct = {'title':'My Home','us':us,'user':a,'home':b,'sname':SocietyDetail.objects.all()}
    return render(request,'default/my_home.html',dct)

def rent(request):
    us = request.session.get('user')
    a = AllocateHouseDetail.objects.get(username = us)
    b = HouseDetail.objects.get(blockno = a.blockno ,sname = a.sname)
    if request.method == 'POST':

        c = Rent_List.objects.all()
        for i in c:
            if i.username == us:
                i.rent_price = request.POST['rent_price']
                i.save()

                dct = {'title':'My Home','us':us,'user':a,'home':b,'sname':SocietyDetail.objects.all()}
                return render(request,'default/my_home.html',dct)

        obj = Rent_List()
        obj.sname = a.sname
        obj.house_no = a.blockno
        obj.type = b.type
        obj.username = a.username
        obj.rent_price = request.POST['rent_price']
        obj.save()
            
        dct = {'title':'My Home','us':us,'user':a,'home':b,'sname':SocietyDetail.objects.all()}
        return render(request,'default/my_home.html',dct)

def sell(request):
    us = request.session.get('user')
    a = AllocateHouseDetail.objects.get(username = us)
    b = HouseDetail.objects.get(blockno = a.blockno ,sname = a.sname)
    if request.method == 'POST':
        c = Sell_List.objects.all()
        for i in c:
            if i.username == us:
                i.sell_price = request.POST['sell_price']
                i.save()

                dct = {'title':'My Home','us':us,'user':a,'home':b,'sname':SocietyDetail.objects.all()}
                return render(request,'default/my_home.html',dct)
            
        obj = Sell_List()
        obj.sname = a.sname
        obj.house_no = a.blockno
        obj.type = b.type
        obj.username = a.username
        obj.sell_price = request.POST['sell_price']
        obj.save()
        
        dct = {'title':'My Home','us':us,'user':a,'home':b,'sname':SocietyDetail.objects.all()}
        return render(request,'default/my_home.html',dct)

def complain(request):
    us = request.session.get('user')
    a = AllocateHouseDetail.objects.get(username = us)
    if request.method == 'POST':
        form = forms.ComplainForm(request.POST)
        if form.is_valid():
           obj = Complain()
           obj.username =  a.username
           obj.mobile = a.mobile_no
           obj.subject = form.cleaned_data['subject']
           obj.content = form.cleaned_data['content']
           obj.save()
           
    dct = {'title':'Complain','us':us,'user':a,'sname':SocietyDetail.objects.all()}
    return render(request,'default/complain.html',dct)

def selllist(request):
    us = request.session.get('user')
    a = AllocateHouseDetail.objects.get(username = us)
    dct = {'title':'Sell list','us':us,'user':a,'data':Sell_List.objects.all(),'sname':SocietyDetail.objects.all()}
    return render(request,'default/selllist.html',dct)

def sell_h_view(request,pk):
    us = request.session.get('user')
    a = AllocateHouseDetail.objects.get(username = us)
    b = Sell_List.objects.get(id = pk)
    c = HouseDetail.objects.get(sname = b.sname , blockno = b.house_no)
    x = AllocateHouseDetail.objects.get(sname = b.sname , blockno = b.house_no)
    dct = {'title':'Sell house','us':us,'user':a,'data':b,'house':c,'obj':x,'sname':SocietyDetail.objects.all()}
    return render(request,'default/sell_house_view.html',dct)

def rentlist(request):
    us = request.session.get('user')
    a = AllocateHouseDetail.objects.get(username = us)
    dct = {'title':'Rent list','us':us,'user':a,'data':Rent_List.objects.all(),'sname':SocietyDetail.objects.all()}
    return render(request,'default/rentlist.html',dct)

def rent_h_view(request,pk):
    us = request.session.get('user')
    a = AllocateHouseDetail.objects.get(username = us)
    b = Rent_List.objects.get(id = pk)
    c = HouseDetail.objects.get(sname = b.sname , blockno = b.house_no)
    x = AllocateHouseDetail.objects.get(sname = b.sname , blockno = b.house_no)
    dct = {'title':'Rent house','us':us,'user':a,'data':b,'house':c,'obj':x,'sname':SocietyDetail.objects.all()}
    return render(request,'default/rent_house_view.html',dct)

def my_msg(request):
    us = request.session.get('user')
    a = AllocateHouseDetail.objects.get(username = us)
    dct = {'title':'My Message','us':us,'user':a,'data':Message.objects.all(),'sname':SocietyDetail.objects.all()}
    return render(request,'default/my_message.html',dct)

def message(request,pk):
    us = request.session.get('user')
    a = AllocateHouseDetail.objects.get(username = us)
    # b = AllocateHouseDetail.objects.get(id = pk)
    if request.method == "POST":
        form = forms.MessageForm(request.POST)
        if form.is_valid():
            obj = Message()
            obj.sender_name = a.username
            obj.receiver_name = pk
            obj.subject = form.cleaned_data['subject']
            obj.message = form.cleaned_data['message']
            obj.save()
            return redirect('index')

    dct = {'title':'Message','us':us,'user':a,'sname':SocietyDetail.objects.all()}
    return render(request,'default/message.html',dct)

def delete(request,pk):
    b = Message.objects.get(id = pk)
    b.delete()
    
    return redirect('my_msg')
