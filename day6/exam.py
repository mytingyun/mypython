一，选择题（每题2分，共30分）
1、以下说法正确的是：

A、Python中str的单引号与双引号有区别

B、python3x版本默认编码方式为unicode。
C、Python设置变量可以为and。

D、Python3x版本中的input输入的字符串类型。

答案选D
2、此代码的运行结果为：

while flag:
    print(1)
    print(2)
    flag = False
    print(4)
A、1
2
B、1
2
1
2.....C、1
2
4
D、1
2
4
1
2
4........

答案选C

3、下面代码的结果为：
name = ‘alex’
a = ‘3’
print(name * a)
A、alexalexalex
B、 alex3
C、3
alex
D、TypeError

答案选D

4、以下说法错误的是：

A、ASCII码只包含数字，字母，特殊字符。

B、unicode有两个版本，第一个版本是一个字符用两个字节表示，第二个版本是一个字符用四个字节表示。
C、utf - 8
中，一个字节用三个字符表示。

D、gbk只包含英文，数字，特殊字符，和中文。

答案选C

5、计算一下这个不等式的结果：
1 > 2 and 3 or 6
A、True
B.
False
C.
3
D
.6

答案选D

6、‘老男孩’用utf - 8
编码需要几个字节表示？
A、3
B、6
C、9
D、12

答案选C

7、在Python3x中：a = b‘alex’，如何将a转化成 ‘alex’？
A、a.encode(‘utf - 8’)  B、a.decode()
C、bytes(a)
D、str（a）

答案选B

8、count在内存中最终等于：

count = 1
while count < 9:
    print(count)
count += 1
A
.7
B
.8
C
.9
D
.6

答案选C

9、以下叙述正确的是：
A、continue语句的作用是结束整个循环的执行
B、只能在循环体内使用break语句
C、在循环体内使用break语句或continue语句的作用相同
D、从多层循环嵌套中退出时，只能使用quit语句

答案选B

10、a = ‘老男孩教育’，a[:6]
的结果为:
A、‘老男孩教育’ B、‘’  C、TypeError
D、‘老男孩教育老男’

答案选A

11、下列说法正确的是(多选)：
A，字符串的capitalize()
为首字母大写，其余字母小写。
B，列表的pop为通过索引删除，且有返回值。
C，字典的remove为通过键删除字典的键值对。
D，元组为只读列表，只能进行增和查。

答案选A，B

12、下列表达正确的是(多选)：
A、字典中的keys（）方法是将字典的所有键都存放至一个列表中。
B、给一个列表extend（‘ab3’）实际上是添加了a，b, 3
三个字符串。
C、s1 =‘alex @’，s2 =‘alex @’，print(s1 is s2)
为True。
D、‘abc’.encode(‘utf - 8’).decode(‘gbk’) 结果为‘abc’。

答案选：A,B,C,D

13、下列表达正确的是（多选）：
A、a =（1，） a为int类型。
B、l1 = [1, 2, 3]
l2 = l1
l1.append(666)
print(l2)
结果为[1, 2, 3，666]
C、l1 = [22, 33, 44]
l2 = l1[:]
l1与l2的关系为浅copy。
D、集合是无序的不重复的，里面的元素要求是不可哈希的。

答案选：B，C

14、选出你认为正确的答案（多选）：
A、在文件操作中，r + 模式只能读写，不能写读。
B、函数是以功能为导向的。
C、文件操作中，将光标移动至末尾是seek（0, 1）。
D、函数的 * args在默认参数前面。

答案选：A，B，D

15、下列说法正确的是（多选）：
A、函数的return的是将值返回给函数名。
B、函数的实参的位置参数在关键字参数前面。
C、全局作用域包含内置名称空间和局部名称空间。
D、函数名被视为第一类对象。

答案选：B，D

二，填空题（10
分）。

def calc(a, b, c, d=1, e=2):
    return a + b + c - d - e


请分别写出下列标号代码的输出结果，如果出错请写出Error。
print(calc(1, 2, 3, 4, 5))
结果：-3
_____
print(calc(1, 2))
结果：TypeError，没有给C传参
____
print(calc(e=4, c=5, a=2, b=3))
结果：5___

print(calc(1, 2, 3))
结果：3
_____
print(calc(1, 2, 3, d=5, 4))
结果：SyntaxError，位置参数要放在关键字参数前面

获取list的元素个数，和向末尾追加元素所用的方法是__len()_, append()____.

