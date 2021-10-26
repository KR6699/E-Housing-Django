from django import forms
from django.db.models import fields
from django.forms.forms import Form
from . import models

class Rent_ListDetail(forms.ModelForm):

    class Meta:
        model = models.Rent_List
        fields = "__all__"

class Sell_ListDetail(forms.ModelForm):

    class Meta:
        model = models.Sell_List
        fields = "__all__"

class ComplainForm(forms.ModelForm):

    class Meta:
        model = models.Complain
        fields = ("subject","content")

class MessageForm(forms.ModelForm):

    class Meta:
        model = models.Message
        fields = ("subject","message")

