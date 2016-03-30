#coding:utf-8
from django.contrib import admin

# Register your models here.'

from .models import Article
from .models import Url

#把列表注册到后台
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_date','update_time',)

admin.site.register(Article,ArticleAdmin)


#把sso_url注册到后台
class UrlAdmin(admin.ModelAdmin):
    list_display = ('url_name','url_url','url_parameter','url_note','add_date','update_time')

admin.site.register(Url,UrlAdmin)

#重写权限
class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)

#定制搜索功能
class PersonAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    search_fields = ('title','content')

    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct = super(PersonAdmin,self).get_search_results(request,queryset,search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return  queryset,use_distinct