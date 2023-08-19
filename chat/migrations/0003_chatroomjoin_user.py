# Generated by Django 4.2.4 on 2023-08-19 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_chatmessage_user_alter_chatmessage_chatroom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroomjoin',
            name='user',
            field=models.ForeignKey(db_column='user_id', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_join', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
