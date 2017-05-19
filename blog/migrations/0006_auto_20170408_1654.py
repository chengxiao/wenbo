# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SysInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(max_length=255, verbose_name='\u7ad9\u70b9\u540d\u79f0')),
                ('keywords', models.CharField(max_length=10, verbose_name='\u5173\u952e\u8bcd')),
            ],
        ),
        migrations.AddField(
            model_name='myinfo',
            name='password',
            field=models.CharField(default=123, max_length=50),
        ),
    ]
