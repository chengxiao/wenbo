# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20170428_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='sysinfo',
            name='logo',
            field=models.ImageField(blank=True, upload_to='uploads/images/', verbose_name='logo'),
        ),
    ]
