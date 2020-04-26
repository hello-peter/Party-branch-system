from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
import sys
sys.path.append('../dzb')
import os
# Create your models here.
class User(models.Model):
    u_name=models.CharField(max_length=18)
    u_age=models.IntegerField(default=18)

class Logfile(models.Model):
    file = models.FileField(u'文件', upload_to='excel/', null=False, blank=False)
    file_name = models.CharField(u'文件名称', max_length=50, default='logfile_name', null=False)
    create_time = models.DateTimeField(u'创建时间', null=False)
    host_ip = models.CharField(u'主机IP', max_length=50, default='127.0.0.1', null=False)
    comment = models.CharField(u'备注说明', max_length=100, null=False)
    isanalyse = models.BooleanField(u'是否分析', default='0', null=False)

@receiver(post_delete, sender=Logfile)
def delete_upload_files(sender, instance, **kwargs):
    files = getattr(instance, 'file')
    if not files:
        return
    fname = os.path.join(settings.MEDIA_ROOT, str(files))
    if os.path.isfile(fname):
        os.remove(fname)

class teacher(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)
    introduce = models.CharField(max_length=100)

class about_us(models.Model):
    text = models.CharField(max_length = 500)


class students(models.Model):
    img = models.ImageField(upload_to='stu_img')
    major_in = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)
    position = models.CharField(max_length = 20)

class missions(models.Model):
    dzb_name = models.CharField(max_length=20)
    mission_name = models.CharField(max_length=100)
    missions_principle = models.CharField(max_length=20)

class activity(models.Model):
    img = models.ImageField(upload_to='img')
    introduce = models.CharField(max_length=100)