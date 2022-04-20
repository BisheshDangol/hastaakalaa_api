from django.contrib import admin

from follow import models


# Register your models here.
@admin.register(models.Follow)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'follower_id')