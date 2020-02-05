from django.shortcuts import render,HttpResponse
from django.views.generic import View
# Create your views here.
import os
import pandas as pd

class get_excel(View):
    template_name = 'excel.html'
    def get_excel(self,name,num):
        path = os.getcwd()+"/check/excel"
        file_list = os.listdir(path)
        position = []
        for index in range(len(file_list)):
            filesuffix = os.path.splitext(file_list[index])
            filesuffix = filesuffix[1]
            if filesuffix == ".xlsx" or filesuffix == ".xls":
                position.append(index)
        for index in position:
            file_name = file_list[index]
            file_name = "./check/excel/"+file_name
            df = pd.read_excel(file_name,encoding = 'gb18030')
            df = df.fillna(0)
            info = df[(df['姓名'] == name) & (df['学号'] == num)]
            if info.empty == False:
                break
        if info.empty == True:
            return 0
        else:
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
                    'excel_data' : excel_data,
                }
                return context
            
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        name = request.POST.get('name',None)
        num = request.POST.get('num',None)
        try:
            if isinstance(type(num),str) == True:
                num = int(num)
            else:
                pass
        except:
            print('1')
            alert = "<script type='text/javascript'>alert('信息输入有误或参数非法!');location.href = ''</script>"
            return HttpResponse(alert)
        info = self.get_excel(name,num)
        if info == 0:
            alert = "<script type='text/javascript'>alert('信息输入有误或参数非法!');location.href = ''</script>"
            return HttpResponse(alert)
        else:
            return render(request,self.template_name,context = info) 