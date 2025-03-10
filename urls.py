from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('apply', views.apply, name='apply'),
    path('view_status', views.view_status, name='view_status'),
]
