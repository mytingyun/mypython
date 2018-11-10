from django.conf.urls import url,include
from django.contrib import admin
from crm.views import home
from crm.views import depart
from crm.views import userinfo
from crm.views import courses
from crm.views import classes


urlpatterns = [
    url(r'^index/$', home.index),
    url(r'^depart/list/$', depart.depart_list),
    url(r'^depart/add/$', depart.depart_add),
    url(r'^depart/edit/(\d+)/$', depart.depart_edit),
    url(r'^depart/del/(\d+)/$', depart.depart_del),
    url(r'^user/list/$', userinfo.user_list),
    url(r'^user/add/$', userinfo.user_add),
    url(r'^user/edit/(\d+)/$', userinfo.user_edit),
    url(r'^user/del/(\d+)/$', userinfo.user_del),
    url(r'^login/$', home.login),
    url(r'^course/list/$', courses.course_list),
    url(r'^course/add/$', courses.course_add),
    url(r'^course/edit/(\d+)/$', courses.course_edit),
    url(r'^course/del/(\d+)/$', courses.course_del),
    url(r'^classes/list/$', classes.classes_list),
    url(r'^classes/add/$', classes.classes_add),
    url(r'^classes/edit/(\d+)/$', classes.classes_edit),
    url(r'^classes/del/(\d+)/$', classes.classes_del),
]
