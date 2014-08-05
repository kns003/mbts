'''
Created on 27-Jul-2014

@author: shashank
'''
from mangalore.models import Bus
from django import forms

class RouteForm(forms.Form):
    source = forms.CharField(max_length=30)
    destination = forms.CharField(max_length = 30)
    
    def clean_routes(self):
        source = self.cleaned_data.get('source')
        destination = self.cleaned_data.get('destination')
        buses = Bus.objects.all()
        for bus in buses:
            if not [source,destination] in bus.routes:
                raise forms.ValidationError("No Bus no. exists with this Source and destination.")
            elif source == destination or destination == source:
                raise forms.ValidationError("Source and Destination cannot be same")
            return source
                