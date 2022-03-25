from django.contrib import admin

from bookmark import models


# Register your models here.
@admin.register(models.Bookmark)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'art')