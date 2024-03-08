# Generated by Django 4.2.7 on 2024-03-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed_interest', '0003_grouppost_created_at_alter_grouppost_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouppost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/group_post_images'),
        ),
        migrations.AlterField(
            model_name='grouppost',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Расскажите что сегодня было интересного'),
        ),
    ]