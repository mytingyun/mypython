# conding: utf-8

import logging,os,sys
bash_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(bash_dir)

from core.mylog import loggings
from config.myconf import *
from core.auth import log_status,wrapper,login,mymd5

import configparser
config = configparser.ConfigParser()
config.read(lessonfile)


logs = loggings()
# logs.loggers.error("这是error")
# logs.loggers.info("这是info")

class Student:
    def __init__(self,name):
        self.name = name


    # @wrapper
    def get_lesson(self):
        self.lesslist = []
        logs.loggers.info("%s同学查看了所有课程" %self.name)
        for i in config.sections():
            self.lesslist.append(i)
            print("%s课程的周期为%s;\n"
                  "价格为：%s\n"
                  "老师为：%s" %(i,config[i]["period"],config[i]["price"],config[i]["teacher"]))



    #@wrapper
    def choose_lesson(self):
        self.get_lesson()
        for i in enumerate(self.lesslist):
            print(i)
        lessond = input("请输入你选择的课程的序号：").strip()
        if type(int(lessond)) == int:
            chosed = self.lesslist[int(lessond)]
            print(chosed)
            with open(choseless,mode='a',encoding='utf-8') as f2:
                f2.write("\n%s %s" %(self.name,chosed))
            logs.loggers.info("%s同学选择了%s课程" %(self.name,chosed))
        else:
            print("请输入数字。。")

    #@wrapper
    def get_chose_lesson(self):
        file1 = open(choseless,mode='r',encoding='utf-8')
        all_lesson = file1.readlines()
        # print(all_lesson)
        lesslist = []
        for less in all_lesson:
            if self.name in less:
                user1 = less.strip().split()
                lesslist.append(user1[1])
        print("%s同学所选的课程有:" %self.name)
        logs.loggers.info("%s同学查看了自己所选的课程" %self.name)
        for i in lesslist:
            print(i)


class Lesson:
    def __init__(self,name,period,price,teacher):
        self.name = name
        self.period = period
        self.price = price
        self.teacher = teacher


class Manager(Student):
    def __init__(self,name):
        self.name = name
        Student.__init__(self,name)

    # @wrapper
    def create_lesson(self):
        self.lesson_name = input("pls input lesson name: ").strip()
        self.lesson_period = input("pls input lesson period: ").strip()
        self.lesson_price = input("pls input lesson price: ").strip()
        self.teacher = input("pls input teacher name for lesson: ").strip()


    # @wrapper
    def create_student(self):
        self.student_name = input("pls input student name: ").strip()
        self.spasswd = input("pls input password: ").strip()
        md5pwd = mymd5(self.spasswd)
        self.student =Student(self.student_name)
        with open(userfile,mode='a',encoding='utf-8') as userf:
            userf.write("\n%s %s student" %(self.student_name,md5pwd))
        print("创建学生帐号成功，用户名为：%s，密码为：%s" %(self.student_name,self.spasswd))

    # @wrapper
    def get_all_lessons(self):
        stud = Student('test')
        stud.get_lesson()

    # @wrapper
    def get_all_student(self):
        with open("%s/db/user.txt" % bash_dir, encoding='utf-8', mode='r+') as file2:
            alluser = file2.readlines()
        allstudent = []
        for user in alluser:
            if 'student' in user:
                resu = user.strip().split()
                allstudent.append(resu[0])
        print("所有的学生名字如下：")
        for i in allstudent:
            print(i)

    # @wrapper
    def get_student_lesson(self,studname):
        stud2 = Student(studname)
        stud2.get_chose_lesson()


