#coding: utf-8
import logging
import os,sys

bash_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(bash_dir)

class loggings:

    loggers = logging.getLogger()
    screen = logging.StreamHandler()
    filemange = logging.FileHandler('%s/log/loging.txt' %bash_dir,encoding='utf-8')
    fomatter = logging.Formatter('%(asctime)s - %(name)s -[line:%(lineno)d]- %(levelname)s - %(message)s')

    screen.setFormatter(fomatter)
    filemange.setFormatter(fomatter)
    screen.setLevel(logging.ERROR)
    filemange.setLevel(logging.INFO)

    loggers.addHandler(filemange)
    loggers.addHandler(screen)
    loggers.setLevel(logging.DEBUG)








