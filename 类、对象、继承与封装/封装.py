#1、定义私有成员：私有成员变量和私有成员方法都以__开头
class Phone:
    __current_voltage = 0.5  # 私有成员变量

    def __keep_single_core(self):
        print("CPU 保持单核运行")

#私有成员无法被类对象使用，但被其他的成员使用
    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5G 通话")
        else:
            self.__keep_single_core()
phone = Phone()
phone.call_by_5g()


class Phone1:
    __is_5g_enable = False  # 私有成员变量

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G 开启")
        else:
            print("5G 关闭,使用 4G")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone1 = Phone1()
phone1.call_by_5g()

