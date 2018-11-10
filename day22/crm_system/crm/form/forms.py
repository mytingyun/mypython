from crm import models
from django import forms
from django.forms import ModelForm


class DepartModelForm(ModelForm):
    class Meta:
        model = models.Department
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'部门名称'})
        }
        error_message = {
            'title':{
                'required':'部门名称不能为空'
            }
        }

class CourseModelForm(ModelForm):
    class Meta:
        model = models.Course
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'课程名'})
        }
        error_message = {
            'title': {
                'required': '课程名称不能为空'
            }
        }

class ClassesModelForm(ModelForm):
    class Meta:
        model = models.ClassList
        fields = "__all__"
        widgets = {
            'course': forms.Select(attrs={'class':'form-control','placeholder':'课程'}),
            'num': forms.TextInput(attrs={'class':'form-control','placeholder':'期数'}),
            #ManyToManyField 多对多的情况，此处要用SelectMultiple
            'teachers': forms.SelectMultiple(attrs={'class':'form-control','placeholder':'老师'})
        }
        error_message = {
            'course': {
                'required': '课程名不能为空'
            },
            'num': {
                'required': '期数不能为空'
            },
            'teachers': {
                'required': '老师不能为空'
            }
        }


class UserModelForm(ModelForm):
    class Meta:
        model = models.UserInfo
        fields = "__all__"
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'用户名'}),
            'password': forms.TextInput(attrs={'class':'form-control','placeholder':'密码'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'邮箱'}),
            'gender': forms.Select(attrs={'class':'form-control','placeholder':'姓别'}),
            'depart': forms.Select(attrs={'class':'form-control','placeholder':'部门'})

        }
        error_message = {
            'username':{
                'required':'用户名不能为空'
            },
            'password': {
                'required': '密码不能为空'
            },
            'email': {
                'required': '邮箱不能为空'
            },
            'gender': {
                'required': '性别不能为空'
            },
            'depart': {
                'required': '所属部门不能为空'
            }
        }



