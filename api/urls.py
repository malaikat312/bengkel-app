
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.BengkelListCreateAPIView.as_view(), name='bengkel-list-create'),
    path('api/login/', views.LoginAPIView.as_view(), name='login'),
     path('api/token/', obtain_auth_token, name='api-token'),
    path('api/register/', views.RegisterAPIView.as_view(), name='register'),
    path('bengkels/<int:pk>/', views.BengkelRetrieveUpdateDestroyAPIView.as_view(), name='bengkel-detail'),
    path('layanans/', views.LayananListCreateAPIView.as_view(), name='layanan-list-create'),
    path('layanans/<int:pk>/', views.LayananRetrieveUpdateDestroyAPIView.as_view(), name='layanan-detail'),
]
