# Generated by Django 3.0.8 on 2020-07-12 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_userprofile_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_bool',
        ),
    ]
