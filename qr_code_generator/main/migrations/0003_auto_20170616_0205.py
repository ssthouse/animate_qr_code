# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_gifmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='gifmodel',
            name='result',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='gifmodel',
            name='picture',
            field=models.ImageField(upload_to='static/pictures'),
        ),
    ]