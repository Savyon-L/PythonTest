"""1.猜数字import random

num=random.randint(1,100)
count=0
while(True):
    num2=int(input())
    if  num2>num:
        print("大了")
    elif num2<num:
        print("小了")
    else:
        print("猜对了")
        break
    count+=1
    print(f"你猜了{count}次")"""
from contextlib import nullcontext
from random import choice

"""2.九九乘法表for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end=" ")
    print()"""

"""3.发工资import random
salary=10000
for i in range(1,21):
    performance = random.randint(1, 10)
    if performance >=5:
        salary-=1000
        if(salary>=0):
            print(f"向员工{i}发放工资1000元，账户余额还剩余{salary}元")
        else:
            print("工资发放完了，下个月领取吧。")
            break
    else:
        print(f"员工{i}，绩效分{performance}，低于5，不发工资，下一位")"""

"""4.定义函数:def 函数名(传入参数):
              函数体
             return 返回值"""
# def add(x,y):
#     """函数说明：计算x+y的值
#     :param x: 第一个数
#     :param y: 第二个数
#     :return: x+y的值
#     """
#     result=x+y
#     print(f"{x}+{y}={result}")
# add(4,6)
#
# def adc():
#     print("hello")#没有return，默认返回None
# r=adc()
# print(r)
#
# #global关键字设置函数内部变量为全局变量
# num=100
# def testA():
#     print(num)
# def testB():
#     global num
#     num=200
#     print(num)
# testA()
# testB()
# print(num)

"""
money=5000000
name=None
def query(show_header):#通过参数控制是否显示表头
    if show_header:
        print("-------查询余额--------")
    print(f"{name}您好，您的余额为{money}元")
def deposit(data):
    global money
    money+=data
    print('-------存款-------')
    print(f"{name}您好，您存款{data}成功。")
    query(False)
def withdraw(data):
    global money
    money-=data
    print('-------取款-------')
    print(f"{name}您好，您取款{data}成功。")
    query(False)
def main():
    print("-------ATM机-------")
    print("查询余额\t","[输入1]\t")#一个制表符对不齐就两个
    print("存款\t\t","[输入2]\t")
    print("取款\t\t","[输入3]\t")
    print("退出\t\t","[输入4]\t")
    return int(input("请输入操作："))

name=str(input("请输入姓名："))
while True:
    choice = main()
    if choice == 1:
        query(True)
        continue
    elif choice == 2:
        data = int(input("请输入存款金额："))
        deposit(data)
        continue
    elif choice == 3:
        data = int(input("请输入取款金额："))
        withdraw(data)
        continue
    elif choice == 4:
        print("谢谢使用");
        break
    else:
        print("输入错误");
        break
"""

"""
def test_module(x,y):
    insult=x+y
    print(insult)

if __name__=="__main__":#将功能代码与测试代码分开独立运行
    test_module(1,2)
"""

__all__=["test_module"]#__all__控制import*时哪些功能被导入
def test_module(x,y):
    insult=x+y
    print(insult)
def test_module2(x,y):
    insult=x-y
    print(insult)