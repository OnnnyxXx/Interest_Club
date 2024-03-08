# Generated by Django 4.2.7 on 2024-03-01 14:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed_interest', '0002_grouppost_interest_group_group_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouppost',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='grouppost',
            name='text',
            field=models.TextField(verbose_name='Расскажите что сегодня было интересного'),
        ),
    ]
