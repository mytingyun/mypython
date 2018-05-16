# /usr/bin/env python
#coding:utf8


commodity = {"pen":25,"coat":340,"umbrella":30,"keyboard":120}

print "please select  serial number of the commodity: "
print "the commodity name and pric is: "

waitselect = []
num = 0
for name,price in commodity.items():
    print "%d, %s: %d" %(num,name,price)
    waitselect.append(name)
    num+=1

result = {}
while True:
    num = raw_input("please input commodity number or 'q' to exit: ")
    if num == 'q' or num == None:
        break
    else:
        num = int(num)
        if num >= len(waitselect):
            print "you select commodity is not exist, please retry..."
            continue
        print "Your select commodity is: %s" % waitselect[num]
        count = input("please input buy quantity: ")
        result[waitselect[num]] = [count,commodity[waitselect[num]] * count]


print "result is:",result
print "This is you selected commodity bills: "
print '{:<10}'.format('Commodity'),'{:^20}'.format('Numbers'),'{:>10}'.format('Price')
totalprices=0
for name,num in result.items():
    print '{:<10}'.format(name),'{:^20}'.format(num[0]),'{:>10}'.format(num[1])
    totalprices+=num[1]

print "All commodity the total price is: ", totalprices