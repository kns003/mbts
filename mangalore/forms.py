'''
Created on 27-Jul-2014

@author: shashank
'''
from mangalore.models import Bus
from django import forms

class RouteForm(forms.Form):
    source = forms.CharField(max_length=30)
    destination = forms.CharField(max_length = 30)
    