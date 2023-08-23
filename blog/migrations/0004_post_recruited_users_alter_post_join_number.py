# Generated by Django 4.2.4 on 2023-08-21 04:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_remove_post_updatd_at_post_is_compelete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='recruited_users',
            field=models.ManyToManyField(blank=True, related_name='recruited_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='join_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]