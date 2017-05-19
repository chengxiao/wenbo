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
    image = models.ImageField(upload_to='uploads/images/', blank=True)



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
    image = models.ImageField(upload_to='uploads/images/',blank=True)


    class Meta:
        verbose_name = "页面管理"
        verbose_name_plural = "页面管理"

class SysInfo(models.Model):
    sitename = models.CharField(u'站点名称',max_length=255)
    logo = models.ImageField(u'logo',upload_to='uploads/images/',blank=True)
    keywords = models.CharField(u'关键词',max_length=10)
    description = models.TextField(u'站点描述',max_length=300,default='')
    tel = models.CharField(u'电话',max_length=15,default='')
    address = models.CharField(u'地址',max_length=200,default='')
    qq = models.CharField(u'联系qq',max_length=30,default='')
    mail = models.CharField(u'邮件地址',max_length=50,default='')
    url = models.CharField(u'站点地址',max_length=70,default='')


    class Meta:
        verbose_name = '站点信息'
        verbose_name_plural = '站点信息'

class Nav(models.Model):
    title = models.CharField(u'菜单名称',max_length=30)
    url = models.CharField(u'地址',max_length=255)
    display = models.BooleanField(u'是否显示',default=True)
    ob = models.IntegerField(u'排序',default=99)

    class Meta:
        verbose_name = "导航管理"
        verbose_name_plural = "菜单管理"

class ProCate(models.Model):
    title= models.CharField(u'产品栏目',max_length=30)
    description = models.TextField(u'栏目介绍',max_length=300)
    ob = models.IntegerField(U'排序',default=99)
    display = models.BooleanField(u'是否显示',default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '产品分类'
        verbose_name_plural = '产品分类'

class Producuct(models.Model):
    title = models.CharField(u'产品名称',max_length=30)
    imgage = models.ImageField(u'产品小图',upload_to='uploads/images/',blank=True)
    content = UEditorField('内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')
    ob = models.IntegerField(u'排序',default=99)
    display = models.BooleanField(u'是否显示',default=True)
    cate = models.ForeignKey('ProCate',verbose_name='栏目',default='')
    pub_time = models.DateTimeField(u'发布时间',auto_now_add=True,editable=True,blank=True)
    tag = models.CharField(u'标签',default='',max_length=30)

    class Meta:
        verbose_name = '产品管理'
        verbose_name_plural = '产品管理'













