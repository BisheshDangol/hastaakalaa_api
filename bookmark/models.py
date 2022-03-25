from django.conf import settings
from django.db import models

from art.models import Art

User = settings.AUTH_USER_MODEL

class Bookmark(models.Model):
    user = models.ForeignKey(User, default=1, null = True, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, default=1, null=True, on_delete=models.CASCADE)
    
    objects = models.Manager()

  