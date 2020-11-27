from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view_student, name='home'),
    path("block/",views.block_views,name='block'),
    # path('student/sample/', views.sam, name='sample'),
    path('floor/<str:pk>/', views.floor, name='floor'),
    path('rooms/<str:pk>/', views.rooms, name='rooms'),
    # path('student/profile/', views.student, name='student'),
    # path('warden/profile', views.warden, name='warden'),
    path('confirmation/booking/<str:pk>/', views.booking_form_views, name='confirmation_booking')
]
