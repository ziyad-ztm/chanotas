# Generated by Django 4.2.4 on 2023-08-07 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='received_by',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='sent_by',
        ),
    ]