import json
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from sklearn.linear_model import LinearRegression
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文字体
plt.rcParams['axes.unicode_minus'] = False    # 显示负

#画出一次回归拟合曲线
def linear_trend(x, y,name,a,b):
    lreg = LinearRegression()
    lreg.fit(x, y)
    #print(lreg.coef_[0])
    coef = round(lreg.coef_[0], 4)
    intercept = round(lreg.intercept_, 4)

    pred = lreg.predict(x)
    plt.plot(pred,'s-', color='r',label="1次")
    plt.plot(a,b,'r-',color='b',label="true value")
    plt.title("线性趋势方程 yt={} + ({})t".format(intercept, coef))
    plt.legend()
    return (intercept, coef)
#画出二次回归拟合曲线
def second_order_trend(x, y,name,a,b):
    lreg = LinearRegression()
    lreg.fit(x, y)
    coef = lreg.coef_
    intercept = round(lreg.intercept_, 4)
    #print(coef)
    pred = lreg.predict(x)
    plt.plot(pred,'s-',color='r',label="2次")
    plt.legend()
    plt.plot(a, b, 'r-', color='b', label="true value")
    plt.title("二阶曲线 yt={} + ({})t + ({})t**2".format(intercept, round(coef[0], 4), round(coef[1], 4)))
    return (intercept, coef)
#画出三次回归拟合曲线
def third_order_trend(x, y,name,a,b):
    lreg = LinearRegression()
    # 拟合出三次函数
    lreg.fit(x, y)
    coef = lreg.coef_
    intercept = round(lreg.intercept_, 4)

    #添加时间预测 len(a)-len(x)+1
    # print(len(a))
    # print(len(x))
    # print(x)
    # x1=[]
    # for i in range(1,len(a)+1):
    #     x1.append([i,i*i,i*i*i])
    # x1_=np.array(x1)
    x1=[]
    for i in range(1,len(a)+5):
        x1.append([i,i*i,i*i*i])
    x1_=np.array(x1)

    pred = lreg.predict(x1_)

    # print(lreg._decision_function(x))

    plt.plot(pred,'r-',color='r',label="3次拟合预测")
    plt.plot(a, b, 'r-', color='purple', label="实际值")
    # plt.title("三阶曲线 yt={} + ({})t + ({})t**2 + ({})t**3".format(
    #     intercept, round(coef[0], 4), round(coef[1], 4), round(coef[2], 4)))
    plt.legend()
    drawAverage()
    plt.show()
    return (intercept, coef)


def drawAverage():
    #折线图
    list_ex=[6.16,6.17,6.18,6.19,6.20,6.21,6.22,6.23,6.24,6.25,6.26,6.27,6.28,6.29,6.30,7.1,7.2,7.3,7.4,7.5]
    average_line=[]
    x_line=[]
    index_song=1
    num_song=0
    actual_num_song=[]

    #新增ma3曲线
    ma3=[]
    x_line_ma3=[]

    #新增ma5曲线
    ma5=[]
    x_line_ma5=[]

    #ma20均线
    x_line_ma20=[]

    song_name=""
    # 一共多少天的数据 图像即总天数-1
    with open("test_data_modification.json", "r", encoding='UTF-8') as f:
        temp = json.loads(f.read())

        for i in range(1,len(list_ex)):
            average_line.append(0.0)
        for i in range(1,len(list_ex)):
            x_line.append(i)
        for i in range(3,len(list_ex)):
            ma3.append(0.0)
            x_line_ma3.append(i)
        for i in range(5, len(list_ex)):
            ma5.append(0.0)
            x_line_ma5.append(i)
        # 计算song总数
        for i in temp.keys():
            if(len(temp[i])<10):
                continue
            num_song=num_song+1
        # print("num_song="+str(num_song))
        #实际每天计算平均值的song数量 list 未用
        for i in range(1,len(list_ex)):
            actual_num_song.append(0)

        for i in temp.keys():
            song_name=i
            x = []
            y = []
            if(len(temp[i])<10):
                continue
            # print(i)
            # print(temp[i])
            templist = list(temp[i])

            # 预处理 先判断这首歌最后一天有没有新增
            if list(map(float,templist[len(templist)-1].split()))[0]!=list_ex[len(list_ex)-1]:
                templist.append(str(list_ex[len(list_ex)-1])+" "+str(list(map(float,templist[len(templist)-1].split()))[1]))
            print(templist)
            # 预处理 再判断这首歌第一天有没有在热门榜上
            if list(map(float,templist[0].split()))[0]!=list_ex[0]:
                templist.insert(0,str(list_ex[0])+" "+str(list(map(float,templist[0].split()))[1]))

            # 需求1 处理templist 将当天跌出榜单算为0增长
            # 需求2 因为可能网站出现未刷新的问题 所以如果是0增长 则视为增长了明日增量的2/5(系数 minus)
            numlist=[]
            h=0
            for w in range(0,len(list_ex)):
                num=list(map(float,templist[h].split()))
                if num[0]==list_ex[w]:
                    numlist.append(templist[h])
                    h=h+1   #h被消耗 加一
                else:
                    #判断数据是否更新2
                    num_before=list(map(float,templist[h-1].split()))
                    minus=(num[1]-num_before[1])*0.4+num_before[1]
                    numlist.append(str(list_ex[w])+" "+str(minus))
                    #h未被消耗 不变

            for j in range(1,len(numlist)):
                num1 = list(map(float,numlist[j].split()))
                num2 = list(map(float, numlist[j-1].split()))
                y.append(num1[1]-num2[1])
                if(num1[1]-num2[1]!=0):
                    actual_num_song[j-1]=actual_num_song[j-1]+1
                average_line[j-1]=average_line[j-1]+(num1[1]-num2[1])
            x_line_ma20 = []
            for k in range(0,len(y)):
                x.append(k+1)
                x_line_ma20.append(k+1)
            # print(song_name)
            # plt.title(song_name)

            #  每首歌的热度曲线
            # plt.plot(x, y, 's-', color='r', label="song "+str(index_song))  # s-:方形
            index_song=index_song+1
            # plt.xlabel("time")  # 横坐标名字
            # plt.ylabel("addHot")  # 纵坐标名字
            # plt.legend(loc="best")  # 图例

            # plt.savefig('image2/'+i+'.png')
            # plt.close()

            # average line
            if index_song-1==num_song:
                for k in range(0,len(average_line)):
                    average_line[k]=average_line[k]/index_song
                plt.plot(x_line, average_line, 's-', color='b', label="average")  # s
                plt.legend()

        # ma3
        for i in range(3,len(list_ex)):
            ma3[i-3]=(average_line[i-3]+average_line[i-2]+average_line[i-1])/3
        plt.plot(x_line_ma3,ma3,'s-',color='green',label='ma3',linestyle=':')
        plt.legend()
        # ma5
        for i in range(5,len(list_ex)):
            ma5[i-5]=(average_line[i-5]+average_line[i-4]+average_line[i-3]+average_line[i-2]+average_line[i-1])/5
        plt.plot(x_line_ma5,ma5,'s-',color='pink',label='ma5',linestyle='--')
        plt.legend()
        # 均线ma20
        sum=0
        for i in range(0,len(list_ex)-1):
            sum=sum+average_line[i]
        sum_ave=sum/len(average_line)
        ma20=[]
        for i in range(0,len(list_ex)-1):
            ma20.append(sum_ave)

        x_line_ma20_2=[]
        ma20_2=[]
        for i in range(0,26):
            x_line_ma20_2.append(i)
            ma20_2.append(sum_ave)
        plt.plot(x_line_ma20_2,ma20_2,'r-',color='black',label='ma20均线')
        plt.legend()


        # plt.show()

