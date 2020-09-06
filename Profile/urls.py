from django.urls import path
from . import views

app_name = 'Profile'
urlpatterns = [
    path('profile', views.profile, name = 'profile'),
]