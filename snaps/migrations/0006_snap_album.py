# Generated by Django 2.0.7 on 2018-08-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0005_auto_20180826_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='snap',
            name='album',
            field=models.ManyToManyField(related_name='album_snaps', to='snaps.Album'),
        ),
    ]
