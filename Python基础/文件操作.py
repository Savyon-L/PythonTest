#文件有r，w，a三种模式，其中w模式是写入模式，打开文件时会清空文件内容，如没有这个文件会自行创建一个；r模式是只读模式；a模式是追加模式
"""#打开文件
f=open("D:/Java资料/笔记.txt","r",encoding="utf-8")
print(f.read().count("字"))

#1.读取文件read()方法,形成字符串每次读取都从上一次中断的地方开始
print(f"读取十个字节的结果：{f.read(10)}")
print(f"读取全部内容的结果：{f.read()}")

#2.读取文件readlines()方法:读取文件全部行，封装到列表中
lines=f.readlines()
print(f"读取全部行的结果：{lines}")

#3.读取文件readline()方法:只读取一行
line=f.readline()
print(f"读取一行的结果：{line}")

#4.for循环读取文件
for line in f:
    print(f"每一行数据：{line}")

#5.关闭文件close()方法，不关程序就会一直被程序占用
f.close()
import time

#6.with open()方法:操作完成后自动关闭文件
with open("D:/Java资料/笔记.txt","r",encoding="utf-8")as f:
    for line in f:
        print(f"每一行数据：{line}")
time.sleep(500000)"""




#---------------------------------------------------------------------------------
#文件的写入：调用write（）方法时内容并未写入到文件中，而是先写入到缓存区，等缓存区满了或者调用flush()方法时才会写入到文件中
"""f=open("D:/PythonTest/笔记.txt","w",encoding="utf-8")
f.write("hello world！！！")#内容写入内存中
f.flush()#将缓存区的内容写入到文件中
f.close()#close()方法会自动flush()"""

#---------------------------------------------------------------------------------
#文件的追加：a模式中文件不存在会创建一个新文件，存在就会在文件末尾追加内容
"""f=open("D:/PythonTest/笔记.txt","a",encoding="utf-8")
f.write("python！！！")
f.flush()
f.close()
"""

#使用with open()打开多个文件
with(
    open("D:/PythonTest/bill.txt", "r", encoding="utf-8") as f,
    open("D:/PythonTest/bill2.txt.bak", "w", encoding="utf-8") as f2
):
    for line in f:
        if "测试" not in line:#直接判断字符串line是否包含"测试"
            f2.write(line)

