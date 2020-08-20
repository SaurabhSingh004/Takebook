from django.db import models

from register.models import user

class Request(models.Model):
    mSent = models.ForeignKey(user, on_delete=models.CASCADE,related_name="sent")
    mReceived = models.ForeignKey(user, on_delete=models.CASCADE, related_name="received")
