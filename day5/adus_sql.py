#!/usr/bin/env python
# encoding: utf-8
import os

def last():
    with open("datas.txt",encoding='utf-8',mode='r') as f1:
        lines = f1.readlines()
    myline = [i for i in lines]
    lastnum = myline[-1].split(',')[0]
    lastnum = int(lastnum)
    with open("last.txt", encoding='utf-8', mode='r+') as f2:
        values = f2.read()
        values = int(values)
        if lastnum > values:
            f2.seek(0)
            f2.write(str(lastnum))
    return values,myline


def add():
    name = input("please input your name: ").strip()
    age = input("your age: ").strip()
    phone = input("your phone: ").strip()
    job = input("your job: ").strip()
    oldnum,linedata = last()
    newnum = oldnum + 1
    newdata = "\n%s,%s,%s,%s,%s" %(str(newnum),name,age,phone,job)
    with open("datas.txt", encoding='utf-8', mode='a+') as f1:
        f1.write(newdata)
    last()

#add()

def delete():
    oldnum, linedata = last()
    for i in linedata:
        print(i)

delete()

def update():
    pass

def select():
    pass


