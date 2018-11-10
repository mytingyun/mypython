from django.shortcuts import render,redirect
from crm import models
from crm.form.forms import ClassesModelForm

def classes_list(request):

    class_queryset = models.ClassList.objects.all()
    return render(request,'class_list.html',{'class_queryset':class_queryset})


def classes_add(request):
    """
    课程添加
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = ClassesModelForm()
        return render(request,'class_form.html',{"form":form})

    form = ClassesModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/crm/classes/list')
    return render(request,'class_form.html',{'form':form})

def classes_edit(request,nid):
    """
    编辑课程
    :param request:
    :return:
    """
    obj = models.ClassList.objects.filter(id=nid).first()  # 包含此行的所有数据
    if request.method == "GET":
        # 生成HTML标签 + 携带默认值
        form = ClassesModelForm(instance=obj)
        return render(request, 'class_form.html', {'form': form})
    form = ClassesModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crm/classes/list')
    return render(request, 'class_form.html', {'form': form})

def classes_del(request,nid):
    """
    删除课程
    :param request:
    :param nid:
    :return:
    """
    models.ClassList.objects.filter(id=nid).delete()
    return redirect('/crm/classes/list/')