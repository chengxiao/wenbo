# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20170508_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='producuct',
            name='tag',
            field=models.CharField(default='', max_length=30, verbose_name='\u6807\u7b7e'),
        ),
    ]
