# Generated by Django 4.0.2 on 2022-02-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_alter_art_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
