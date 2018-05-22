#!/usr/bin/env python
# -*- coding:utf-8 -*-


def test1(*args,**kwargs):
    print(args)
    print(kwargs)

#test1("wang",23,[33,"liu"])
#test1("wang",23,*[33,"liu"])

#test1("wang",23,[33,"liu"],*("your","are",88))

test1("wang",23,[33,"liu"],*("your","are",88),cote=64,open="90",watch=100)
#test1("wang",23,[33,"liu"],*("your","are",88),**{"cote":64,"open":"90","watch":100})