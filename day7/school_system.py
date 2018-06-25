# coding: utf-8


class school:
    def __init__(self,address):
        self.address = address


class lesson:
    def __init__(self,name,period):
        self.name = name
        self.period = period

    def primary(self):
        print("这个是初级%s课程，%s个月的学习周期，价格为3000" %(self.name,self.period))
    def intermediate(self):
        print("这个是中级%s课程，%s个月的学习周期，价格为6000" %(self.name,self.period))
    def expert(self):
        print("这个是高级%s课程，%s个月的学习周期，价格为10000" %(self.name,self.period))

class student:


