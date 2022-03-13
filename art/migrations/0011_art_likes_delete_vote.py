# Generated by Django 4.0.2 on 2022-03-12 06:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('art', '0010_remove_vote_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='likes',
            field=models.ManyToManyField(related_name='art_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]