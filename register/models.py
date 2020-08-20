from django.db import models

class user(models.Model):

    mName = models.CharField(max_length=20)
    mEmail = models.CharField(max_length=30)
    mUsername = models.CharField(max_length=20, primary_key=True)
    mPassword = models.CharField(max_length=25)