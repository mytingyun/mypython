# coding: utf-8


class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address


class Lesson:
    def __init__(self,name,period,school):
        self.name = name
        self.period = period
        self.school = school

    def primary(self):
        print("这个是初级%s课程，%s个月的学习周期，价格为3000" %(self.name,self.period))
    def intermediate(self):
        print("这个是中级%s课程，%s个月的学习周期，价格为6000" %(self.name,self.period))
    def expert(self):
        print("这个是高级%s课程，%s个月的学习周期，价格为10000" %(self.name,self.period))

class Grade:
    def __init__(self,name,school,lesson,teacher):
        self.name = name
        self.school = school
        self.lesson = lesson
        self.teacher = teacher


class Student:
    def __init__(self,name,passwd,grade):
        self.name = name
        self.passwd = passwd
        self.grade = grade

class Teacher:
    def __init__(self,name,passwd,lesson,grade):
        self.name = name
        self.passwd = passwd
        self.lesson = lesson
        self.grade = grade

class Admin:
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd

def login():
    name = input("please input your name: ").strip()
    with open("username.txt",encoding='utf-8',mode='r+') as file2:
        alluser = file2.readlines()
    stu_index = 0
    pwd = 0
    for user in alluser:
        if name in user:
            reault = alluser[stu_index]
            nowuser = reault.strip().split()
            print("nowuser is: ",nowuser)
            while True:
                passwd = input("please input your password: ").strip()
                if passwd == nowuser[1]:
                    if nowuser[2] == "student":
                        print("student %s login success" %name)
                        print("your grade is: ")
                        print("your lession is: ")
                    elif nowuser[2] == "teacher":
                        print("student %s login success" %name)
                        print("your grade is: ")
                        print("your lession is: ")
                    else:
                        print("Admin  %s login success\n"
                              "What are you doing:\n"
                              "1、创建讲师\n"
                              "2、创建班级\n"
                              "3、创建课程" %name)
                    break

                else:
                    pwd+=1
                    print("your passwd is error, please retry...")
                    if pwd == 3:
                        print("your input password error thrice, your account locked")
                        exit()
                    continue

        if stu_index == len(alluser)-1:
            print("your name is not exist,please contact admin")
            break
        stu_index += 1

login()


