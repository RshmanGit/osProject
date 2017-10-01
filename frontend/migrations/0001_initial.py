# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-01 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='backupFolder',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('path', models.CharField(max_length=200, unique=True)),
                ('backupPath', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
