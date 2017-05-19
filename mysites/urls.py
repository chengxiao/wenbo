"""mysites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
from django.contrib import auth
from blog import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^add/$',views.add,name='add'),
    url(r'^list/$',views.bloglist,name='list'),
    url(r'^page/(?P<name>[a-z]+)/$',views.AboutUs,name='about'),
    url(r'^added/$',views.add2,name='add2'),
    url(r'^blog/(?P<id>[0-9]+)/$',views.blogdetail,name='detail'),
    url(r'^cate/(?P<id>[0-9]+)/$',views.CateList,name='catelist'),
    url(r'^index/$',views.index,name='index'),
    url(r'^header/$',views.Header,name='header'),
    url(r'^$',views.Main,name='main2'),
    url(r'^product/(?P<id>[0-9]+)/$',views.Pro,name='prodetail'),
    url(r'^prolist/$', views.Prolist, name='prolist'),
    url(r'^newslist/$', views.Newslist, name='newslist'),
    url(r'^news/(?P<id>[0-9]+)/$', views.News, name='newsdetail'),

              ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
