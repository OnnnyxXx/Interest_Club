# Generated by Django 4.2.7 on 2024-03-01 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed_interest', '0005_alter_grouppost_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest_group',
            name='group_posts',
        ),
    ]