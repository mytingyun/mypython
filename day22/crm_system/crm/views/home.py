from django.shortcuts import render
from crm.form.forms import UserModelForm
from crm import models
from django.contrib import auth
import random

cookies = random.random()
def index(request):
    ret = render(request,'index.html')
    ret.set_cookie(key='mycookie', value=None)
    return ret


def login(request):
    static = None
    if request.method == 'get':
        form = UserModelForm()
        return render(request, 'login.html', {'form': form})
    form = UserModelForm(data=request.POST)
    if request.method == "POST":
        user = request.POST.get('username')
        passwd = request.POST.get('password')
        res_user = models.UserInfo.objects.filter(username=user).exists()
        realy_pwd = models.UserInfo.objects.filter(username=user).values('password').get()['password']

        if res_user and passwd == realy_pwd:
            static = '登录成功'
            rep = render(request, 'index.html',{'static':static})
            rep.set_cookie(key='mycookie', value=cookies)
            return rep
        else:
            rep = render(request, 'login.html', {'form': form})
            rep.set_cookie(key='mycookie', value=None)
            return rep
    return render(request,'login.html',{'form': form})




