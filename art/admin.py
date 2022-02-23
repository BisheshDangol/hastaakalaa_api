from django.contrib import admin
from . import models

@admin.register(models.Art)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'user', 'image', 'description', 'slug', 'price', 'status', 'for_sale', 'published')
    prepopulated_fields = {'slug':('title',), }
