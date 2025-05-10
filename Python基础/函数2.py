#函数多返回值
def test_return():
    return 1,"hello",True
x,y,z=test_return()
print(x,y,z)
#函数的多种参数
#1.位置参数：根据函数定义的位置来传递参数
def test_args(name,age,gender):
    print(f"姓名是：{name}，年龄是:{age},性别是:{gender}")
test_args("小明",18,"男")

#2.关键字参数：根据函数定义的参数名来传递参数
def test_args(name,age,gender):
    print(f"姓名是：{name}，年龄是:{age},性别是:{gender}")
test_args(name="小明",gender="男",age=18)

#3.缺省参数：在函数定义时给参数设置默认值
def test_args(name,age,gender="男"):#默认值必须在最后
    print(f"姓名是：{name}，年龄是:{age},性别是：{gender}")
test_args("小马",18)

#4.不定长参数：也叫可变参数，传入的参数个数不确定
#位置传递的不定长：所有参数都被*args变量接收合并成一个元组
def test_args(*args):
    print(args)
test_args("小明",18,"男")
#关键字传递的不定长：所有参数必须是键值对，都被**kwargs变量接收合并成一个字典
def test_args(**kwargs):
    print(kwargs)
test_args(name="小王",age=18,gender="男")

#函数作为参数传递
def test_args(func):
    print(func(1,2))
def func(x,y):
    return x+y
test_args(func)

#lambda匿名函数
"""lambda语法：
lambda 参数1,参数2,...:函数体（只能一行代码）
"""

def test_func2(compute):
    num=compute(1,2)
    print(num)
test_func2(lambda x,y:x+y)#匿名函数只能用一次
