from file_define import *
from data_define import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("D:/PythonTest/类、对象、继承与封装/文件读取案列/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:/PythonTest/类、对象、继承与封装/文件读取案列/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

#将两个月份的数据合并在一个list存储
all_data: list[Record] = jan_data + feb_data

#数据计算法一:异常处理方法
all_data_dict = {}
for data in all_data:
    try:
        all_data_dict[data.date] += data.money
    except KeyError:
        all_data_dict[data.date] = data.money


"""
数据计算法二:if-else方法
all_data_dict = {}
for data in all_data:
    if data.date in all_data_dict.keys():
        all_data_dict[data.date] += data.money
    else:
        all_data_dict[data.date] = data.money
"""

#可视化图表开发
bar = Bar(
    init_opts=InitOpts(theme=ThemeType.LIGHT, width="800px", height="600px")
)
bar.add_xaxis(list(all_data_dict.keys()))
bar.add_yaxis("销售额", list(all_data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额"),
    xaxis_opts=AxisOpts(name="日期"),
    yaxis_opts=AxisOpts(name="销售额"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
)

bar.render("每日销售额柱状图.html")