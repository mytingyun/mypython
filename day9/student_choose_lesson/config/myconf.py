# coding: utf-8
import os,sys


bash_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(bash_dir)

userfile = '%s/db/user.txt' %bash_dir
lessonfile = '%s/db/lesson.txt' %bash_dir
choseless = '%s/db/chose_lesson.txt' %bash_dir
