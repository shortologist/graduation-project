# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-25 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='driver-photo'),
        ),
    ]
