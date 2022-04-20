from django.contrib import admin

from payment import models

# Register your models here.
# Register your models here.
@admin.register(models.Payment)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer_id', 'seller_id', 'price' )