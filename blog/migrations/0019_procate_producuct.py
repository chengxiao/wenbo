# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 14:10
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_sysinfo_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProCate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='\u4ea7\u54c1\u680f\u76ee')),
                ('description', models.TextField(max_length=300, verbose_name='\u680f\u76ee\u4ecb\u7ecd')),
                ('ob', models.IntegerField(default=99, verbose_name='\u6392\u5e8f')),
                ('display', models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b\u7ba1\u7406',
                'verbose_name_plural': '\u5206\u7c7b\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Producuct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('imgage', models.ImageField(blank=True, upload_to='uploads/images/', verbose_name='\u4ea7\u54c1\u5c0f\u56fe')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='\u5185\u5bb9')),
                ('ob', models.IntegerField(default=99, verbose_name='\u6392\u5e8f')),
                ('display', models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u7ba1\u7406',
                'verbose_name_plural': '\u4ea7\u54c1\u7ba1\u7406',
            },
        ),
    ]