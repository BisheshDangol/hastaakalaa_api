from django.conf import settings
from django.db import models

from art.models import Art

# Create your models here.
User = settings.AUTH_USER_MODEL

class Payment(models.Model):
    art_id = models.ForeignKey(Art, null = True, on_delete=models.CASCADE, related_name='art_id')
    seller_id = models.ForeignKey(User, default=1, null = True, on_delete=models.CASCADE, related_name='seller_id')
    buyer_id = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE, related_name='buyer_id')
    price = models.CharField(max_length=10)

    objects = models.Manager()
