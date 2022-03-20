from django.contrib import admin
from . import models

@admin.register(models.Art)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'user', 'image', 'description', 'slug', 'price', 'status', 'genre', 'for_sale', 'published', 'get_likes', 'get_bookmarks')
    # prepopulated_fields = {'slug':('title',), }

# @admin.register(models.Vote)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'art_id')

@admin.register(models.Art.likes.through)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'newuser_id', 'art_id')
    # prepopulated_fields = {'slug':('title',), }