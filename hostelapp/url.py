from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view_student, name='home'),
    path("block/", views.block_views, name='block'),

    path('floor/<str:pk>/', views.floor, name='floor'),
    path('rooms/<str:pk>/', views.rooms, name='rooms'),
     path('gatepass/', views.gatepass_view, name='gatepass'),
    path('confirmation/booking/<str:pk>/', views.booking_form_views, name='confirmation_booking'),
    path('gatepass_status/',views.gatepass_state,name='gatepass_status'),
    path('raise_issue/',views.raise_issue_view,name='issue_student'),
    path('issue_raisers/',views.issue_raisers_view,name='issueraise'),
    path('upvote/<str:pk>/',views.upvote_view,name='upvote'),
    path('downvote/<str:pk>/',views.downvote_view,name='downvote'),
]
