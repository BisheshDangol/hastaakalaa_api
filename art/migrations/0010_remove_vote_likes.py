# Generated by Django 4.0.2 on 2022-03-12 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0009_vote_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='likes',
        ),
    ]
