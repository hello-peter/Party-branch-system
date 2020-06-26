"""dzb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import static
from dzb import settings
from django.conf.urls import include, url
from rest_framework.documentation import include_docs_urls

import sys
sys.path.append('../check')
from check import views as cv
urlpatterns = [
    path('admin/', admin.site.urls),
    path('query/',cv.get_excel.as_view(),name = 'query'),
    path('',cv.open_index,name = 'index'),
    path('timer/',cv.open_timer ,name = 'timer'),
    path('downloads/',cv.downloads_center,name = 'downloads'),
    path('front/',cv.open_front),
    path('test/',cv.open_test,name = 'test'),
    path('info/',cv.open_notice,name = 'info'),
    path('infodetail/',cv.open_infodetail,name = 'info_detail'),
    path('sectioninfo/',cv.section_info,name = 'section_info'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url('^contact$',cv.contact,name = 'contact'),
    url(r'^infoajax/',cv.infoajax,name = 'infoajax')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)