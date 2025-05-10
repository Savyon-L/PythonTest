"""
和文件相关的类定义
"""
from data_define import Record
import json



#先定义一个抽象类用来顶层设计，确定有哪些功能需要实现
class FileReader:

    def read_date(self) -> list[Record]:#返回值注解是list
        """读取文件的数据，读到的每一条数据都转换为Record对象，将他们都封装到list中返回"""
        pass

#读取文本数据的子类
class TextFileReader(FileReader):

    #定义成员变量记录文件路径
    def __init__(self, file_path: str):
        self.file_path = file_path

    #复写（实现抽象类方法）父类的方法
    def read_data(self) -> list[Record]:
        record_list: list[Record] = []#定义一个空列表用来存放Record对象
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()#去掉每行的\n
                data_list = line.split(",")
                record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])##*
                record_list.append(record)
        return record_list

#读取Json数据的子类
class JsonFileReader(FileReader):
    #定义成员变量记录文件路径
    def __init__(self, file_path: str):
        self.file_path = file_path

    #复写（实现抽象类方法）父类的方法
    def read_data(self) -> list[Record]:
        record_list: list[Record] = []#定义一个空列表用来存放Record对象
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                data_dict = json.loads(line)
                record = Record(data_dict["date"], data_dict["order_id"], data_dict["money"], data_dict["province"])
                record_list.append(record)
        return record_list




if __name__ == '__main__':
    text_file_reader = TextFileReader("D:/PythonTest/类、对象、继承与封装/文件读取案列/2011年1月销售数据.txt")
    list1 = text_file_reader.read_data()

    json_file_reader = JsonFileReader("D:/PythonTest/类、对象、继承与封装/文件读取案列/2011年2月销售数据JSON.txt")
    list2 = json_file_reader.read_data()

    print(list1)
    print(list2)





