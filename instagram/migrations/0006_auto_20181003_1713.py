# Generated by Django 2.1.2 on 2018-10-03 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_auto_20181003_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
    ]
