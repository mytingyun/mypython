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
            f2.write(lastnum)
    return values

print(last())

def add():
    name = input("please input your name: ")
    age = input("your age: ")
    phone = input("your phone: ")
    job = input("your job: ")

    pass

def delete():
    pass

def update():
    pass

def select():
    pass


