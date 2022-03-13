# Generated by Django 4.0.2 on 2022-03-12 09:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('art', '0011_art_likes_delete_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='art_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]