from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('volunteer/form/', views.volunteerform, name='volunteerform'),
    path('volunteer/update/', views.updateform, name='updateform'),

    path('burnnotice/', views.burnnotice, name='burnnotice'),
    path('events/', views.events, name='events'),
    path('educational/', views.educational, name='educational'),
]