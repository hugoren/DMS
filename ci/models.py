#-*-coding:utf-8-*-

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import random
import time



#记录文件上传记录
class upload_log(models.Model):
    username = models.CharField(max_length=100)
    upload_record = models.FileField(upload_to='./upload')

    def __unicode__(self):
        return  self.username

class SimpleTask(models.Model):
    task_name = models.CharField(max_length=200)
    start_time = models.DateTimeField('task begin time', default=timezone.now)
    finish_time = models.DateTimeField('task end time', blank=True, null=True)
