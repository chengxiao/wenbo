# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20170417_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sysinfo',
            options={'verbose_name': '\u7ad9\u70b9\u4fe1\u606f', 'verbose_name_plural': '\u7ad9\u70b9\u4fe1\u606f'},
        ),
        migrations.AddField(
            model_name='sysinfo',
            name='address',
            field=models.CharField(default='', max_length=200, verbose_name='\u5730\u5740'),
        ),
        migrations.AddField(
            model_name='sysinfo',
            name='description',
            field=models.TextField(default='', max_length=300, verbose_name='\u7ad9\u70b9\u63cf\u8ff0'),
        ),
        migrations.AddField(
            model_name='sysinfo',
            name='mail',
            field=models.CharField(default='', max_length=50, verbose_name='\u90ae\u4ef6\u5730\u5740'),
        ),
        migrations.AddField(
            model_name='sysinfo',
            name='qq',
            field=models.CharField(default='', max_length=30, verbose_name='\u8054\u7cfbqq'),
        ),
        migrations.AddField(
            model_name='sysinfo',
            name='tel',
            field=models.CharField(default='', max_length=15, verbose_name='\u7535\u8bdd'),
        ),
        migrations.AddField(
            model_name='sysinfo',
            name='url',
            field=models.CharField(default='', max_length=70, verbose_name='\u7ad9\u70b9\u5730\u5740'),
        ),
    ]
