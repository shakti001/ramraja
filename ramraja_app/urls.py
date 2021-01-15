from django.contrib import admin
from django.urls import path, include 
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about , name="about"),
    path('services/', views.services , name="services"),
    path('team/', views.team , name="team"),
    path('contact/', views.contact , name="contact"),


   
]