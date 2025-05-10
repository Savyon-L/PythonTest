#类的语法： class 类名:
#               类的属性(定义在类中的变量)
#               类的方法(定义在类中的函数)
#            对象 = 类名()

"""
#1.设计一个类(类比生活中设计一份登记表)
class Student:
    name = None
    gender = None
    nationality = None#国籍
    native_place = None#籍贯
    age = None
#2.创建一个对象(类比生活中打印一份登记表)
stu_1 = Student()
#3.对象属性进行赋值(类比生活中填写登记表)
stu_1.name = '小明'
stu_1.gender = 'male'
stu_1.nationality = '中国'
stu_1.native_place = '北京'
stu_1.age = 18
#4.获取对象中记录的信息(类比生活中查看登记表)
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)
"""

class Student:
    name = None

    def say_hello(self):#self表示对象本身,若要访问内部成员变量需加上self
        print(f'大家好，我是{self.name}')

    def say_hello2(self, msg):
        print(f'大家好，我是{self.name}, {msg}')

stu = Student()
stu.name = "小明"
stu.say_hello()#调用对象的方法
stu.say_hello2("你好呀！")#调用对象的方法

