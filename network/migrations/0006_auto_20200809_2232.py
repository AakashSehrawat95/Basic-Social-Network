# Generated by Django 3.0.7 on 2020-08-09 17:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_delete_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='total_likes',
        ),
        migrations.AddField(
            model_name='post',
            name='liked_by',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
