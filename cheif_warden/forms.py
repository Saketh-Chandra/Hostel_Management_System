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
    def custom_warden_form(self):
        print("-----------------------The id we got from forms------------------------",self.id)
    class Meta:
        model = warden
        fields = '__all__'
