from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.contrib.auth.models import User
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    def clean_email(self):
        demail = self.cleaned_data['email']
        if "amrita.edu" not in demail:
            raise forms.ValidationError("You must be use collage Email ID")
        return demail

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']