from django.urls import path
from . import views

urlpatterns = [path('hello/',views.hello_world,name='hello'),
               path('login',views.login_views,name='login_page'),
               path('register',views.register_views,name='register_page'),
               path('logout',views.logout_view,name='logout_page')
               ]