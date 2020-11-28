from django import forms
from django.forms import ModelForm
from hostelapp.models import room


class hidden_room_form(forms.ModelForm):
    class Meta:
        model = room
        fields = ['hide']