with open("test_data_modification.json", "r", encoding='UTF-8') as f:
    list_ex=[6.16,6.17,6.18,6.19,6.20,6.21,6.22,6.23,6.24,6.25,6.26,6.27,6.28,6.29,6.30,7.1,7.2,7.3,7.4,7.5]
    temp = json.loads(f.read())
    song_name=""
    for i in temp.keys():
        song_name=i
        x = []
        y = []
        if (len(temp[i]) < 10):
            continue
        templist = temp[i]

        # 预处理 先判断这首歌最后一天有没有新增
        if list(map(float, templist[len(templist) - 1].split()))[0] != list_ex[len(list_ex) - 1]:
            templist.append(
                str(list_ex[len(list_ex) - 1]) + " " + str(list(map(float, templist[len(templist) - 1].split()))[1]))
        # print(templist)
        # 预处理 再判断这首歌第一天有没有在热门榜上
        if list(map(float, templist[0].split()))[0] != list_ex[0]:
            templist.insert(0, str(list_ex[0]) + " " + str(list(map(float, templist[0].split()))[1]))

        #处理不在榜单的天
        numlist = []
        h = 0
        for w in range(0, len(list_ex)):
            num = list(map(float, templist[h].split()))
            if num[0] == list_ex[w]:
                numlist.append(templist[h])
                h = h + 1  # h被消耗 加一
            else:
                # 判断数据是否更新2
                num_before = list(map(float, templist[h - 1].split()))
                minus = (num[1] - num_before[1]) * 0.4 + num_before[1]
                numlist.append(str(list_ex[w]) + " " + str(minus))

        for j in range(1, len(numlist)):
            num1 = list(map(float, numlist[j].split()))
            num2 = list(map(float, numlist[j - 1].split()))
            y.append(num1[1] - num2[1])
        for k in range(0, len(y)):
            x.append(k+1)

        print(song_name)
        plt.title(song_name)

        # 三次
        x3 = []
        y3 = y
        for p in x:
            x3.append([p, p * p, p * p * p])
        x3_ = np.array(x3)
        y3_ = np.array(y3)
        # y3_ = np.array([y3[0],y3[1],y3[2],y3[3],y3[4],y3[5],y3[6],y3[7],y3[8],y3[9],y3[10],y3[11],y3[12],y3[13],y3[14]])
        a = third_order_trend(x3_, y3_, i, x, y)
        with open("Learn1-3.txt", encoding="utf-8", mode="a") as data:
            data.write(
                i + "    " + str(a[0]) + "    " + str(a[1][0]) + "    " + str(a[1][1]) + "    " + str(a[1][2]) + "\n")


    plt.show()