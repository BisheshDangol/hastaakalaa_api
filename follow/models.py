from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL

class Follow(models.Model):
    user_id = models.ForeignKey(User, default=1, null = True, on_delete=models.CASCADE, related_name='user_id')
    follower_id = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE, related_name='follower_id')
    
    objects = models.Manager()
    