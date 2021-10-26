from datetime import datetime
from typing import Reversible

from django.http.response import HttpResponseRedirect
from adminpart.models import AllocateHouseDetail, HouseDetail, SocietyDetail
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from . import forms
from default.models import *

import requests
import json

# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pwd']
        user = authenticate(username = username, password = password)
        print(user)
        # if user is not None:
        if user:
                if user.is_active:
                    login(request, user)
                    request.session['admin_login'] = username
                    return redirect('home')
        

    return render(request,'admin/admin_login.html',{'title':'login'})

def admin_logout(request):
    #del request.session['admin_login']
    logout(request)
    return redirect('/')
    # return HttpResponseRedirect(Reversible('index'))

def home(request):
    return render(request,'admin/master.html',{"title":"master page"})

def add_society(request):

    if request.method == 'POST':
        form = forms.SocietyRegistration(request.POST,request.FILES)
        if form.is_valid():
            obj = SocietyDetail()
            obj.sname = form.cleaned_data['sname']
            obj.address = form.cleaned_data['address']
            obj.city = form.cleaned_data['city']
            obj.pincode = form.cleaned_data['pincode']
            obj.nohouse = form.cleaned_data['nohouse']
            obj.image = form.cleaned_data['image']
            obj.save()
            return redirect('home')

    return render(request,'admin/add_society.html',{"title":"add society"})

def add_house(request):

    if request.method == 'POST':
        form = forms.HouseRegistration(request.POST,request.FILES)
        if form.is_valid():
            obj = HouseDetail()
            # if request.POST.get("sname"):
                # obj.sname = request.POST.get("sname")
            obj.sname = form.cleaned_data['sname']
            obj.blockno = form.cleaned_data['blockno']
            obj.type = form.cleaned_data['type']
            obj.detail = form.cleaned_data['detail']
            obj.image = form.cleaned_data['image']
            obj.save()
            return redirect('home')
        else:
            print(form.errors)
            return redirect('home')

    return render(request,'admin/add_house.html',{"title":'add house','obj':SocietyDetail.objects.all()})

def h_report(request):

    if request.method == "POST":
        sname = request.POST['sname']
        dct = {"title":"house report","data": HouseDetail.objects.all(),"obj": SocietyDetail.objects.all(),'sname' : sname}
        return render(request,'admin/house_report.html',dct)

    content = {"title":"house report" , "obj": SocietyDetail.objects.all()}
    return render(request,'admin/house_report.html',content)

def delete(request,pk):
    print(pk)
    a = HouseDetail.objects.get(id = pk)
    b = AllocateHouseDetail.objects.get(sname = a.sname , blockno = a.blockno)
    c = Complain.objects.all()
    for i in c:
        if i.username == b.username:
            i.delete()
    d = Message.objects.all()
    for i in d:
        if i.sender_name == b.username or i.receiver_name == b.username:
            i.delete()
    e = Rent_List.objects.all()
    for i in e:
        if i.username == b.username:
            i.delete()
    e = Sell_List.objects.all()
    for i in e:
        if i.username == b.username:
            i.delete()
    b.delete()
    a.delete()

    return redirect('house_report')
    # content = {"title":"house report" , "obj": SocietyDetail.objects.all()}
    # return render(request,'admin/house_report.html',content)

def h_allocate(request):
    if request.method == 'POST':
        form = forms.AllocateHouse(request.POST,request.FILES)
        if form.is_valid():
            obj = AllocateHouseDetail()
            obj.fname = form.cleaned_data['fname']
            obj.lname = form.cleaned_data['lname']
            obj.dob = form.cleaned_data['dob']
            obj.blockno = form.cleaned_data['blockno']
            obj.sname = form.cleaned_data['sname']
            obj.members = form.cleaned_data['members']
            obj.username = form.cleaned_data['username']
            obj.password = form.cleaned_data['password']
            obj.mobile_no = form.cleaned_data['mobile_no']
            obj.image = form.cleaned_data['image']
            obj.save()
            a = obj.mobile_no
            b = obj.username
            c = obj.password
            print(a)
            msgsending(a,b,c)
            
            return redirect("home")
        else:
            print(form.errors)

    return render(request,'admin/allocate_house.html',{"sname":SocietyDetail.objects.all(),'title':'house allocate'})

