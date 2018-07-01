# coding: utf-8
import re

def delspace(olodstr):
    '''
    去除字符中的空格
    '''
    real = olodstr.replace(" ","")
    return real

def cutstr(allstr):
    '''
    截取中间括号字段并返回
    '''
    for one in allstr:
        leftlist = []
        if one == ")":
            # 循环字符串，如果遇到右括号，就获取所在位置的索引并返回截取部分
            endright = allstr.index(one)
            newstr = allstr[:endright+1]
            content = enumerate(list(newstr))
            # 循环截取部分，如果遇到最后一个括号，就获取所在位置的索引，返回中间截取部分
            for num,left in content:
                if left == "(":
                    leftlist.append(num)
            #print(leftlist)
            return newstr[leftlist[-1]:]


def multi_division(datas,res):
    '''
    乘法和除法运算
    '''
    matchs = re.search(res,datas)
    if matchs.group():
        equa = matchs.group()
        #print("equa is--",equa)
        if "*" in equa:
            resu = equa.split("*")
            result = float(resu[0]) * float(resu[1])
            return equa,result
        if "/" in equa:
            resu = equa.split("/")
            result = float(resu[0]) / float(resu[1])
            return equa, result


def add_subtraction(datas,res):
    '''
    加法和减法运算
    '''
    matchs = re.search(res, datas)
    if matchs is None:
        return None,datas
    if matchs.group():
        equa = matchs.group()
        if "+" in equa:
            resu = equa.split("+")
            result = float(resu[0]) + float(resu[1])
            return equa, result
        if "-" in equa:
            resu = equa.split("-")
            if resu[0]:
                result = float(resu[0]) - float(resu[1])
                return equa, result
            else:
                return None,resu

def circulation_MD(datas):
    '''
    递归查找乘除法
    '''
    if "*" in datas or "/" in datas:
        res = '\d+(\.\d+)?[*/]\d+(\.\d+)?'
        matchdata,results = multi_division(datas,res)
        test2 = datas.replace(matchdata,str(results))
        #如果替换后的结果中还有乘除法，继续递归处理
        if "*" in test2 or "/" in test2:
            return circulation_MD(test2)
        else:
            return test2
    else:
        return datas

def circulation_AS(datas):
    '''
    递归查找加减法
    '''
    if "+" in datas or "-" in datas:
        res = '\d+(\.\d+)?[+-]\d+(\.\d+)?'
        matchdata, results = add_subtraction(datas,res)
        #如果加减法处理后匹配的结果不为None,就替换，否则直接返回数据，
        if matchdata:
            addsub2 = datas.replace(matchdata, str(results))
        else:
            return datas
        if "+" in datas or "-" in datas:
            if matchdata:
                #print("matchdata is: ====",matchdata)
                return circulation_AS(addsub2)
        else:
            return addsub2
    else:
        return datas

def double_addsub(datas,res):
    '''
    :计算符为+和-或为两个-号
    '''
    #print("datas is:",datas)
    matchs = re.search(res, datas)
    #print("matchs is:",matchs)
    #如果没有匹配出结果，直接返回数据
    if matchs is None:
        return None,datas
    if matchs.group():
        equa = matchs.group()
        if "+-" in equa:
            resu = equa.split("+-")
            result = float(resu[0]) - float(resu[1])
            return equa, result
        if "--" in equa:
            resu = equa.split("--")
            if resu[0]:
                result = float(resu[0]) + float(resu[1])
                return equa, result
            else:
                return None,resu

def bracket(alldata):
    '''
    递归处理所有小括号中的内容
    '''
    nospace = delspace(alldata)
    newdata = cutstr(nospace)
    #先进行乘除法运算
    resuMD = circulation_MD(newdata)
    resuMD = resuMD.strip("()")
    #再进行加减法运算
    resuAS = circulation_AS(resuMD)
    resuAS2 = resuAS.strip("()")
    #print("result is: ",resuAS2)
    newdata = nospace.replace(newdata,resuAS2)
    #print("newdata is: ",newdata)
    #如果结果中只有一个小括号，就返回
    if newdata.count('(') > 1:
        return bracket(newdata)
    else:
        return newdata

if __name__ == '__main__':
    alldata = '1 - 2 * ( (60-30 +(-40/5) * (9-10/3 + 7 /3*99/4*2998 +10 * 568/14)) - (-4*3)/ (16-3*2) )'
    #去除空格
    enddata = bracket(alldata)
    #返回最后一个小括号：1-2*(30.0+-1388367.0476190478--12.0/10.0)
    data = cutstr(enddata)
    #先用乘除法运算
    resuMD = circulation_MD(data)
    resuMD = resuMD.strip("()")
    #乘法运算后返回结果，再用+-相连的符号运逄
    res = '\d+(\.\d+)?[+-][+-]\d+(\.\d+)?'
    newdata = double_addsub(resuMD, res)
    olddata = resuMD.replace(newdata[0], str(newdata[1]))
    #print("@@@",olddata)
    res2 = '[+-]\d+(\.\d+)?[+-][+-]\d+(\.\d+)?'
    newdata = double_addsub(olddata, res2)
    newdata = olddata.replace(newdata[0], str(newdata[1]))
    nowdata = enddata.replace(data,newdata)
    #最后一个小括号计算结果完成并替换，返回最后算式，匹配乘号后面的负数
    res3 = '\d+(\.\d+)?[*/]-\d+(\.\d+)?'
    single,resutmp = multi_division(nowdata,res3)
    nowdata2 = nowdata.replace(single,str(resutmp))
    #乘法运算结果并替换后返回最后一个双负号算式，匹配双负号，负负得正最后计算结果
    res4 = '\d+(\.\d+)?[+-][+-]\d+(\.\d+)?'
    end,result = double_addsub(nowdata2, res4)
    print("result is: ",result)









