from django.contrib import admin
from . import models
# Register your models here.

class HouseDetailAdmin(admin.ModelAdmin):
    list_display=['id','blockno','detail','sname','image','type']

class SocietyDetailAdmin(admin.ModelAdmin):
    list_display = ['id','sname','address','city','pincode','nohouse','image']

class AllocateHouse(admin.ModelAdmin):
    list_display = ['id','fname','lname','mobile_no','members','dob','sname','blockno','image','username','password']

admin.site.register(models.SocietyDetail,SocietyDetailAdmin)
admin.site.register(models.HouseDetail,HouseDetailAdmin)
admin.site.register(models.AllocateHouseDetail,AllocateHouse)
