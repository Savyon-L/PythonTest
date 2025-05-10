from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据
with open('D:/PythonTest/pyecharts绘图/1960-2019全球GDP数据.csv', 'r',encoding="GB2312") as f:
    data_lines = f.readlines()

#删除第一条数据
data_lines.pop(0)
data_dict = {}

#把数据转换为字典储存，格式为：
# {年份：[[国家1：GDP1]，[国家2：GDP2]，...]，年份：[[国家1：GDP1]，[国家2：GDP2]，...],...}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])#float转化科学计数法
    #判断字典是否有对应key年份
    try:
        data_dict[year].append([country,gdp])#列如有1960就添加数据
    except KeyError:
        data_dict[year] = []#如有1960而没有1961就创建一个新的key
        data_dict[year].append([country,gdp])

#按年份排序，keys()方法获取字典的所有key
sorted_year_list = sorted(data_dict.keys())

# 构建时间线对象,循环外面创建
timeline = Timeline(
    {"theme": ThemeType.LIGHT},  # 设置主题颜色
)

for year in sorted_year_list:
    bar = Bar()
    data_list = data_dict[year]
    data_list.sort(key=lambda x:x[1],reverse=True)
    new_data_list = data_list[:8]
    country = []
    gdp = []
    for item in new_data_list:
        country.append(item[0])
        gdp.append(item[1]/100000000)#单位转换为亿
    #传入数据必须是列表
    bar.add_xaxis(country)
    bar.add_yaxis("GDP(亿)",gdp,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    # 设置全局配置项
    bar.set_global_opts(
        title_opts=TitleOpts(title=str(year) + "年全球GDP前8国家"),
        xaxis_opts=AxisOpts(name="GDP(亿)"),
        yaxis_opts=AxisOpts(name="国家"),
        legend_opts=LegendOpts(is_show=True),
        toolbox_opts=ToolboxOpts(is_show=True),
    )
    timeline.add(bar, str(year) + "年")
# 设置自动播放
timeline.add_schema(
    play_interval=1000,  # 播放间隔时间,单位毫秒
    is_auto_play=True,  # 是否自动播放
    is_loop_play=True,  # 是否循环播放
    is_timeline_show=True,  # 是否显示时间线
)
timeline.render("动态GDP柱状图.html")
