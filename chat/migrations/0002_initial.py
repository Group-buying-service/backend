# Generated by Django 4.2.4 on 2023-09-02 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroomjoin',
            name='user',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='post',
            field=models.OneToOneField(db_column='post_id', on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='chatroom',
            field=models.ForeignKey(db_column='chatroom_id', on_delete=django.db.models.deletion.CASCADE, related_name='chat_room', to='chat.chatroom'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='user',
            field=models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]