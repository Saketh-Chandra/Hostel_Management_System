from django.urls import path
from . import views

urlpatterns = [
    path('floors/<str:pk>', views.floors_view, name='warden_floor1'),
    path('blocks/', views.blocks_view, name='warden_blocks'),
    path('rooms/<str:pk>', views.rooms_view, name='warden_rooms'),
    path('room/student/list/<str:pk>',views.student_view,name='student_rooms_info')

]
