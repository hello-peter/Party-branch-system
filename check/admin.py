from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Logfile)
class BlogTypeLogfile(admin.ModelAdmin):
    # 每页显示为10条 
    list_per_page = 10    
    # 在后台页面显示的字段
    list_display = ('id', 'file', 'file_name', 'create_time', 'host_ip', 'comment', 'isanalyse')

@admin.register(downloadsfile)
class BlogTypeLogfile(admin.ModelAdmin):
    # 每页显示为10条 
    list_per_page = 10    
    # 在后台页面显示的字段
    list_display = ('file', 'file_name', 'create_time',)

@admin.register(teacher)
class teacherdisplay(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('img','name','introduce')

@admin.register(activity)
class activitydisplay(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('img','introduce')



@admin.register(missions)
class missions_display(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('dzb_name','mission_name','missions_principle')

@admin.register(students)
class students_display(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('img','major_in','name','position')
#admin.site.register(teacher)
admin.site.register(about_us)
#admin.site.register(activity)
#admin.site.register(missions)
#admin.site.register(students)