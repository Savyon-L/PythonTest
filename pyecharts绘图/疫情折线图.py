import json
from pyecharts.charts import Line
from pyecharts.options import *

with (
    open("D:/PythonTest/pyecharts绘图/美国.txt", "r", encoding="utf-8") as f,
    open("D:/PythonTest/pyecharts绘图/印度.txt", "r", encoding="utf-8") as f1,
    open("D:/PythonTest/pyecharts绘图/日本.txt", "r", encoding="utf-8") as f2,
):
    #清理前面数据
    data = f.read().replace("jsonp_1629344292311_69436(", " ")
    data1 = f1.read().replace("jsonp_1629350745930_63180(", " ")
    data2 = f2.read().replace("jsonp_1629350871167_29498(", " ")
    data = data[:-2]
    data1 = data1[:-2]
    data2 = data2[:-2]
    #json.loads()方法将字符串转换为字典
    data_list = json.loads(data)
    data_list1 = json.loads(data1)
    data_list2 = json.loads(data2)
    #抓取日期数据
    x_data = data_list["data"][0]["trend"]["updateDate"]
    x_data1 = data_list1["data"][0]["trend"]["updateDate"]
    x_data2 = data_list2["data"][0]["trend"]["updateDate"]
    #抓取确诊数据
    y_data = data_list["data"][0]["trend"]["list"][0]["data"]
    y_data1 = data_list1["data"][0]["trend"]["list"][0]["data"]
    y_data2 = data_list2["data"][0]["trend"]["list"][0]["data"]
    #创建一个折线图对象
    line = Line()
    #添加x轴数据
    line.add_xaxis(x_data[:314])
    #添加y轴数据
    line.add_yaxis(
        series_name="美国确诊人数",
        y_axis=y_data[:314],
        label_opts=LabelOpts(is_show=False),
    )
    line.add_yaxis(
        series_name="印度确诊人数",
        y_axis=y_data1[:314],
        label_opts=LabelOpts(is_show=False),
    )
    line.add_yaxis(
        series_name="日本确诊人数",
        y_axis=y_data2[:314],
        label_opts=LabelOpts(is_show=False),
    )
    #设置全局配置项
    #设置标题
    line.set_global_opts(
    title_opts = TitleOpts( True,"2022各国确诊人数对比", pos_left="center", pos_bottom="1%",),
    toolbox_opts=ToolboxOpts(is_show=True),
    legend_opts=LegendOpts(is_show=True),
    #visualmap_opts=VisualMapOpts(is_show=True)
    )
    #渲染图片
    line.render("D:/PythonTest/pyecharts绘图/美国印度日本确诊人数对比.html")







