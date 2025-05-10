#递归：即方法(函数)自己调用自己
import os

"""
def test_os():
    print(os.listdir("D:/PythonTest/Python进阶/递归test"))#列出目录下的所有文件和文件夹
    print(os.path.isdir('D:/PythonTest/Python进阶/递归test/a'))#判断是否是目录
    print(os.path.exists('D:/PythonTest/Python进阶/递归test'))#判断路径是否存在
"""


def get_files_recursion_from_dir(path):
    """
    从指定目录开始递归获取所有文件
    :param path: 被遍历的目录
    :return: list,包含所有文件的列表
    """
    files = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + '/' + f
            if  os.path.isdir(new_path):
                files.extend(get_files_recursion_from_dir(new_path))
            else:
                files.append(new_path)
        return files
    else:
        print("路径不存在")
        return []

if __name__ == '__main__':
    s = get_files_recursion_from_dir("/Python进阶/递归test")
    print(s)