# Generated by Django 4.2.4 on 2023-09-01 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_merge_20230901_1847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatroomjoin',
            options={'ordering': ['updated_at']},
        ),
    ]