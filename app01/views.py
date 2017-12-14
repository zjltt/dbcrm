from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from app01 import models
import json
from django.forms import Form
from django.forms import fields
from django.forms import widgets
# Create your views here.
#生成一个类继承View
class LoginView(View):
    '''
    get是从服务器上获取数据，post是向服务器传送数据。
    '''
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")
    def post(self,request,*args,**kwargs):
        username=request.POST.get("username")
        password=request.POST.get("pwd")
        cnt=models.UserInfo.objects.filter(username=username,pwd=password).count()
        #定义个字典
        ret={'status':True,"error":None}
        if cnt:
            request.session["username"]=username
            request.session["passwrod"]=password
            return HttpResponse(json.dumps(ret)) ##json.dumps : dict转成str json.loads:str转成dict
        else:
            ret["status"]=False
            ret["error"]="用户名或者密码错误"
            return HttpResponse(json.dumps(ret))

# class AuthView(object):
#     def dispatch(self, request, *args, **kwargs):
#         if request.session.get('username'):
#             response = super(AuthView,self).dispatch(request, *args, **kwargs)
#             return response
#         else:
#             return redirect('/login/')

#注册用户 设置RegisterForm继承Form类
class RegisterForm(Form):
    username=fields.CharField(
        required=True, #是否允许为空
        min_length=2, #最小长度
        max_length=18,#最大长度
        error_messages={'required':'用户名不能为空','invalid':'用户名格式错误'}, #错误信息 {'required': '不能为空', 'invalid': '格式错误'}
        widget=widgets.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名'}) #HTML插件
    )
    pwd=fields.CharField(
        required=True,
        min_length=2,
        max_length=18,
        error_messages={'required': '密码不能为空', 'invalid': '密码格式错误'},
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'})
    )
    email=fields.CharField(
        min_length=2,
        error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'},
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'})
    )
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        #通过render返回一个form对象
        return render(request,'register.html',{'form':form})
    else:
        response = {'status':True,'data':None,'msg':None}
        form = RegisterForm(request.POST)
        if form.is_valid():
            # print('用户前端界面输入的数据是:')
            # #下面这行代码需要继续优化
            # print(form.cleaned_data)
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            email = form.cleaned_data['email']
            models.UserInfo.objects.create(username=username,pwd=pwd,email=email,ut_id=1)
            print(username,pwd,email)
        else:
            print(form.errors)
            response['status'] = False
            response['msg'] = form.errors
        return HttpResponse(json.dumps(response))

from utils.page import PageInfo
class HostsView(View):
    def get(self,request,*args,**kwargs):
        all_count=models.HostInfo.objects.all().count()
        # 设置显示6页
        page_info=PageInfo(request.GET.get("p"),6,all_count,request.path_info)
        all_host_list = models.HostInfo.objects.all()[page_info.start():page_info.end()]
        all_bus_list = models.BusinessInfo.objects.all()
        return render(request,'hosts.html',{'all_host_list':all_host_list,
                                            "page_info":page_info,
                                            'all_bus_list':all_bus_list})

