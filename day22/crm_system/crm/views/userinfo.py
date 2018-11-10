from django.shortcuts import render,redirect
from crm import models
from crm.form.forms import UserModelForm
from crm.utils.pager import Pagination


def user_list(request):
    page = request.GET.get('page', 1)
    total_count = models.UserInfo.objects.all().count()
    pager = Pagination(page, total_count, '/crm/user/list/')
    user_queryset = models.UserInfo.objects.all()[pager.start :pager.end]

    # user_queryset = models.UserInfo.objects.all()
    return render(request,'user_list.html',{'user_queryset':user_queryset,'pager':pager})

def user_add(request):
    """
    添加用户
    :param request:
    :return:
    """
    if request.method == 'get':
        form = UserModelForm()
        return render(request, 'user_form.html', {'form':form})
    form = UserModelForm(data=request.POST)
    #对用户提交的数据进行校验
    if form.is_valid():
        print(form.data)
        form.save()
        return redirect('/crm/user/list')
    return render(request, 'user_form.html', {'form':form})

def user_edit(request,nid):
    """
    用户编辑
    :param request:
    :return:
    """
    obj = models.UserInfo.objects.filter(id=nid).first()#包含此行的所有数据
    if request.method == "GET":
        # 生成HTML标签 + 携带默认值
        form = UserModelForm(instance=obj)
        return render(request, 'user_form.html', {'form': form})
    form = UserModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crm/user/list')
    return render(request, 'user_form.html', {'form': form})


def user_del(request,nid):
    """
    删除
    :param request:
    :return:
    """
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/crm/user/list/')