def m_report(request):
    if request.method == "POST":
        sname = request.POST['sname']
        dct = {"data" : AllocateHouseDetail.objects.all() , "title" : "member report" , "obj":SocietyDetail.objects.all() , 'sname':sname}
        return render(request,'admin/member_report.html',dct)
    dct = {"title" : "member report", "obj":SocietyDetail.objects.all()}
    return render(request,'admin/member_report.html',dct)

def delete_member(request,pk):
    a = AllocateHouseDetail.objects.get(username = pk)
    c = Complain.objects.all()
    for i in c:
        if i.username == a.username:
            i.delete()
    d = Message.objects.all()
    for i in d:
        if i.sender_name == a.username or i.receiver_name == a.username:
            i.delete()
    e = Rent_List.objects.all()
    for i in e:
        if i.username == a.username:
            i.delete()
    e = Sell_List.objects.all()
    for i in e:
        if i.username == a.username:
            i.delete()
    a.delete()
    return redirect('member_report')

def admin_complain(request):
    dct = {'title':'complain list','obj':Complain.objects.all()}
    return render(request,'admin/complain_list.html',dct)

def sh_report(request):
    dct = {'title':'sell house report','obj':Sell_List.objects.all(),'sname':SocietyDetail.objects.all()}
    return render(request,'admin/admin_sell_list.html',dct)

def delete_sh(request,pk):
    a = Sell_List.objects.get(id = pk)
    a.delete()
    return redirect('sell_h_report')

def rh_report(request):
    dct = {'title':'sell house report','obj':Rent_List.objects.all(),'sname':SocietyDetail.objects.all()}
    return render(request,'admin/admin_rent_list.html',dct)

def delete_rh(request,pk):
    a = Rent_List.objects.get(id = pk)
    a.delete()
    return redirect('rent_h_report')

def society_report(request):
    dct = {'title':'Society list','obj':SocietyDetail.objects.all()}
    return render(request,'admin/admin_society_list.html',dct)

def delete_society(request,pk):
    a = SocietyDetail.objects.filter(sname = pk)
    a.delete()
    b = HouseDetail.objects.all()
    for i in b:
        if i.sname == pk:
            i.delete()
    d = Rent_List.objects.all()
    for j in d:
        if j.sname == pk:
            j.delete()

    e = Sell_List.objects.all()
    for k in e:
        if k.sname == pk:
            k.delete()
    c = AllocateHouseDetail.objects.all()
    for l in c:
        if l.sname == pk:
            cmp = Complain.objects.all()
            msg = Message.objects.all()
            for r in cmp:
                if r.username == l.username:
                    r.delete()
            for r in msg:
                if r.sender_name == l.username or r.receiver_name == l.username:
                    r.delete()
            l.delete()
    
    return redirect('society_report')

def solve(request,pk):
    a = Complain.objects.get(id = pk)
    a.delete()
    return redirect('admin_complain')

def msgsending(num,uname,pas):
    # mention url
    url = "https://www.fast2sms.com/dev/bulk"

    # create a dictionary
    my_data = {
         # Your default Sender ID
        'sender_id': 'FSTSMS', 
    
        # Put your message here!
        'message': 'Your Username and Password for Ehousing is\nUsername : '+uname+'\nPassword : '+pas, 
    
        'language': 'english',
        'route': 'p',
    
        # You can send sms to multiple numbers
        # separated by comma.
        'numbers': num    
    }
  
    # create a dictionary
    headers = {
        'authorization': 'your fast2sms api key',
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }
    # make a post request
    response = requests.request("POST",
                                url,
                                data = my_data,
                                headers = headers)
    #   json.load json data from source
    returned_msg = json.loads(response.text)
  
    # print the send message
    print(returned_msg['message'])