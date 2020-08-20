from django.urls import path

from . import views

app_name = 'findfriend'
urlpatterns = [
    path('find/', views.find, name = "find"),
    path('sentReq/<str:friendname>/', views.sentReq, name = "sentReq"),
    path('received/', views.receivedReq, name = "received"),
    path('process/<str:action>/<str:friendname>', views.process, name = 'process'),
]
