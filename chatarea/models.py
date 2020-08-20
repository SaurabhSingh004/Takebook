from django.db import models

from register.models import user

class Chat(models.Model):
    mFrom = models.ForeignKey(user, on_delete=models.CASCADE, related_name='From')
    mTo = models.ForeignKey(user, on_delete=models.CASCADE, related_name='To')
    mSent = models.CharField(max_length=100, default=None, null=True)
    mReceived = models.CharField(max_length=100, default=None, null=True)