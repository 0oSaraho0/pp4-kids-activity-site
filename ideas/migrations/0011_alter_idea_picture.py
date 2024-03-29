# Generated by Django 3.2.13 on 2022-07-26 15:43

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0010_alter_idea_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='picture',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
