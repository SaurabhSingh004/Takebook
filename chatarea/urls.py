from django.urls import path

from . import views

app_name = 'chatarea'
urlpatterns = [
    path('', views.chat, name = 'chat'),
    path('<str:friend>/', views.chatarea, name = 'chatarea'),
]
