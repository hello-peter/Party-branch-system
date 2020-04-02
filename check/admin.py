from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Logfile)
class BlogTypeLogfile(admin.ModelAdmin):
    # 每页显示为10条 
    list_per_page = 10    
    # 在后台页面显示的字段
    list_display = ('id', 'file', 'file_name', 'create_time', 'host_ip', 'comment', 'isanalyse')