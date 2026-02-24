from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('register/', views.register, name='register'),
    
]