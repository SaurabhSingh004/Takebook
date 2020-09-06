from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('register.urls')),
    path('', include('home.urls')),
    path('chat/', include('chatarea.urls')),
    path('', include('Profile.urls')),
    path('home/', include('findfriend.urls')),
    path('admin/', admin.site.urls),
]
