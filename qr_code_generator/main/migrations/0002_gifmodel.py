# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GifModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('colorful', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='pictures')),
            ],
            options={
                'db_table': 'gif',
            },
        ),
    ]
