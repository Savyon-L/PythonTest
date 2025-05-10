#画廊功能：网站：gallery.pyecharts.org
#全局配置项：网站：pyecharts.org
#pycharts入门：导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
#创建一个折线图对象
line = Line()
#添加x轴数据
line.add_xaxis(["中国","美国","日本"])
#添加y轴数据
line.add_yaxis(series_name="GDP",
               y_axis=[30,20,10],
)
#设置全局配置项
#设置标题
line.set_global_opts(
    title_opts=TitleOpts(title="2023年各国GDP对比",pos_left="center",pos_bottom="1%",subtitle="数据来源：世界银行"),
#设置图例
legend_opts=LegendOpts(is_show=True),
#设置工具箱
toolbox_opts=ToolboxOpts(is_show=True),
#设置视觉映射
visualmap_opts=VisualMapOpts(is_show=True)
)
# #通过render方法渲染图表
line.render()

