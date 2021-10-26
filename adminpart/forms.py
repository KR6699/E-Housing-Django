from django import forms
from django.db.models import fields
from django.forms.forms import Form
from . import models

class SocietyRegistration(forms.ModelForm):

    class Meta:
        model = models.SocietyDetail
        fields = "__all__"

class HouseRegistration(forms.ModelForm):

    class Meta:
        model = models.HouseDetail
        fields = '__all__'

class AllocateHouse(forms.ModelForm):

    class Meta:
        model = models.AllocateHouseDetail
        fields = '__all__'