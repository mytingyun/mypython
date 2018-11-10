from django.shortcuts import render,redirect
from crm import models
from crm.form.forms import CourseModelForm


def course_list(request):

    course_queryset = models.Course.objects.all()
    return render(request,'course_list.html',{'course_queryset':course_queryset})


def course_add(request):
    """
    增加课程
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = CourseModelForm()
        return render(request,'course_form.html',{"form":form})

    form = CourseModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/crm/course/list')
    return render(request,'course_form.html',{'form':form})

def course_edit(request,nid):
    """
    编译课程
    :param request:
    :return:
    """
    obj = models.UserInfo.objects.filter(id=nid).first()  # 包含此行的所有数据
    if request.method == "GET":
        # 生成HTML标签 + 携带默认值
        form = CourseModelForm(instance=obj)
        return render(request, 'course_form.html', {'form': form})
    form = CourseModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crm/course/list')
    return render(request, 'course_form.html', {'form': form})

def course_del(request,nid):
    """
    删除课程
    :param request:
    :param nid:
    :return:
    """
    models.Course.objects.filter(id=nid).delete()
    return redirect('/crm/course/list/')