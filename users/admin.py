from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'last_name', 'address', 'user_type', 'is_active', 'is_staff')
    ordering = ('-email',)
    list_display = ('email', 'id', 'user_name', 'first_name', 'profile_picture', 'last_name', 'address', 'phone_number', 'user_type',
                    'is_active', 'is_staff', 'get_followers', 'get_followedby')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name','address', 'user_type', 'follower', 'followedby')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'address', 'user_type', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)