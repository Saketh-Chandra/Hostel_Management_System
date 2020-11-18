from django.urls import path
from . import views

urlpatterns = [path('test/', views.create_block, name='create_block_view')
               ]