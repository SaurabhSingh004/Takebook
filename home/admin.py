from django.contrib import admin

from .models import friends, Posts

admin.site.register(friends)
admin.site.register(Posts)