from django.contrib import admin
from .models import BlogContent,BlogPage,MyInfo,Cate,Nav,SysInfo,ProCate,Producuct

# Register your models here.

class ArclistAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_date','ob','display','image')

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','ob','display','vname','image')

class MyInfoAdmin(admin.ModelAdmin):
    list_display = ('username','age')

class CateAdmin(admin.ModelAdmin):
    list_display = ('title','ob','display')

class NavAdmin(admin.ModelAdmin):
    list_display = ('title','url','display','ob')

class SystemAdmin(admin.ModelAdmin):
    list_display = ('sitename','keywords','description','url')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','cate','ob','display')

class ProCateAdmin(admin.ModelAdmin):
    list_display = ('title','description','ob','display')



admin.site.register(BlogContent,ArclistAdmin)
admin.site.register(BlogPage,PageAdmin)
admin.site.register(MyInfo,MyInfoAdmin)
admin.site.register(Cate,CateAdmin)
admin.site.register(Nav,NavAdmin)
admin.site.register(SysInfo,SystemAdmin)
admin.site.register(Producuct,ProductAdmin)
admin.site.register(ProCate,ProCateAdmin)



