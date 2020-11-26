from django.urls import path
from . import views

urlpatterns = [path('',views.cheif_warden,name='cheif_warden_home'),
               path('block/', views.create_block, name='create_block_view'),
               path('warden/',views.create_warden,name='create_warden'),
               path('room/',views.create_room,name='create_room'),
               path('floor/',views.create_floor,name='create_floor'),
               path('update/student_room/<str:pk>',views.update_student_room,name='update_student_room_name')
               ]