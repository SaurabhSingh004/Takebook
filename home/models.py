from django.db import models

from register.models import user

class friends(models.Model):
    mUsername = models.ForeignKey(user, on_delete=models.CASCADE, related_name='user')
    mFriendUser = models.ForeignKey(user, on_delete=models.CASCADE, related_name='userfriend')

class Posts(models.Model):
    mUser = models.ForeignKey(user, on_delete=models.CASCADE)
    mLikes = models.IntegerField(default=0)
    mCaption = models.CharField(default="", max_length=199)
    mPhoto = models.TextField(default=None)