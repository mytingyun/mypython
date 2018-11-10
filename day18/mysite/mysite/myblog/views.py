# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myblog import models
from django.shortcuts import render

# Create your views here.


def index(request):
    users = models.Myuser.objects.create(name='wang',passwd='123456')
    return render(request, 'index.html',{"users":users})