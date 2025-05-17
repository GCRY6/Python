import numpy
import matplotlib
from matplotlib import pyplot
new=int(input("请输入y值:"))
# 修改全局周期参数并补充x=1的数据点
period = 8
x = [2,3,4,5,6,7,8]
y = [4,16,37,49,58,145,42]
x.insert(0, 1)
y.insert(0, new)

def lagrange_interpolation(x1):
    base_x = x[0]  # 基准点自动变为1
    offset = (x1 - base_x) % period  # 现在按8周期计算
    mapped_x = base_x + offset  # 映射到1-9区间
    
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
x2 = numpy.arange(1 - period, 8 + period*2, 0.1)  # 显示3个完整周期
y2 = []

for i in range(len(x2)):
    y2.append(lagrange_interpolation(x2[i]))

pyplot.plot(x2, y2)
pyplot.scatter(x, y, color='red')  # 添加原始数据点显示
pyplot.title('Lagrange Interpolation')  # 添加标题
pyplot.grid(True)  # 添加网格
pyplot.xlim(x[0] - period, x[-1] + period)
pyplot.show()