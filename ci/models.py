#-*-coding:utf-8-*-

from django.db import models

# Create your models here.


#记录文件上传记录
class upload_log(models.Model):
    username = models.CharField(max_length=100)
    upload_record = models.FileField(upload_to='./upload')

    def __unicode__(self):
        return  self.username