from django.urls import path
from . import views

# Paths for the portfolio app

urlpatterns = [
    path('', views.home, name='home'),
]

