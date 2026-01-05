from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'latitude', 'longitude','address']
        widgets = {
            'latitude': forms.HiddenInput(), 
            'longitude': forms.HiddenInput(), 
            'address': forms.HiddenInput(), 
        }