# coding: utf-8
import random
#https://www.cnblogs.com/Eva-J/articles/9235899.html

def baks(num,money):
    rednum = [i for i in range(money)]
    myrandom = []
    for i in range(num-1):
        nums = random.choice(rednum)
        rednum.remove(nums)
        myrandom.append(nums)
    myrandom.sort()

    if myrandom[0] != 0:
        myrandom.insert(0,0)
    if myrandom[-1] != money:
        myrandom.append(money)

    smallbak = []
    while num > 0:
        smallbak.append(myrandom[num] - myrandom[num-1])
        num -= 1
    print(smallbak)

baks(30,200)


