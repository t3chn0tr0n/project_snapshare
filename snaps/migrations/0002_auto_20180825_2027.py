# Generated by Django 2.0.7 on 2018-08-25 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snap',
            old_name='authur',
            new_name='author',
        ),
    ]