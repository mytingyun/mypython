from django.shortcuts import render,redirect
from crm import models
from crm.form.forms import DepartModelForm
from crm.utils.pager import Pagination



def depart_list(request):
    page = request.GET.get('page', 1)
    total_count = models.Department.objects.all().count()

    pager = Pagination(page, total_count, '/crm/depart/list/')
    depart_queryset = models.Department.objects.all()[pager.start:pager.end]
    # depart_queryset = models.Department.objects.all()
    return render(request,'depart_list.html',{'depart_queryset':depart_queryset,'pager':pager})

def depart_add(request):
    """
    添加部门
    :param request:
    :return:
    """
    if request.method == 'get':
        form = DepartModelForm()
        return render(request, 'depart_form.html', {'form':form})
    form = DepartModelForm(data=request.POST)
    #对用户提交的数据进行校验
    if form.is_valid():
        form.save()
        return redirect('/crm/depart/list')
    return render(request, 'depart_form.html', {'form':form})

def depart_edit(request,nid):
    """
    编辑部门名称
    :param request:
    :param nid:
    :return:
    """
    obj = models.Department.objects.filter(id=nid).first() #包含此行的所有数据
    if request.method == "GET":
        #生成HTML标签 + 携带默认值
        form = DepartModelForm(instance=obj)
        return render(request,'depart_form.html',{'form':form})
    form = DepartModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crm/depart/list')
    return render(request,'depart_form.html',{'form':form})

def depart_del(request,nid):
    """
    删除
    :param request:
    :param nid:
    :return:
    """
    models.Department.objects.filter(id=nid).delete()
    return redirect('/crm/depart/list/')