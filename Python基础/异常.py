#异常捕获语法
from logging import exception

try:#尝试执行可能发生错误代码
    f = open("D:/PythonTest/test2.txt", 'r',encoding='utf-8')
except:#如果出现错误则执行except代码
    print("文件并不存在,我将只读r模式改为写入w模式")
    f = open("D:/PythonTest/test2.txt", 'w',encoding='utf-8')

#捕获指定的异常
try:
    print(name)
except NameError as e:
    print("变量未定义", e)

#捕获多个异常
try:
    1/0
except (ZeroDivisionError, NameError) as e:
    print("除数不能为0", e)

#捕获所有异常
try:
    1/0
except Exception as e:
    print("发生了异常", e)

#异常的else语句(可写可不写)
try:
    2/1
except Exception as e:
    print("发生了异常", e)
else:
    print("没有发生异常")#没有异常执行else语句

#finally语句(可写可不写)，无论是否发生异常都会执行，如关闭文件
try:
    f = open("D:/PythonTest/test2.txt", 'r',encoding='utf-8')
except Exception as e:
    print("发生了异常", e)
else:
    print("没有发生异常")
finally:
    f.close()