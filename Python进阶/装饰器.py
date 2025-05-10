#装饰器就是创建一个闭包函数，在闭包函数里调用原函数，可以达到不改动原函数的同时增加额外功能。
"""基础写法：
def outer(func):
    def inner():
        print("开始执行")
        func()
        print("执行结束")
    return inner

def sleep():
    import time
    import random
    print("睡眠中。。。。。。。")
    time.sleep(random.randint(1,5))

fn = outer(sleep)
fn()
"""

# 装饰器的语法糖写法：
def outer(func):                # 装饰器函数，接收一个函数func作为参数
    def inner():                #inner是闭包函数，用于增强func的功能
        print("开始执行")
        func()                  #调用原始函数func
        print("执行结束")
    return inner                # #返回增强后的闭包函数inner

@outer                         #使用@outer语法糖来装饰sleep函数，等同于sleep = outer(sleep)
def sleep():                     #原函数
    import time
    import random
    print("睡眠中。。。。。。。")
    time.sleep(random.randint(1,5))

sleep()                        #实际上调用的是inner函数


