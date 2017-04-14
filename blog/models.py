# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField



class Cate(models.Model):
    title = models.CharField(u'栏目标题',max_length=10)
    describtion = models.TextField(u'描述')
    ob = models.IntegerField(u'排序',default=99)
    display = models.BooleanField(u'是否显示',default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '分类管理'
        verbose_name_plural = '分类管理'



class MyInfo(models.Model):
    username = models.CharField(max_length=30)
    age = models.IntegerField()
    password = models.CharField(max_length=50,default=123)

    class Meta:
        verbose_name = '评论管理'
        verbose_name_plural = '评论管理'

    def __unicode__(self):
        return self.username

class BlogContent(models.Model):
    title = models.CharField(u'标题',max_length=255)
    content = UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
    pub_date = models.DateTimeField(u'发布时间',auto_now_add=True,editable=True)
    update_date = models.DateTimeField(u'更新时间',auto_now_add=True,null=True)
    cate = models.ManyToManyField(Cate,verbose_name='栏目')
    ob = models.IntegerField(u'排序',default=99)
    display = models.BooleanField(u'是否显示',default=True)

    class Meta:
        verbose_name = "文章管理"
        verbose_name_plural = "文章管理"


    def __unicode__(self):
        return self.title

class BlogPage(models.Model):
    title = models.CharField(u'标题',max_length=255)
    content = UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
    ob = models.IntegerField(u'排序',default=99)
    display = models.BooleanField(u'是否显示',default=True)
    vname=models.CharField(u'页面地址',default='',max_length=10)


    class Meta:
        verbose_name = "页面管理"
        verbose_name_plural = "页面管理"

class SysInfo(models.Model):
    sitename = models.CharField(u'站点名称',max_length=255)
    keywords = models.CharField(u'关键词',max_length=10)

class Nav(models.Model):
    title = models.CharField(u'菜单名称',max_length=30)
    url = models.CharField(u'地址',max_length=255)
    display = models.BooleanField(u'是否显示',default=True)
    ob = models.IntegerField(u'排序',default=99)

    class Meta:
        verbose_name = "导航管理"
        verbose_name_plural = "菜单管理"






