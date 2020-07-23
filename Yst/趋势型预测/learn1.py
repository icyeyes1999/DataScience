#python 实现时间序列(趋势型序列预测)
#三种拟合曲线，一次、二次和三次
import json
from xlutils.copy import copy


import numpy as np
import matplotlib.pyplot as plt
import xlrd
from sklearn.linear_model import LinearRegression
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文字体
plt.rcParams['axes.unicode_minus'] = False    # 显示负号
filePath1 = 'Learn1/1/'
filePath2 = 'Learn1/2/'
filePath3 = 'Learn1/3/'
#画出一次回归拟合曲线
def linear_trend(x, y,name):
    lreg = LinearRegression()
    lreg.fit(x, y)
    #print(lreg.coef_[0])
    coef = round(lreg.coef_[0], 4)
    intercept = round(lreg.intercept_, 4)

    pred = lreg.predict(x)
    plt.plot(pred,'s-', color='r')
    plt.title("线性趋势方程 yt={} + ({})t".format(intercept, coef))
    #plt.show()
    plt.savefig(filePath1 + name + '.png')
    plt.close()
    return (intercept, coef)
#画出二次回归拟合曲线
def second_order_trend(x, y,name):
    lreg = LinearRegression()
    lreg.fit(x, y)
    coef = lreg.coef_
    intercept = round(lreg.intercept_, 4)
    #print(coef)
    pred = lreg.predict(x)
    plt.plot(pred)
    plt.title("二阶曲线 yt={} + ({})t + ({})t**2".format(intercept, round(coef[0], 4), round(coef[1], 4)))
    plt.savefig(filePath2 + name + '.png')
    plt.close()
    return (intercept, coef)
#画出三次回归拟合曲线
def third_order_trend(x, y,name):
    lreg = LinearRegression()
    lreg.fit(x, y)
    coef = lreg.coef_
    intercept = round(lreg.intercept_, 4)

    pred = lreg.predict(x)
    plt.plot(pred)
    plt.title("三阶曲线 yt={} + ({})t + ({})t**2 + ({})t**3".format(
        intercept, round(coef[0], 4), round(coef[1], 4), round(coef[2], 4)))
    plt.savefig(filePath3 + name + '.png')
    plt.close()
    return (intercept, coef)

with open("test_data_modification.json", "r", encoding='UTF-8') as f:
    temp = json.loads(f.read())
    for i in temp.keys():
        x = []
        y = []
        #print(i)
        #print(temp[i])
        if(len(temp[i])<10):
            continue
        numlist = temp[i]
        index = 1
        for j in numlist:
            num = list(map(float,j.split()))
            #print(num)
            #x.append(num[0]*100)
            x.append(index)
            index = index + 1
            y.append(num[1])
        #一次
        x_ = np.array(x).reshape(-1,1)
        y_ = np.array(y)
        # print(x_)
        # print(y)
        a = linear_trend(x_,y_,i)
        #print(linear_trend(x_,y,i))
        with open("Learn1.txt", encoding="utf-8", mode="a") as data:
            data.write(i+"    "+str(a[0])+"    "+str(a[1])+"\n")
        #二次
        x2 = []
        y2 = y
        for p in x:
            x2.append([p,p*p])
        x2_ = np.array(x2)
        y2_ = np.array(y2)
        a = second_order_trend(x2_,y2_,i)
        #print(second_order_trend(x2_,y2_,i))
        with open("Learn1-2.txt", encoding="utf-8", mode="a") as data:
            data.write(i+"    "+str(a[0])+"    "+str(a[1][0])+"    "+str(a[1][1])+"\n")

        #三次
        x3 = []
        y3 = y
        for p in x:
            x3.append([p,p*p,p*p*p])
        x3_ = np.array(x3)
        y3_ = np.array(y3)
        #print(x3_)
        a = third_order_trend(x3_,y3_,i)
        #print(third_order_trend(x3_,y3_,i))
        with open("Learn1-3.txt", encoding="utf-8", mode="a") as data:
            data.write(i+"    "+str(a[0])+"    "+str(a[1][0])+"    "+str(a[1][1])+"    "+str(a[1][2])+"\n")

