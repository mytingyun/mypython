# coding: utf-8


class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address


class Lesson:
    def __init__(self,name,period,price,school):
        self.name = name
        self.period = period
        self.price = price
        self.school = school

    # def primary(self):
    #     print("这个是初级%s课程，%s个月的学习周期，价格为3000" %(self.name,self.period))
    # def intermediate(self):
    #     print("这个是中级%s课程，%s个月的学习周期，价格为6000" %(self.name,self.period))
    # def expert(self):
    #     print("这个是高级%s课程，%s个月的学习周期，价格为10000" %(self.name,self.period))

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
                        return nowuser
                    elif nowuser[2] == "teacher":
                        print("teacher %s login success" %name)
                        print("your grade is: ")
                        print("your lession is: ")
                        return nowuser
                    else:
                        print("Admin  %s login success\n"
                              "What are you doing:\n"
                              "1、创建讲师\n"
                              "2、创建班级\n"
                              "3、创建课程" %name)
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




class Manager:
    def __init__(self,name,passwd):
        self.name = name
        self.apasswd = passwd


    def create_school(self):
        self.school_name = input("please input school name: ").strip()
        self.school_addr = input("please input school address: ").strip()
        self.school = School(self.school_name, self.school_addr)
        return self.school

    def create_lesson(self):
        self.lesson_name = input("pls input lesson name: ").strip()
        self.lesson_period = input("pls input lesson period: ").strip()
        self.lesson_price = input("pls input lesson price: ").strip()
        self.lesson = Lesson(self.lesson_name,self.lesson_period,self.lesson_price,self.school)
        return self.lesson

    def create_grade(self,teacher):
        self.grade_name = input("pls input grade name: ").strip()
        self.grade = Grade(self.grade_name,self.school_name,self.lesson,teacher)
        return self.grade

    def create_teacher(self,lesson,grade):
        self.teacher_name = input("pls input teacher name: ").strip()
        self.tpasswd = input("pls input password: ").strip()
        self.teacher = Teacher(self.teacher_name,self.passwd,lesson,grade)
        return self.teacher

    def create_student(self,grade):
        self.student_name = input("pls input student name: ").strip()
        self.spasswd = input("pls input password: ").strip()
        self.student =Student(self.student_name,self.spasswd,grade)


login()