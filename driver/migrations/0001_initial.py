# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-16 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=50)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('snn', models.CharField(max_length=14)),
                ('is_deleted', models.BooleanField(default=False)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.CharField(default='', max_length=25)),
                ('total_orders', models.IntegerField(blank=True, default=0)),
                ('orders_this_month', models.IntegerField(blank=True, default=0)),
                ('salary', models.FloatField(blank=True, default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=13)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='driver.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(blank=True, null=True, upload_to='')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='driver.Driver')),
            ],
        ),
    ]