不依赖中间变量，交换变量a和b的值得表达式是____a,b = b,a____.

list = [1, 2, 3, 4, 5]
print(list[10:])
答案是什么？___[] 空列表____.

如何通过一行语句创建一个这样的字典
{1: 'alex', 2: 'alex', 3: 'alex'}？
不能直接写dic = {1: 'alex', 2: 'alex', 3: 'alex'})
____________________________.
    三，简答题（共20分）
1、 is 和 == 的区别 （1
分）
答：is 比较的是两个对象是否完全相同，它们都要是同一个对象，占用的内存地址也要相同
== 比较的是两个对象的内容是否相等，内存地址可以不一样，但是内容必须一样

2、Python
如何实现tuple和list的转换。（1
分）
答：可以使用list()函数转换

3、list和tuple有什么不同 （1
分）
答：
list可以进行增册改查的操作，
tuple不可增删改，只能查询

4、*args和 ** kwargs在什么情况下会使到？请给出使 ** kwargs的事例（2
分）
答：*args和 ** kwargs被称为万能参数，在不确定参数的个数和类型的情况下可以使用，例如装饰器等


5、Python中什么数据类型存在小数据池？小数据池有什么作用？（1
分）
答：只有数字类型有小数据池，小数据池的使用就是为了节省内存

6、在Python3x版本中，s1 = ‘老男孩’，如何将s1转化成utf - 8
的bytes类型？转化成功之后，得到了s2，如何将s2转化成gbk的bytes类型（请写出具体代码）？（2
分）
答：
s2 = s1.encode('utf-8')
s3 = s2.decode().encode('gbk')

7、下面代码有没有问题？如果有问题请指出来（2
分）？
f = open('a.txt', encoding='utf-8')
f.write('666')
答：有问题，write方法需要使用w的模式打开，没有加mode参数默认使用r只读模式打开，因此无法写入

8、l = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8]
将此列表去重。（1
分）
答：  l = set(l)

9、有如下代码，写出最后结果，并解释为什么。（2
分）
l1 = [1, [22, 33, 44], 3, 4, ]
l2 = l1
l3 = l1.copy()
l1.append(666)
l1[1].append('55')
Print(l1, l2, l3)
答：
l1：[1, [22, 33, 44, '55'], 3, 4, 666]
l2: [1, [22, 33, 44, '55'], 3, 4, 666]
l3: [1, [22, 33, 44, '55'], 3, 4]
l1直接赋值给l2,所以l1和l2的内存地址相同，当l1增的时候，l2也会增，l3是通过浅copy方法得到，因此第一层各自独立，从第二层开始，共用一个内存地址



10、‘1, 2, 3’如何变成[‘1’, ’2’, ’3’]？ [‘1’, ’2’, ’3’]如何变成[1, 2, 3]?（写具体代码）（2
分）
答： "1,2,3".split(',')

a = ['1', '2', '3']
b=[]
for i in a:
    i=int(i)
    b.append(i)
print(b)

11、什么是闭包（closure），为什么要用它？（2
分）
答：
1、闭包就是内层函数对外层函数非全局变量的引用；
2、因为闭包不会随着函数的结束而释放，因此可以用于装饰器等需要暂时保留数据的地方


12，global有什么用？nonlocal又是干什么的？（2
分）
答：global用于引用并改变一个全局变量和在局部作用域声明一个全局变量
nonlocal是引用局部变量从哪层引用的该变量，从那层开始全部改变

13，如何终止while循环？（1
分）
答：用break


四，编程题。

1、有文件t1.txt里面的内容为：（6
分）

1, alex, 22, 13651054608, IT
2, wusir, 23, 13304320533, Tearcher
3, taibai, 18, 1333235322, IT

利用文件操作，将其构造成如下数据类型。
[{'id': '1', 'name': 'alex', 'age': '22', 'phone': '13651054608', 'job': 'IT'}, ......]

答：
li = ["id","name","age","phone","job"]
dicts = {}
all = []
with open("1.txt",encoding='utf-8',mode='r') as f1:
    result = []

    for i in f1.readlines():
        #print(i.strip().split(','))
        lines = i.strip().split(',')
        result.append(lines)
    for a in result:
        for b in range(len(a)):
            dicts[li[b]] = a[b]
        all.append(dicts)
print(all)

