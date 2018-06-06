# coding:utf-8

import json,time,sys



def key_value(key,value):
    '''
    对象值比较
    '''
    if key == value:
        return True
    else:
        return False

def diff_type(a,b):
    '''
    对象类型比较
    '''
    if type(a) == type(b):
        return True
    else:
        return False



def diff_result(data1,data2,*args):
    for key1,values1 in data1.items():
        if key1 in args[0]:
            continue
        if data1.keys() == data2.keys():
            if key1 in data2.keys():
                print("\033[1;34m%s字段对比成功,新值为%s\033[0m]" %(key1,data2.keys()))
        else:
            print("\033[1;31m字段对比失败,\n旧值为：%s,\n新值为%s\033[0m]" %(data1.keys(),data2.keys()))
        try:
            if diff_type(data1[key1],data2[key1]):
                print("\033[1;34m%s的值类型对比成功：%s和新字段的值类型%s相等\033[0m]" %(key1,type(data1[key1]),type(data2[key1])))
            else:
                print("\033[1;31m类型对比失败：旧字段%s的值类型%s和新字段的值类型%s不相等\033[0m]" %(key1,type(data1[key1]),type(data2[key1])))
        except KeyError as error:
            pass

        try:
            if isinstance(data2[key1],list):
                oldlist = data1[key1]
                newlist = data2[key1]
                #当值为列表，循环读取新旧两个列表中的元素
                for old in oldlist:
                    for new in newlist:
                        #如果列表中的元素为字典
                        if isinstance(old,dict) and isinstance(new,dict):
                            #当旧数据列表中的字典元素的索引等于新数据列表中的字典元素的索引
                            if oldlist.index(old) == newlist.index(new):
                                #通过两个索引取出相同的位置的字典，再传入递归函数
                                diff_result(oldlist[oldlist.index(old)], newlist[newlist.index(new)], *args)
            elif not isinstance(data2[key1],dict):
                if key_value(data1[key1],data2[key1]):
                    print("\033[1;34m%s的值对比成功：和新字段的值相等，是%s\033[0m]" % (key1,data2[key1]))
                else:
                    print("\033[1;31m值对比失败：旧字段%s的值和新字段的值不相等,分别是\n%s \n%s\033[0m]" % (key1,values1,data2[key1]))
        except KeyError as error:
            pass
        if isinstance(data1[key1],dict):
            diff_result(data1[key1],data2[key1],*args)



# import result_json
# #
# data1 = result_json.mydata
# data2 = result_json.data2
# ignore = ["created","modified","uuid"]
# #
# diff_result(data1,data2,ignore)

