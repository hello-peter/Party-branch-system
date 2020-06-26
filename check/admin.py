from django.contrib import admin
from .models import *
import check.adminforms as adminforms
# Register your models here.
@admin.register(contact_us)
class contact_us(admin.ModelAdmin):
    # 每页显示为10条 
    form = adminforms.content_manager
    search_fields = ('name','connect')
    list_per_page = 10    
    # 在后台页面显示的字段
    list_display = ( 'name', 'connect','comments')

@admin.register(Logfile)
class BlogTypeLogfile(admin.ModelAdmin):
    search_fields = ('file_name','comment')
    # 每页显示为10条 
    list_per_page = 10    
    # 在后台页面显示的字段
    list_display = ('file_name', 'create_time', 'host_ip', 'comment', 'isanalyse','file')

@admin.register(downloadsfile)
class BlogTypeLogfile(admin.ModelAdmin):
    search_fields = ('file_name','create_time')
    # 每页显示为10条 
    list_per_page = 10    
    # 在后台页面显示的字段
    list_display = ( 'file_name', 'create_time','file')

@admin.register(teacher)
class teacherdisplay(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name','introduce','img')

@admin.register(activity)
class activitydisplay(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('introduce','img')



@admin.register(missions)
class missions_display(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('dzb_name','mission_name','missions_principle')

@admin.register(students)
class students_display(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('major_in','name','position','img')

@admin.register(assistant)
class assistant_display(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('major_in','name','img')
#admin.site.register(teacher)
admin.site.register(about_us)
#admin.site.register(activity)
#admin.site.register(missions)
#admin.site.register(students)

@admin.register(notice_Category)
class notice_cate(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name','detail')


@admin.register(notice_Article)
class notice_cate(admin.ModelAdmin):
    search_fields = ('title','author')
    list_per_page = 10
    list_display = ('title','author','date','content','category')

@admin.register(section)
class section_admin(admin.ModelAdmin):
    search_fields = ('name','content')
    list_per_page = 10
    list_display = ('name','content')