from hostelapp.models import *
from django import forms
from django.forms import ModelForm


class Block_form(forms.ModelForm):
    class Meta:
        model = blocks
        fields = '__all__'


class floor_form(forms.ModelForm):
    class Meta:
        model = floors
        fields = '__all__'


class room_form(forms.ModelForm):
    class Meta:
        model = room
        fields = '__all__'


class warden_form(forms.ModelForm):
    class Meta:
        model = warden
        fields = '__all__'


class Booking_form(forms.ModelForm):
    class Meta:
        model = student_room
        fields = '__all__'


class update_booking_form(forms.ModelForm):
    class Meta:
        model = student_room
        fields = ['user_room']


class update_warden_form(forms.ModelForm):
    class Meta:
        model = warden
        fields = ['Block_Name', 'Floor_Number']
