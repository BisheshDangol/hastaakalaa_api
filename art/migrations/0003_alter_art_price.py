# Generated by Django 4.0.2 on 2022-02-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_alter_art_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='price',
            field=models.IntegerField(),
        ),
    ]