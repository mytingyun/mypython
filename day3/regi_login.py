#!/usr/bin/env python
# encoding: utf-8
global session
session = 0
def register():
    file1 = open('username.txt',encoding='utf-8',mode='a+')
    file1.seek(0)
    nowuser = file1.read()
    #print('now user is:', nowuser)
    while True:
        user = input("please input your name: ").strip()
        passwd1 = input("please input your passwd: ").strip()
        passwd2 = input("please again input your passwd: ").strip()
        if user in nowuser:
            print("your name is exist, please again input...")
            continue
        elif passwd1 != passwd2:
            print("you input twice password different, please again again input...")
            continue
        else:
            file1.write('\n%s  %s' %(user, passwd1))
            break
    return "%s user register success, please login..." %user


def login(name):
    with open("username.txt",encoding='utf-8',mode='r+') as file2:
        alluser = file2.readlines()
    index = 0
    pwd = 0
    for user in alluser:
        if name in user:
            reault = alluser[index]
            nowuser = reault.strip().split()
            #print("nowuser is: ",nowuser)
            while True:
                passwd = input("please input your password: ").strip()
                if passwd == nowuser[1]:
                    print("login success")
                    session = 'success'
                    return session
                else:
                    pwd+=1
                    print("your passwd is error, please retry...")
                    if pwd == 3:
                        print("your input password error thrice, your account locked")
                        exit()
                    continue
        if index == len(alluser)-1:
            print("your name is not exist,please register")
            break
        index += 1

def shopping():
    #商品列表
    commodity = {"pen":25,"coat":340,"umbrella":30,"keyboard":120,"shoes":230}
    money = input("please input your money: ").strip()
    money = int(money)
    print("please select  serial number of the commodity: ")
    print("the commodity name and pric is: ")
    #定义空字典存放选择的商品数量和价格
    result = {}
    while True:
        #打印商品价格列表
        waitselect = []
        num0 = 0
        for name,price in commodity.items():
            print("{%d}  %s: %d" %(num0,name,price))
            waitselect.append(name)
            num0+=1
        num = input("please input commodity number or 'q' to settle accounts: ").strip()
        totalprices = 0
        #输入q去结算
        if str(num) == 'q':
            break
        else:
            num = int(num)
            #如果输入超出列表序列，打印无此商品
            if num >= len(waitselect):
                print("you select commodity is not exist, please retry...")
                continue
            count = input("please input buy quantity: ").strip()
            count = int(count)
            #根据输入的序号定位商品名称
            seledted = waitselect[num]
            #将商品名称和选择的数量与价格存入字典
            result[seledted] = [count, commodity[seledted] * count]
            for name, nums in result.items():
                totalprices += int(nums[1])
            #如果所选商品总价大于资产总额，退出程序，购买失败
            if totalprices > money:
                print("Total amount of goods is: ",totalprices)
                print("your money is %d, Lack of balance, purchase failed" % money)
                exit()
        #打印所选商品的总额
        print("Total amount of goods is: %s" %totalprices)
        amount = totalprices
    #打印购物列表和商品总价
    print("This is you selected commodity bills: ")
    print('{:<10}'.format('Commodity'),'{:^20}'.format('Numbers'),'{:>10}'.format('Price'))
    for name,num2 in result.items():
        print('{:<10}'.format(name),'{:^20}'.format(num2[0]),'{:>10}'.format(num2[1]))
    print("Total amount of goods is: ",amount)
    exit()


while True:
    print("what are you doing: \n"
          "1、登陆\n"
          "2、注册\n"
          "3、退出")
    do = input("please select number: ").strip()
    do = int(do)
    if do == 1:
        name = input("please input your name for login: ").strip()
        set = login(name)
        if set == 'success':
            print("1、购物\n"
                  "2、返回上级菜单")
            select = input("please select number: ").strip()
            if int(select) == 1:
                shopping()
            elif select == 2:
                exit()
    elif do == 2:
        status = register()
        print(status)
    elif do == 3:
        exit()
    else:
        print("input error, please reatry...")


