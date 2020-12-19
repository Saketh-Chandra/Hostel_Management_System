"""Hostel_Room_Booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.http import HttpResponse
from accounts.views import default_home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', default_home, name='default_home_name'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.url')),
    path('student/', include('hostelapp.url')),
    path('cheif_warden/', include('cheif_warden.url')),
    path('warden/', include('Wardenapp.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
