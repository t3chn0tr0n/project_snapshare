# Generated by Django 2.0.7 on 2018-08-25 14:17

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, null=True)),
                ('weight', models.PositiveIntegerField(default=0, null=True)),
                ('likes', models.PositiveIntegerField(default=0, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('author', models.CharField(default='', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Snap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', null=True, upload_to='images/')),
                ('name', models.TextField(default='', max_length=20, null=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('caption', models.CharField(default=models.TextField(default='', max_length=20, null=True), max_length=30, null=True)),
                ('likes', models.PositiveSmallIntegerField(default=0, null=True)),
                ('authur', models.CharField(default='', max_length=30, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=20), default=[], null=True, size=None)),
            ],
        ),
    ]
