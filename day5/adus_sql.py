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
    orderlist = []
    datas = []
    oldnum, linedata = last()
    for i in linedata:
        order = i.strip().replace('，',',').split(',')[0]
        line = i.strip().replace('，', ',').split(',')
        if line[0]:
            datas.append(line)
        if order.isdigit():
            orderlist.append(order)
    for i in datas:
        print(i)
    while True:
        delnum = input("please input need delete num: ").strip()
        if not delnum.isdigit():
            continue
        elif delnum not in orderlist:
            continue
        else:
            for i in datas:
                if delnum == i[0]:
                    print(delnum,"line delete success")
                    del(datas[datas.index(i)])
                    break
            break
    with open('datas2.txt',encoding='utf-8',mode='w') as f2:
        for i in datas:
            new = ','.join(i)
            f2.write(new+'\n')
    os.remove('datas.txt')
    os.rename('datas2.txt','datas.txt')


def update():
    print("this is updata")
    pass

def select():
    while True:
        choise = input("please your select sql: ").strip()
        #print(choise)
        conduction = [">", "<", "=","like"]
        if "where" not in choise:
            print("your input error,please retry..")
            continue
        else:
            sql = choise.split("where")
            #print(sql)
            diff = None
            for i in conduction:
                if i in sql[1]:
                    diff = i
                    #print("diff is: ", diff)
            if diff == None:
                print("Input need have %s,please retry.." %conduction)
                continue

            oldnum, linedata = last()
            all = []
            for i in linedata:
                line = i.strip().replace('，', ',').split(',')
                if line[0]:
                    all.append(line)
            field = all[0]
            #print("所有字段是：",field)
            if '*' in sql[0]:
                #带*的显示所有列
                #用比较符将where后的字段分开赋给data
                data = sql[1].split(diff)
                #values是需要过滤出来的内容
                values = data[1].strip()
                #根据data[0]在首行字段列表中的位置定位出索引
                myindex = field.index(data[0].strip())
                del(all[0])
                # 利用myindex索引循环找出符合上面values条件的行
                for lists in all:
                    if diff is "=":
                        if lists[myindex] == values:
                            print(lists)
                    elif diff is "like":
                        if values in lists[myindex].strip():
                            print(lists)
                    elif diff is ">":
                        if lists[myindex] > values:
                            print(lists)
                    else:
                        if lists[myindex] < values:
                            print(lists)
            else:
                #不带*, 只显示指定列
                rank = sql[0].replace(','," ").strip().split()
                del(rank[0])
                #rank为需要取的多个字段名
                for i in rank:
                    if i not in field:
                        print("you input %s is not exist, please retry..." %i)
                        continue
                #用nowindex列表收集各字段在每行中的索引
                nowindex = []
                for i in rank:
                    nowindex.append(field.index(i))
                #字义收集所有新数据的列表
                newall = []
                del (all[0])
                for list2 in all:
                    #定义收集每一行的列表
                    newline = []
                    for i in nowindex:
                        #循环索引收集每需要的字段为新行到列表
                        newline.append(list2[i])
                    #收集每一行
                    newall.append(newline)
                #print(newall)

                #以下代码同上面带*号的代码
                data = sql[1].split(diff)
                values = data[1].strip()
                myindex = field.index(data[0].strip())
                for lists1 in all:
                    for lists2 in newall:
                        if diff is "=":
                            if lists1[myindex] == values:
                                print(lists2)
                        elif diff is "like":
                            if values in lists1[myindex].strip():
                                print(lists2)
                        elif diff is ">":
                            if lists1[myindex] > values:
                                print(lists2)
                        else:
                            if lists1[myindex] < values:
                                print(lists2)



#delete()
#select()


funcs= {1: add, 2: delete, 3: update, 4: select, 5: exit}

while True:
    print("欢迎使用: \n"
          "1、增加个人资料\n"
          "2、删除个人资料\n"
          "3、更新个人资料\n"
          "4、查询个人资料\n"
          "5、退出\n")
    selectnum = input("please select number: ").strip()
    try:
        select = int(selectnum)
        if 0 < select <= len(funcs):
            funcs[select]()
            exit()
    except ValueError as err:
        print("您输入有误，请输入1-5的数字")