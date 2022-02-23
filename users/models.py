from email.policy import default
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

USER_TYPES = (
    ('art collector', 'Art Collector'),
    ('artist', 'Artist'),
)


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password, last_name, address, user_type, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, last_name, address, user_type, **other_fields)

    def create_user(self, email, user_name, first_name, password, last_name, address, phone_number, user_type, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, last_name=last_name, address=address, phone_number=phone_number, user_type=USER_TYPES, **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):

    # Custom manager this post object that returns the posts that have status published.
    class ArtistObjectManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(user_type='artist')

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=30, blank=False, default="0000000000")
    user_type = models.CharField(choices=USER_TYPES, max_length=100, default="artist")
    is_staff = models.BooleanField(default=False)
    # This true signifies that the user can now use login function
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()
    
    artist_object = ArtistObjectManager()
    # This email is used for the username field field while login
    USERNAME_FIELD = 'email'
    # Required fields that must be filled to submit the form
    REQUIRED_FIELDS = ['user_name', 'first_name']