提个问题：
循环每一行添加到字典元素中时候，key值相同会被覆盖了，所以只能得到最后一行，有什么思路可以在覆盖前获取到


2、写函数，完成以下功能：（6
分）
用户将文件名（文件前提必须存在），操作方法（只有r, w, a三种）传入此函数，此函数按照传入的参数完成相应的操作。
例如：
def func(path, mode, *args):
    pass


func(‘a.txt’, ’r’) 此函数完成的就是以读的模式打开a.txt文件，并打印出来。
func(‘a.txt’, ’w’, ’老男孩教育’)此函数完成的就是以写的模式打开a.txt文件，将内容写入。
func(‘a.txt’, ’a’, ’老男孩教育’)此函数完成的就是以追加的模式打开a.txt文件，将内容追加。

答：
def func(path, mode, *args):
    with open(path,encoding='utf-8',mode=mode) as f1:
        if mode == "r":
            print(f1.read())
        elif mode == "w":
            f1.write(args[0])
        elif mode == "a":
            f1.write("\n"+args[0])

3、写函数完成以下功能：（6
分）
给函数传入一个列表（此列表里面的元素必须全部是str类型），将列表中的每个元素按照顺序依次加上他们的索引，形成新的元素，并添加到一个新列表，将新列表返回。
例如：给函数传入一个列表[‘alex’, ’太白’]，
返回值为[‘alex0’, ’太白1’]
答：
def func1(lists):
    result =[]
    for key,value in enumerate(lists):
        new = str(key)
        result.append(value+new)
    return result



4，写一个函数，完成注册的功能，将用户名，密码写入到文件中（用户名不能重复，如果重复提示他重新输入）。再写一个函数，完成三次登录功能，账号密码从注册的文件中获取。（12
分）
答：
注册函数：
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

登陆函数：
def login():
    with open("username.txt",encoding='utf-8',mode='r+') as file2:
        alluser = file2.readlines()
    name = input("please input your name for login: ").strip()
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
                    break
                else:
                    pwd+=1
                    print("your passwd is error, please retry...")
                    if pwd == 3:
                        print("your input password error thrice, your account locked")
                        exit()
                    continue
            break
        if index == len(alluser)-1:
            print("your name is not exist,please register")
            break
        index += 1


5、编写装饰器，为多个函数加上认证的功能（用户名密码存在文件中，只有一个），要求登录成功一次（给三次机会），后续的函数都无需再输入用户名和密码。（10
分）

答：
def wrapper(f):
    def inner(*args,**kwargs):
        if log_status["status"]:
            ret = f(*args,**kwargs)
            return ret
        else:
            print("您尚未登陆，请先登陆。。。")
            return False
    return inner

log_status = {"username": None,"status": False}
def login():
    name = input("请输入你的用户名： ").strip()
    with open("username.txt",encoding='utf-8',mode='r+') as file2:
        alluser = file2.readlines()
    index = 0
    pwd = 0
    for user in alluser:
        if name in user:
            reault = alluser[index]
            nowuser = reault.strip().split()
            while True:
                passwd = input("please input your password: ").strip()
                if passwd == nowuser[1]:
                    print("%s login success" %name)
                    log_status["username"] = name
                    log_status["status"] = True
                    return log_status
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


@wrapper
def article(username):
    print("欢迎%s来到文章页面。。。。" %username)
@wrapper
def diary(username):
    print("欢迎%s来到日记页面。。。。" %username)
@wrapper
def comment(username):
    print("欢迎%s来到评论页面。。。。" %username)
@wrapper
def enshrine(username):
    print("欢迎%s来到收藏页面。。。。" %username)

@wrapper
def logout(name):
    log_status["username"] = None
    log_status["status"] = False
    print("%s已注销"%name)

funcs= {1: login, 2: article, 3: diary, 4: comment, 5: enshrine, 6: logout, 7: exit}


while True:
    print("欢迎: \n"
          "1、登陆\n"
          "2、文章页面\n"
          "3、日记页面\n"
          "4、评论页面\n"
          "5、收藏页面\n"
          "6、注销\n"
          "7、退出程序")
    selectnum = input("please select number: ").strip()
    try:
        select = int(selectnum)
        if 0 < select <=len(funcs):
            if 1 < select <= 6:
                funcs[select](log_status["username"])
            else:
                funcs[select]()
        else:
            print("您输入的超出范围")
    except ValueError as err:
        print("您输入有误，请输入1-7的数字")

