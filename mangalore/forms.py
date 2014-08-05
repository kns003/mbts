'''
Created on 27-Jul-2014

@author: shashank
'''
from mangalore.models import Bus
from django import forms
from django.db.models import Q

class RouteForm(forms.Form):
    source = forms.CharField(max_length=30)
    destination = forms.CharField(max_length = 30)
    
#     def clean_source(self):
#         source = self.cleaned_data.get('source','')
#         destination = self.cleaned_data.get('destination','')
#         print source+" in forms"
#         print destination+" in forms"
#         buses = Bus.objects.filter(Q(stops__iexact = source),Q(stops__iexact = destination))
#         if not buses:
#             raise forms.ValidationError("No Bus no. exists with this Source and destination.")
#         return source