from django.contrib import admin
from . import models
# Register your models here.

class SellListAdmin(admin.ModelAdmin):
    list_display=['id','sname','house_no','type','username','sell_price']

class RentListAdmin(admin.ModelAdmin):
    list_display=['id','sname','house_no','type','username','rent_price']

class ComplainAdmin(admin.ModelAdmin):
    list_display = ['id','username','mobile','subject','content']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','sender_name','receiver_name','subject','message']

admin.site.register(models.Rent_List,RentListAdmin)
admin.site.register(models.Sell_List,SellListAdmin)
admin.site.register(models.Complain,ComplainAdmin)
admin.site.register(models.Message,MessageAdmin)