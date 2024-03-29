# Generated by Django 4.0.2 on 2022-02-23 08:38

import art.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(default='posts/default.png', upload_to=art.models.upload_to, verbose_name='Image')),
                ('description', models.TextField(max_length=300)),
                ('slug', models.SlugField(max_length=250)),
                ('price', models.IntegerField(unique_for_date='published')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('for_sale', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('showcase', 'Showcase'), ('purchased', 'purchased'), ('available', 'Available')], default='available', max_length=10)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
