from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from django_ajax.decorators import ajax
# Create your views here.
import check.models as models
import os
import pandas as pd
from django.core.paginator import EmptyPage, InvalidPage, PageNotAnInteger, Paginator
from django.http import JsonResponse

class get_excel(View):
    template_name = 'excel.html'
    def get_excel(self,name,num):
        path = os.getcwd()+"/media/excel" #后去excel文件夹的绝对路径
        file_list = os.listdir(path) #获取excel文件夹下所有的文件名
        position = []
        filenames = []
        info_list = []
        final_name = []
        for index in range(len(file_list)):
            filesuffix = os.path.splitext(file_list[index])
            filenames.append(filesuffix[0])
            filesuffix = filesuffix[1]
            if filesuffix == ".xlsx" or filesuffix == ".xls": #仅支持xls和xlsx后缀的excel表格，csv不支持
                position.append(index)
        for index in position: #循环遍历所有的文件
            file_name = file_list[index]
            headname = str(filenames[index])
            file_name = "./media/excel/"+file_name
            df = pd.read_excel(file_name,encoding = 'gb18030') #读取excel表格文件中的数据
            df = df.fillna(0) #缺失值用0来填补
            info = df[(df['姓名'] == name) & (df['查询码'] == num)] #查询信息
            if info.empty == True: #判断是否查询到 
                continue
            else:
                final_name.append(headname)
                info_list.append(info)
        if len(info_list) != 0: #输出到'excel.html'当中
            result = list()
            for info,fp in zip(info_list,final_name):
                data = info.values[:,:]
                excel_data = []
                li = info.columns.tolist() 
                excel_data.append(li)
                for line in data:
                    ls = []
                    for j in line:
                        ls.append(j)
                    excel_data.append(ls)
                    context = {
                        'filename' : fp,
                        'excel_data' : excel_data
                    }
                    result.append(context)
            return result
        else:
            return 0
            
    def get(self,request):
        return render(request,'login.html')
        
    def post(self,request):
        alert = "<script type='text/javascript'>alert('信息输入有误或参数非法!');location.href = ''</script>"
        name = request.POST.get('name',None)
        num = request.POST.get('num',None)
        try:
            num = int(num)
        except:
            alert = "<script type='text/javascript'>alert('信息输入有误或参数非法!');location.href = ''</script>" #警示框
        '''
        try:
            if isinstance(type(num),str) == True:
                num = int(num)
            else:
                pass
        except:
            alert = "<script type='text/javascript'>alert('信息输入有误或参数非法!');location.href = ''</script>" #警示框
            return HttpResponse(alert)
        '''
        try:
            info = self.get_excel(name,num)
        except:
            return HttpResponse(alert)
        if info == 0:
            return HttpResponse(alert)
        else:
            return render(request,self.template_name,context = {'info' : info}) 

def open_index(request):
    teacher = models.teacher.objects.all()
    teacher = teacher[0]
    teacher_info = {
                    'img' : teacher.img,
                    'name' : teacher.name,
                    'introduce' : teacher.introduce
    }

    abouts = models.about_us.objects.all()
    about = abouts[0]
    about_text = about.text
    stud_info = list()
    assis_info = list()
    students =  models.students.objects.all()
    for i in students :
        info = {'path' : i.img,'major_in' : i.major_in,'name' : i.name,'position' : i.position}
        stud_info.append(info)
    missions_list = list()
    missions_list.append( ('支部', '主要负责任务', '负责人'))
    missions =  models.missions.objects.all()
    for i in missions:
        info = (i.dzb_name,i.mission_name,i.missions_principle)
        missions_list.append(info)
    activity = models.activity.objects.all()
    activity = activity[0]
    activity_info = {
                    'img' : activity.img,
                    'introduce' : activity.introduce
    }
    assistant_info = models.assistant.objects.all()
    for i in assistant_info:
        info = {'assis_img' : i.img,'assis_name' : i.name,'assis_major' : i.major_in}
        assis_info.append(info)
    section_info = models.section.objects.all()
    section_info_list = list()
    for i in section_info:
        section_info_list.append({'id' : i.id,'name' : i.name})
    section_info_len = len(section_info_list)
    print(section_info_len)
    return render(request,'index.html',context = {'teacher':teacher,'about_us' : about_text,'stud_info' : stud_info,
    'missions_list' : missions_list,'activity_info' : activity_info,'assis_info' : assis_info,'section_info_list' : section_info_list,'section_info_len' : section_info_len})


