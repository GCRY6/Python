import numpy
import matplotlib
from matplotlib import pyplot
x=[2,3,4,5,6,7,8]
y=[4,16,37,49,58,145,42]
# 在全局定义周期参数
period = 7  # 新增全局变量

def lagrange_interpolation(x1):
    base_x = x[0]
    # 使用全局的period变量
    offset = (x1 - base_x) % period  # 移除了局部period定义
    
    mapped_x = base_x + offset
    
    p=[]
    L_n=0
    for i in range(len(x)):
        numerator=1
        denominator=1
        for j in range(len(x)):
            if i!=j:
                numerator *= (mapped_x - x[j])  # 使用映射后的x进行计算
                denominator *= (x[i] - x[j])
        p.append(numerator/denominator)

    for i in range(len(x)):
        L_n=L_n+y[i]*p[i]
    return round(L_n,3)
print(lagrange_interpolation(1))
# 修正arange参数（start, stop, step）并增加采样点
# 调整采样范围展示3个完整周期
# 修改后的采样范围代码
x2 = numpy.arange(x[0] - period, x[-1] + period*2, 0.1)  # 现在可以访问全局period
y2 = []

for i in range(len(x2)):
    y2.append(lagrange_interpolation(x2[i]))

pyplot.plot(x2, y2)
pyplot.scatter(x, y, color='red')  # 添加原始数据点显示
pyplot.title('Lagrange Interpolation')  # 添加标题
pyplot.grid(True)  # 添加网格
pyplot.xlim(x[0] - period, x[-1] + period)
pyplot.show()