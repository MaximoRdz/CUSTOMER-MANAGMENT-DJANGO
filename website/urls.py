from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),       # since located in root only ''
]