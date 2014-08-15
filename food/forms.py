'''
Created on 10-Aug-2014

@author: shashank
'''
from django import forms
from food.models import Product

class ProductForm(forms.Form):
    product_name = forms.CharField(max_length = 30)
    product_description = forms.CharField(widget=forms.Textarea)
    
class SearchForm(forms.Form):
    search = forms.CharField(widget = forms.TextInput())