from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('users/', views.get_users, name='get_users'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),  # fixed endpoint
]
