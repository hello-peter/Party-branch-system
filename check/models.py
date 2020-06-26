from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField

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

class assistant(models.Model):
    img = models.ImageField(upload_to='assis_img',verbose_name="学生图片")
    major_in = models.CharField(max_length = 30,verbose_name="专业")
    name = models.CharField(max_length = 30,verbose_name="姓名")
    class Meta:
        verbose_name = '党建服务小组'
        verbose_name_plural = verbose_name

class contact_us(models.Model):
    name = models.CharField(u'留言者名字', max_length=50, default='name', null=False)
    connect = models.CharField(u'邮箱/电话', max_length=50,default='tel/e-mail', null=False)
    comments = models.CharField(u'留言内容', max_length=500,default='contents', null=False)
    class Meta:
        verbose_name = '与我们联系'
        verbose_name_plural = verbose_name

#公告数据
class notice_Category(models.Model):
    name = models.CharField(u'分类名',max_length=10,default='党建分类')
    detail = models.CharField(u'详细描述',max_length = 100,default = '党建分类具体描述')
    def name_level(self):
       	return self.grade.name.name
    name_level.admin_order_field = 'grade__level__name'
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '信息公开分类'
        verbose_name_plural = verbose_name


#显示具体文章
class notice_Article(models.Model):
    title = models.CharField(u'文章标题',default = '标题',max_length=100)
    author = models.CharField(u'发布人',default='学生第三支部支委',null=False,max_length = 10)
    date = models.DateTimeField(u'发布时间', null=False)
    content = RichTextUploadingField(u'发布内容')
    # 是由Category影响Article
    category = models.ForeignKey('notice_Category',on_delete=models.CASCADE)
    class Meta:
        verbose_name = '信息公开'
        verbose_name_plural = verbose_name

#下属部门
class section(models.Model):
    name = models.CharField(u'部门名称',default = '名称',max_length=100)
    content = RichTextUploadingField(u'详细介绍')

    
    class Meta:
        verbose_name = '下属部门'
        verbose_name_plural = verbose_name