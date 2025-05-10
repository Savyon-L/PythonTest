#thread_obj = threading.Thread([group, target, name, args, kwargs, *, daemon)
#-group:暂时无用，未来功能的预留参数
#-target:线程要执行的目标任务（函数）名
#-name:线程的名字，一般不用设置
#-args:传递给目标函数的参数，元组类型
#-kwargs:传递给目标函数的参数，字典类型
#-daemon:是否是守护线程，默认值为False

import time
import threading

#线程锁
#Python 的线程是真正的操作系统线程，由操作系统调度器决定何时切换。
# sing() 和 dance() 两个线程会并发执行，它们的 print() 和 time.sleep(1) 可能在任何时间点被中断或切换

print_lock = threading.Lock()

def sing(msg):
    while True:
        with print_lock:#获取锁
            print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        with print_lock:#获取锁
            print(msg)
        time.sleep(1)

if __name__ == "__main__":
    sing_thread = threading.Thread(target = sing, args = ("唱歌",))
    dance_thread = threading.Thread(target = dance, kwargs = {"msg":"跳舞"},)

    sing_thread.start()
    dance_thread.start()


