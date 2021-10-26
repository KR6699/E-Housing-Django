from django.db import models
from django.db.models.fields import DateTimeField
from datetime import datetime
# Create your models here.
class SocietyDetail(models.Model):
    sname = models.CharField(max_length=50,unique=True)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=50)
    pincode = models.PositiveIntegerField()
    nohouse = models.PositiveIntegerField()
    image = models.FileField(upload_to='upload_society_imgs')

    def __str__(self):
        return self.sname + str(self.pk)

class HouseDetail(models.Model):
    blockno = models.PositiveIntegerField()
    type = models.CharField(max_length=5)
    detail = models.CharField(max_length=200)
    sname = models.CharField(max_length=50)
    image = models.FileField(upload_to="upload_house_imgs")

    def __str__(self):
        return str(self.blockno) + self.sname

class AllocateHouseDetail(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    mobile_no = models.BigIntegerField()
    dob = models.DateField()
    blockno = models.PositiveIntegerField()
    sname = models.CharField(max_length=50)
    members = models.PositiveIntegerField()
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    image = models.FileField(upload_to='allocate_house_detail')
    # entry_date = models.DateTimeField(default = datetime.now().date())

    def __str__(self):
        return self.username

