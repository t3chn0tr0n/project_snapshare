# Generated by Django 2.0.7 on 2018-08-25 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0003_snap_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snap',
            name='album',
        ),
    ]
