import numpy
import matplotlib
from matplotlib import pyplot
x=[2,3,4,5,6,7,8]
y=[4,16,37,49,58,145,42]
def lagrange_interpolation(x1):
    p=[]
    L_n=0
    for i in range(len(x)):
        numerator=1
        denominator=1
        for j in range(len(x)):
            if i!=j:
                numerator=numerator*(x1-x[j])
                denominator=denominator*(x[i]-x[j])
        p.append(numerator/denominator)

    for i in range(len(x)):
        L_n=L_n+y[i]*p[i]
    return round(L_n,3)
print(lagrange_interpolation(1))
# 修正arange参数（start, stop, step）并增加采样点
x2 = numpy.arange(-10, 10, 0.1)  # 原参数(10,10,20)只能生成1个点
y2 = []

for i in range(len(x2)):
    y2.append(lagrange_interpolation(x2[i]))

pyplot.plot(x2, y2)
pyplot.scatter(x, y, color='red')  # 添加原始数据点显示
pyplot.title('Lagrange Interpolation')  # 添加标题
pyplot.grid(True)  # 添加网格
pyplot.show()