# conding: utf-8
import os,sys

base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)
from core.mains import *


if __name__ == "__main__":
    print("请先登陆。。。")
    login()
    while True:
        if log_status["identity"] == "student":
            print("登陆成功，欢迎%s同学" % log_status["username"])
            logs.loggers.info("%s同学登陆成功" % log_status["username"])
            students = Student(log_status["username"])
            print("您可以如下操作：\n"
                  "1、查看所有课程\n"
                  "2、选择课程\n"
                  "3、查看所选课程\n"
                  "4、退出程序")
            studnum = input("请输入序号：").strip()
            if studnum == "1":
                students.get_lesson()
            elif studnum == "2":
                students.choose_lesson()
            elif studnum == "3":
                students.get_chose_lesson()
            elif studnum == "4":
                exit()
            else:
                print("您输入有误 ，请重新输入")
        if log_status["identity"] == "admin":
            print("登陆成功，欢迎管理员%s" % log_status["username"])
            admin1 = Manager(log_status["username"])
            print("您可以如下操作：\n"
                  "1、创建课程\n"
                  "2、创建学生账号\n"
                  "3、查看所有课程\n"
                  "4、查看所有学生\n"
                  "5、查看所有学生的选课情况\n"
                  "6、退出程序")
            adminnum = input("请输入序号：").strip()
            if adminnum == "1":
                admin1.create_lesson()
            elif adminnum == "2":
                admin1.create_student()
            elif adminnum == "3":
                admin1.get_all_lessons()
            elif adminnum == "4":
                admin1.get_all_student()
            elif adminnum == "5":
                studname = input("请输入学生的名字：").strip()
                admin1.get_student_lesson(studname)
            elif adminnum == "6":
                exit()
