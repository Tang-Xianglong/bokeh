#!_*_ coding:utf-8 _*_

import numpy as np
import pandas as pd
from bokeh.charts import Bar
from bokeh.plotting import figure, output_file,show

## 柱状图
data = {'y':[1,2,3,4,5]};
# print type(data)

output_file('./figure/line1.html', title='line');

p = Bar(data, title='line chart example', xlabel='x', ylabel='values', width=400, height=400)

show(p);

## 读取文件,画函数图
# data1 = pd.read_table('./data/data1', header=None, encoding='utf-8', delim_whitespace=True);
data1 = pd.read_table('./data/data1', header=None, encoding='utf-8', sep='  ');
x=data1[0]
y=data1[1]
z=data1[2]

p=figure(width=400, height=400, title='x and y')
p.title_text_color = 'black'    #标题颜色
p.title_text_font = 'times'   #标题字体
p.title_text_font_style = 'italic'   #标题字体样式
p.title_text_font_size = '20pt' #标题字体大小为12磅

p.background_fill = 'beige' #画布背景颜色
p.xaxis.axis_label = 'Innovation'   # x轴变量
p.xaxis.axis_label_text_color = '#aa6666'   # x轴变量颜色
p.xaxis.axis_label_standoff = 10    # x轴变量字体离x坐标轴的距离
p.xaxis.axis_label_text_font_size = '20pt'  # x轴变量字体大小
p.xaxis.axis_label_text_font_style = "bold"    # x轴字体的样式

p.yaxis.axis_label = 'Efficient'   # y轴变量
p.yaxis.axis_label_text_color = 'black'   # y轴变量颜色
p.yaxis.axis_label_standoff = 10    # y轴变量字体离y坐标轴的距离
p.yaxis.axis_label_text_font_size = '20pt'  # y轴变量字体大小
p.yaxis.axis_label_text_font_style = "italic"


p.line(x, y, line_width=2, line_color='black', legend='f1')
p.circle(x, y, fill_color='yellow', size=15, legend='f1', line_color='green')

p.line(x, z, line_width=2, line_color='green', legend='f2')
p.diamond(x, z, fill_color=None, size=15, legend='f2', line_width=2, line_color='blue')

##图例设置
# p.legend.orientation = "bottom_left"
p.legend.label_text_font = 'times'
p.legend.label_text_font_style = 'italic'
p.legend.label_text_color = 'navy'

output_file('./figure/line2.html')

show(p)