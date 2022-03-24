# Generated by Django 4.0.2 on 2022-03-20 07:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('art', '0016_remove_art_bookmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, related_name='bookmark_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
