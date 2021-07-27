from django.urls import path
from . import views


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.ViewPhoto, name='photo'),
    path('add/', views.AddPhoto, name='add'),
    
    ]