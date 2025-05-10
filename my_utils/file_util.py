def print_file_info(file_name):
    f=None
    try:
        f=open(file_name, 'r', encoding='utf-8')
        print(f.read())
    except Exception as e:
        print(e)
    finally:
        if f:#如果变量是None，则不执行close
            f.close()

def append_to_file(file_name,data):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(data)
        f.write('\n')

if __name__ == '__main__':
    print_file_info('D:/PythonTest/test2.txt')
    append_to_file('D:/PythonTest/test2.txt','hello world')