def open_timer(request):
    return render(request,'timer.html')

def open_front(request):
    return render(request,'front.html')


def open_test(request):
    if request.method == "GET":
        return render(request,'test.html')
    if request.method == "POST":
        text = request.POST.get('name')
        data = {
            'text': text,
        }
     
        response = JsonResponse({'status': 200,'data': data})
        return response

@ajax
def contact(request):
    if request.is_ajax():
        name = request.POST.get('name')
        num = request.POST.get('num')
        message = request.POST.get('message')
        try:
            contact_mode = models.contact_us(name = name,connect = num,comments = message)
            contact_mode.save()
            return 1
        except:
            return 1/0

def downloads_center(request):
    info = models.downloadsfile.objects.all().order_by("create_time")
   
    all_info = list()
    all = list()
    for ob in info:
        information = {'file_path' : ob.file,'file_name' : ob.file_name,'create_time' : ob.create_time}
        all_info.append(information)
    for i in range(len(all_info)):
        all.append(all_info[len(all_info) - i - 1])
    paginator = Paginator(all,20)
    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        if page == None:
            page = 1
        try:
            downloads = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            downloads = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            downloads = paginator.page(paginator.num_pages)
        p = str(page)
        template_view = 'downloads.html'
        return render(request, template_view,{'downloads': downloads})

def open_notice(reqiure):
    rcateid = reqiure.GET.get('cate')
    page = reqiure.GET.get('page')
    allcate =  models.notice_Category.objects.all()
    cateinfo = list()
    for ob in allcate:
        cateinfo.append({'id' : ob.id,'catename' : ob.name})
    
    start_id = cateinfo[0].get('id')
    try:
        notice_cate = models.notice_Category.objects.get(id = rcateid)
        notice_detail = models.notice_Article.objects.filter(category = notice_cate).order_by('-date')
        catename = notice_cate.name
    except:
        notice_cate = models.notice_Category.objects.get(id = start_id)
        notice_detail = models.notice_Article.objects.filter(category = notice_cate).order_by('-date')
        catename = notice_cate.name
    notice_details = list()
    for ob in notice_detail:
        notice_details.append({'title' : ob.title,'author' : ob.author,'date' : ob.date,'id' : ob.id})
    paginator = Paginator(notice_details,10)
    if page == None:
        page = 1
    try:
        detail_info = paginator.page(page)
    # todo: 注意捕获异常
    except PageNotAnInteger:
        # 如果请求的页数不是整数, 返回第一页。
        detail_info = paginator.page(1)
    except InvalidPage:
        # 如果请求的页数不存在, 重定向页面
        return HttpResponse('找不到页面的内容')
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        detail_info = paginator.page(paginator.num_pages)
    return render(reqiure,'notice.html' ,context = {'cateinfo' : cateinfo,'detail_info':detail_info,'cateid' : rcateid,'catename' : catename})

def open_infodetail(request):
    try:
        article_id = request.GET.get('id')
        if(article_id == None):
            article_id = models.notice_Article.objects.first().id
        notice_detail = models.notice_Article.objects.get(id = article_id)
        content = notice_detail.content
        title = notice_detail.title
        date = notice_detail.date
        author = notice_detail.author
        return render(request,'noticedetail.html' ,{'content' : content,'title' : title,'date' : date,'author' : author})
    except:
        return HttpResponse("404 Not Found")

@ajax
def infoajax(request):
    if request.is_ajax():
    
        info = request.POST.get('info')
        print(info)
        author = models.notice_Article.objects.filter(author__contains=info).order_by('-date')
        title = models.notice_Article.objects.filter(title__contains=info).order_by('-date')
        result = list()
        for l in author:
            result.append({'id' : l.id,'title' : l.title,'author' : l.author})
        for l in title:
            result.append({'id' : l.id,'title' : l.title,'author' : l.author})
        print(result)
        return result

def section_info(request):
    try:
        if request.method == 'GET':
            id = request.GET.get('id')
            sinfo = models.section.objects.get(id = id)
            info = {'title' : sinfo.name,'content' : sinfo.content}
            return render(request,'sectiondetail.html',context={'info' : info})
    except:
        return HttpResponse('404 not found')