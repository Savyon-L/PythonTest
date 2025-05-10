#__init__()构造方法：在创建类的时候会自动执行，将传入的参数自动传递给_init_()方法使用
class Student:
    def __init__(self,name,age,tel):
        self.name=name#变量定义在构造方法内部，要成为成员变量，需用self表示。
        self.age=age
        self.tel=tel

stu = Student("小明",18,"123456789")
print(stu.name)




class StudentMsg:
    def __init__(self,name,age,tel):
        self.name=name#变量定义在构造方法内部，要成为成员变量，需用self表示。
        self.age=age
        self.tel=tel

    # 添加__str__ 方法定义将学生信息转换为字符串
    def __str__(self):
        return f"学生姓名: {self.name}\t, 学生年龄: {self.age}\t, 学生电话: {self.tel}\t"

#用于定义对象的“官方”字符串表示形式,用于调试和开发。
    def __repr__(self):
        return self.__str__()

students = {}#创建空字典存储学生key和信息
for i in range(1,6):
    print(f"当前录入第{i}位学生信息，总共需录入5位学生信息")
    students[f"stu{i}"] = StudentMsg(
        name = input("请输入学生姓名："),
        age = input("请输入学生年龄："),
        tel = input("请输入学生电话：")
                     )
    print(f"学生{i}信息录入成功，信息为【{students[f"stu{i}"]}】")

print(students)