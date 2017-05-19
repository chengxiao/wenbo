# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response,HttpResponse
from .models import BlogPage,BlogContent,Nav,Cate,MyInfo,SysInfo,Producuct
from django.http import Http404
from captcha.fields import CaptchaField
from .forms import AddForm


def index(request):
    return render(request,'head.html')


def add(request):
    register_form = AddForm()
    response  = render(request,'form.html',{"register_form": register_form},)
    response.set_cookie('postToken',value='allow')
    return response

def add2(request):
    if request.COOKIES['postToken'] !='allow':
        return HttpResponse('请不要重复提交数据!')
    form = AddForm(request.POST)

    if form.is_valid():
        a = form.cleaned_data['name']
        b = form.cleaned_data['age']
        c = MyInfo.objects.create(username = a ,age = int(b))
        c.save()
        response = render(request,'added.html',{'c':c},)
        response.set_cookie('postToken',value='disable')
        return response
    else:
        return HttpResponse('错误')

def home(request):
    l = BlogContent.objects.all()
    nav = Nav.objects.all()
    arcdic = l
    return render_to_response('home.html',{'arcdic':arcdic,'nav':nav},)

def blogdetail(request,id):
    try:
        blog = BlogContent.objects.get(id=id)
        cate =blog.cate.all()
    except BlogContent.DoesNotExist:
        raise Http404
    return render(request,'blogcontent.html',{'blog':blog,'cate':cate,},)

def bloglist(request):
    bloglist = BlogContent.objects.filter(display=True).order_by('ob')
    return render(request,'list.html',{'bloglist':bloglist})

def CateList(request,id):
    catelist = Cate.objects.get(id=id)
    CL = catelist.blogcontent_set.all()
    return render(request,'catelist.html',{'CL':CL})

def AboutUs(request,name):
    try:
        page = BlogPage.objects.get(vname=name, display=True)
    except BlogPage.DoesNotExist:
        raise Http404
    return render(request,'page.html',{'page':page})

def Header(request):
    return render(request,'header.html')

def Main(request):
    news = BlogContent.objects.all()[:10]
    pros = Producuct.objects.all()[:5]
    return render(request,'main.html',{'news':news,'pros':pros})

def Pro(request,id):
    try:
        product = Producuct.objects.get(id=id)
    except BlogContent.DoesNotExist:
        raise Http404
    return render(request,'product.html',{'product':product})

def Prolist(request):
    prolist = Producuct.objects.all()
    return render(request,'prolist.html',{'prolist':prolist})

def Newslist(request):
    newslist = BlogContent.objects.all()
    return render(request,'newslist.html',{'newslist':newslist})

def News(request,id):
    try:
        news = BlogContent.objects.get(id=id)
    except BlogContent.DoesNotExist:
        raise Http404
    return render(request,'news.html',{'news':news})




