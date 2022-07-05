# Generated by Django 3.2.13 on 2022-07-05 12:14

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('activity_location', models.CharField(max_length=200)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ideas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
