# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170411_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='cate',
            name='display',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a'),
        ),
    ]
