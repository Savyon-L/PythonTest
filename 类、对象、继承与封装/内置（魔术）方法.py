#1、__str__字符串方法：把类对象转换为字符串，不用则输出内存地址
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student类对象，name：{self.name}, age：{self.age})"

stu = Student("Alice", 20)
print(stu)

#2、__repr__字符串方法：把类对象转换为字符串，通常用于调试和开发
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student类对象，name：{self.name}, age：{self.age})"
stu = Student("Alice", 20)
print(stu)

#3、__lt__小于号方法：用于比较两个对象的大小
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):#other是另一个对象
        return self.age < other.age

stu1 = Student("Alice", 20)
stu2 = Student("Bob", 25)
print(stu1 < stu2)

#4、__le__小于等于号方法：用于比较两个对象的大小
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __le__(self, other):#other是另一个对象
        return self.age <= other.age
stu1 = Student("Alice", 20)
stu2 = Student("Bob", 20)
print(stu1 <= stu2)

#5、__eq__等于号方法：用于比较两个对象的大小
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):#other是另一个对象
        return self.age == other.age
stu1 = Student("Alice", 20)
stu2 = Student("Bob", 20)
print(stu1 == stu2)#必须要有__eq__方法才能比较，否则比较的是内存地址

