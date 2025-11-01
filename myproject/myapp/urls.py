from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('login/', student_login, name='login'),
    path('register/', student_register, name='register'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout', dashboard, name='logout'),
]