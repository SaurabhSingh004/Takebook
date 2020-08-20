from django.db import models

from register.models import user

class friends(models.Model):

    mUsername = models.ForeignKey(user, on_delete=models.CASCADE, related_name='user')
    mFriendUser = models.ForeignKey(user, on_delete=models.CASCADE, related_name='userfriend')