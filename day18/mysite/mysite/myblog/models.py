# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Myuser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16,null=False,unique=True)
    passwd = models.CharField(max_length=32,null=False)