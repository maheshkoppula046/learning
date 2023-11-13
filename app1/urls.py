from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('men/', views.men),
    path('women/', views.women),
    path('services/', views.services),
    path('clothes/', views.clothes),
]