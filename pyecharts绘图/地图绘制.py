import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据文件
with open("D:/PythonTest/pyecharts绘图/疫情.txt", "r", encoding="utf-8") as f:
    # json.loads()方法将字符串转换为字典
    update_list = json.loads(f.read())
    data_dict = update_list["areaTree"][0]["children"]
    data = []#地图中传入数据类型是：列表中嵌套元组
    """如[("北京"：99)，("上海"：100)]"""
    for item in data_dict:
        name = item["name"]
        confirm = item["total"]["confirm"]
        data.append((name,confirm))
# 创建地图对象
map = Map()
# 添加地图数据
map.add("全国各地确诊人数", data, "china")
# 设置全局配置项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "确诊人数1~99人", "color": "#FFD700"},
            {"min": 100, "max": 999, "label": "确诊人数100~999人", "color": "#FFC125"},
            {"min": 1000, "max": 9999, "label": "确诊人数1000~9999人", "color": "#FF7F00"},
            {"min": 10000, "max": 99999, "label": "确诊人数10000~99999人", "color": "#db5a51"},
            {"min": 100000, "max": 999999, "label": "确诊人数100000人以上", "color": "#ff1405"},
        ]
    )
)
map.render("疫情地图.html")
