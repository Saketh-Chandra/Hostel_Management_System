from django import forms
from django.forms import ModelForm
from .models import *


# from django import DateInput


class Booking_form(forms.ModelForm):
    class Meta:
        model = student_room
        fields = []


class DateInput(forms.DateInput):
    input_type = 'date'


class GatepassForm(forms.ModelForm):
    class Meta:
        model = gatepass
        fields = ['outing_date', 'return_date']
        widgets = {
            'outing_date': DateInput(),
            'return_date': DateInput()
        }
<<<<<<< HEAD

# class IssueStudentForm(forms.ModelForm):
#     class Meta:
#         model=issue_student
#         fields=['upvote','downvote']

class IssueRaiserForm(forms.ModelForm):
    class Meta:
        model=issue_raiser
        fields=['issue']
=======
>>>>>>> 456857cbf5770a301324e6661d2de879f1ffc39c
