from django import forms
from django.forms import ModelForm
from .models import *




class Booking_form(forms.ModelForm):
    class Meta:
        model = student_room
        fields = []