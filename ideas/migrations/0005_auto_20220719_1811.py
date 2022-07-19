# Generated by Django 3.2.13 on 2022-07-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_auto_20220718_1204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idea',
            options={'ordering': ['activity_name']},
        ),
        migrations.RenameField(
            model_name='idea',
            old_name='title',
            new_name='activity_name',
        ),
        migrations.RenameField(
            model_name='idea',
            old_name='featured_image',
            new_name='picture',
        ),
        migrations.RenameField(
            model_name='idea',
            old_name='content',
            new_name='review',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='status',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='user_image',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='web_address',
        ),
        migrations.AddField(
            model_name='idea',
            name='activity_website',
            field=models.URLField(default='https://www.sample.com'),
        ),
        migrations.AddField(
            model_name='idea',
            name='age_range',
            field=models.CharField(choices=[('all_ages', 'All Ages'), ('u1', 'Under 1'), ('1-2', '1 to 2 Years'), ('2-3', '2 to 3 Years'), ('3-5', '3 to 5 Years'), ('6-8', '6 to 8 Years'), ('9-11', '9 to 11 Years'), ('12-14', '12 to 14 Years'), ('15-17', '15 to 17 years'), ('u5', 'Under 5s'), ('u10', 'Under 10s'), ('o10', 'Over 10s')], default='all_ages', max_length=200),
        ),
        migrations.AddField(
            model_name='idea',
            name='cost',
            field=models.CharField(choices=[('free', 'Free'), ('10', 'Under £10 per person'), ('20', 'Under £20 per person'), ('30', 'Under £30 per person'), ('40', 'Under £40 per person'), ('50', 'Under £50 per person'), ('50+', 'Over £50 per person')], default='free', max_length=200),
        ),
    ]
