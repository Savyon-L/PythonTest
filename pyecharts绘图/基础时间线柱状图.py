#Timeline()时间线：再每一个时间点上显示一个图表
#reversal_axis()反转坐标轴：将x轴和y轴互换
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

#创建柱状图
bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP",[30,30,20],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP",[50,50,50],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP",[70,60,60],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

#构建时间线对象
timeline = Timeline(
    {"theme": ThemeType.LIGHT},  # 设置主题颜色
)
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")

#设置自动播放
timeline.add_schema(
    play_interval=1000,  # 播放间隔时间,单位毫秒
    is_auto_play=True,   # 是否自动播放
    is_loop_play=True,   # 是否循环播放
    is_timeline_show=True,  # 是否显示时间线
)
#绘图是用时间线绘图而不是bar对象
timeline.render("基础时间线柱状图.html")

