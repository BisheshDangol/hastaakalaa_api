from django.contrib import admin

from comment import models


# Register your models here.
@admin.register(models.Comment)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'art', 'description', 'published')