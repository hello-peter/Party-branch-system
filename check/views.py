from django.shortcuts import render,HttpResponse
from django.views.generic import View
# Create your views here.
import check.models as models
import os
import pandas as pd

class get_excel(View):
    template_name = 'excel.html'
    def get_excel(self,name,num):
        path = os.getcwd()+"/check/excel" #后去excel文件夹的绝对路径
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
            file_name = "./check/excel/"+file_name
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
    return render(request,'index.html',context = {'teacher':teacher,'about_us' : about_text,'stud_info' : stud_info,'missions_list' : missions_list,'activity_info' : activity_info})


def open_timer(request):
    return render(request,'timer.html')

