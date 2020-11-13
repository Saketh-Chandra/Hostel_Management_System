from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('sample', views.sam, name='sample'),
    path('floor', views.floor, name='floor'),
    path('rooms', views.rooms, name='rooms'),
    path('student', views.student, name='student'),
    path('warden', views.warden, name='warden'),
]
