from django import forms
from main.models import *



class RecordForm(forms.ModelForm):
    success_url = 'home'
    class Meta:
        model = record
        fields = ['name', 'number', 'email']