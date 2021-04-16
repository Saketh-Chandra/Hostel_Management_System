from django import forms
from django.forms import ModelForm
from hostelapp.models import room
from django.contrib.auth.forms import PasswordChangeForm
from accounts.models import CustomUser

class hidden_room_form(forms.ModelForm):
    class Meta:
        model = room
        fields = ['hide']

class passwordchangingform(PasswordChangeForm):
    old_password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    class Meta:
        model = CustomUser
        fields = ['old_password','new_password1','new_password2']