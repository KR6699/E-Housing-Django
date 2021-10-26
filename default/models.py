from django.db import models

# Create your models here.
class Rent_List(models.Model):

    sname = models.CharField(max_length=50)
    house_no = models.PositiveIntegerField()
    type = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    rent_price = models.PositiveIntegerField()

class Sell_List(models.Model):

    sname = models.CharField(max_length=50)
    house_no = models.PositiveIntegerField()
    type = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    sell_price = models.PositiveIntegerField()

class Complain(models.Model):

    username = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    subject = models.CharField(max_length=20)
    content = models.CharField(max_length=20)

class Message(models.Model):

    sender_name = models.CharField(max_length=200)
    receiver_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=5000)