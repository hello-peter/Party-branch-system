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
    class Meta:
        verbose_name = '查询系统文件'
        verbose_name_plural = verbose_name

@receiver(post_delete, sender=Logfile)
def delete_upload_files(sender, instance, **kwargs):
    files = getattr(instance, 'file')
    if not files:
        return
    fname = os.path.join(settings.MEDIA_ROOT, str(files))
    if os.path.isfile(fname):
        os.remove(fname)

class downloadsfile(models.Model):
    file = models.FileField(u'文件', upload_to='downloads/', null=False, blank=False)
    file_name = models.CharField(u'文件名称', max_length=50, default='文件名', null=False)
    create_time = models.DateTimeField(u'创建时间', null=False)
    class Meta:
        verbose_name = '下载中心文件'
        verbose_name_plural = verbose_name

@receiver(post_delete, sender = downloadsfile)
def delete_upload_files(sender, instance, **kwargs):
    files = getattr(instance, 'file')
    if not files:
        return
    fname = os.path.join(settings.MEDIA_ROOT, str(files))
    if os.path.isfile(fname):
        os.remove(fname)

class teacher(models.Model):
    img = models.ImageField(upload_to='img' ,verbose_name="党建指导老师图片")
    name = models.CharField(max_length=20,verbose_name="党建指导老师姓名")
    introduce = models.CharField(max_length=100,verbose_name="党建指导老师介绍")
    class Meta:
        verbose_name = '党建指导老师'
        verbose_name_plural = verbose_name

class about_us(models.Model):
    text = models.CharField(max_length = 500,verbose_name="关于我们")
    class Meta:
        verbose_name = '关于我们'
        verbose_name_plural = verbose_name

class students(models.Model):
    img = models.ImageField(upload_to='stu_img',verbose_name="学生图片")
    major_in = models.CharField(max_length = 30,verbose_name="专业")
    name = models.CharField(max_length = 30,verbose_name="姓名")
    position = models.CharField(max_length = 20,verbose_name="职位")
    class Meta:
        verbose_name = '支委'
        verbose_name_plural = verbose_name

class missions(models.Model):
    dzb_name = models.CharField(max_length=20,verbose_name="支部名称")
    mission_name = models.CharField(max_length=100,verbose_name="任务")
    missions_principle = models.CharField(max_length=20,verbose_name="负责人")
    class Meta:
        verbose_name = '负责任务'
        verbose_name_plural = verbose_name

class activity(models.Model):
    img = models.ImageField(upload_to='img,,verbose_name="组织生活照片"')
    introduce = models.CharField(max_length=100,verbose_name="组织生活介绍")
    class Meta:
        verbose_name = '组织生活'
        verbose_name_plural = verbose_name