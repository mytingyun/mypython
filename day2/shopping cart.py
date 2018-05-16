# /usr/bin/env python
#coding:utf8
#商品列表
commodity = {"pen":25,"coat":340,"umbrella":30,"keyboard":120,"shoes":230}
money = input("please input your money: ")
print "please select  serial number of the commodity: "
print "the commodity name and pric is: "
#定义空字典存放选择的商品数量和价格
result = {}
while True:
    #打印商品价格列表
    waitselect = []
    num0 = 0
    for name,price in commodity.items():
        print "{%d}  %s: %d" %(num0,name,price)
        waitselect.append(name)
        num0+=1
    num = raw_input("please input commodity number or 'q' to settle accounts: ")
    totalprices = 0
    #输入q去结算
    if num == 'q':
        break
    else:
        num = int(num)
        #如果输入超出列表序列，打印无此商品
        if num >= len(waitselect):
            print "you select commodity is not exist, please retry..."
            continue
        count = input("please input buy quantity: ")
        #根据输入的序号定位商品名称
        seledted = waitselect[num]
        #将商品名称和选择的数量与价格存入字典
        result[seledted] = [count, commodity[seledted] * count]
        for name, nums in result.items():
            totalprices += nums[1]
        #如果所选商品总价大于资产总额，退出程序，购买失败
        if totalprices > money:
            print "Total amount of goods is: ",totalprices
            print "your money is %s, Lack of balance, purchase failed" % money
            exit()
    #打印所选商品的总额
    print "Total amount of goods is: ",totalprices
    amount = totalprices
#打印购物列表和商品总价
print "This is you selected commodity bills: "
print '{:<10}'.format('Commodity'),'{:^20}'.format('Numbers'),'{:>10}'.format('Price')
for name,num2 in result.items():
    print '{:<10}'.format(name),'{:^20}'.format(num2[0]),'{:>10}'.format(num2[1])
print "Total amount of goods is: ",amount