from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
# from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from crum import get_current_user
from autoslug import AutoSlugField

  
User = settings.AUTH_USER_MODEL
  
status_options = [
        ('showcase', 'Showcase'),
        ('purchased', 'Purchased'),
        ('available', 'Available'),
    ]

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Art(models.Model):
    title = models.CharField(max_length=250)
    user = models.ForeignKey(User, default=1, null = True, on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='posts/default.png')
    description = models.TextField(max_length=300)
    slug = AutoSlugField(populate_from='title')
    price = models.IntegerField()
    published = models.DateTimeField(default=timezone.now)
    # for_sale = boolean field if the post is for sale or not
    for_sale = models.BooleanField(default=True)
    # status = choice field where the status could either be showcase, sold, available
    status = models.CharField(max_length=10, choices=status_options, default='available')
    
    objects = models.Manager()

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        else:
            self.user = user
        super(Art, self).save(*args, **kwargs)

    def __str__(self):
        return self.title