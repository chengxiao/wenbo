# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20170414_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='img',
            field=models.ImageField(blank=True, upload_to='uploads/images/'),
        ),
    ]
