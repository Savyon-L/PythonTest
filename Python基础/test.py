"""
多行注释
多行"""
money = 100
print("钱包还有：",money)
print("9//2=",9//2)# 整除
print("9**2=",9**2)# 乘方
print("9%2=",9%2)# 取余
name="小明"
class_num=12
avg_salary=10000.1
#占位，和Java+拼接字符串类似,常见占位符%s,%d,%f分别是字符串，整数，浮点数
message="我是：%s,班级人数：%d，平均工资：%f" %(name,class_num,avg_salary)
print(message)
#快速占位符：f"{变量}"
message1=f"我是：{name},班级人数:{class_num},平均工资：{avg_salary}"
print(message1)
# 数字精度控制
num1=11.346
print("%5d " %num1)# 5个字符宽度，整数
print("%5.2f " %num1)# 5个字符宽度(小数点占一位)，2位小数
print("%.2f " %num1)# 2位小数
# input函数
#name=input("who are you?")
print("hello",name)
# 输出不换行
print("hello",end=" ")
print("world")
# 制表符
print("hello\tworld")
print("csgo\tlol")
#九九乘法表
i=1
while i<10:
    j=1
    while j<=i:
        print(f"{j}*{i}={i*j}\t",end=" ")
        j+=1
    i+=1
    print()#换行




