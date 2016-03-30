#coding:utf-8

from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField('标题',max_length=100)
    content =models.TextField('内容')
    pub_date = models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField('更新时间',auto_now_add=True,editable=True)

    def __unicode__(self):
        return self.title

#各子系统的url
class Url(models.Model):
    url_name = models.CharField('url名称',max_length=500)
    url_url = models.CharField('url地址',max_length=500)
    url_parameter = models.CharField('url参数',max_length=500)
    url_note = models.TextField('备注')
    add_date = models.DateTimeField('新增时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField('更新时间',auto_now_add=True,editable=True)

    # def __unicode__(self):
    #     # dict1 = {self.url_name:self.url_url}
    #     return self.url_url
    #     # return dict1


#各子系统的url
class Url_Permissions(models.Model):
    permissions_all = models.CharField('全部权限',max_length=500)
    permissions_customs = models.CharField('自定义权限',max_length=500)
    permissions_note = models.TextField('备注')
    add_date = models.DateTimeField('新增时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField('更新时间',auto_now_add=True,editable=True)

    def __unicode__(self):
        return self.permissions_all