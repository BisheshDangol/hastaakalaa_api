from django.utils import timezone
from django.conf import settings
from django.db import models

from art.models import Art

User = settings.AUTH_USER_MODEL

class Comment(models.Model):
    user = models.ForeignKey(User, default=1, null = True, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, default=1, null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    published = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    