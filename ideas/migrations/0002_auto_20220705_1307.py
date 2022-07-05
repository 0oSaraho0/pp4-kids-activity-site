# Generated by Django 3.2.13 on 2022-07-05 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idea',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='idea',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='idea',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='idea_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='idea',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ideas.idea')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
