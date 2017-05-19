# -*- coding: utf-8 -*-
from blog.models import Nav,SysInfo,BlogContent

def Navbase(request):
    nav = Nav.objects.all()
    system = SysInfo.objects.get(id=1)
    newlist = BlogContent.objects.all()[:10]
    return {'nav':nav,'system':system,'newlist':newlist}