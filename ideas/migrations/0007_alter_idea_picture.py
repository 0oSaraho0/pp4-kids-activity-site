# Generated by Django 3.2.13 on 2022-07-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0006_alter_idea_activity_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='picture',
            field=models.ImageField(default='placeholder', upload_to='', verbose_name='image'),
        ),
    ]