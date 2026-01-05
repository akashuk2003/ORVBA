from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, MechanicProfile

# 1. Customer Registration
class CustomerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number',)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
        return user

# 2. Mechanic Registration (Multi-part form)
class MechanicSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea)
    id_proof = forms.FileField(required=True, help_text="Upload valid ID (PDF/Image)")
    latitude = forms.FloatField(widget=forms.HiddenInput(), initial=0.0) # Will be filled by JS
    longitude = forms.FloatField(widget=forms.HiddenInput(), initial=0.0)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_mechanic = True
        if commit:
            user.save()
            # Create the Profile
            MechanicProfile.objects.create(
                user=user,
                address=self.cleaned_data['address'],
                id_proof=self.cleaned_data['id_proof'],
                latitude=self.cleaned_data['latitude'],
                longitude=self.cleaned_data['longitude']
            )
        return user