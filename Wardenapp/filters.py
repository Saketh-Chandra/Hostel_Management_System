import django_filters

from hostelapp.models import *

class student_roomFilter(django_filters.FilterSet):
    class Meta:
        model=student_room
        fields='__all__'
        exclude=['user_room']


class roomFilter(django_filters.FilterSet):
    class Meta:
        model=room
        fields='__all__'
        exclude=['Floor_Number','Block_Name','Warden_id']

