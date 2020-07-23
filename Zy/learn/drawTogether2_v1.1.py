import matplotlib.pyplot as plt
import json
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
    print("num_song="+str(num_song))
    #实际每天计算平均值的song数量 list 未用
    for i in range(1,len(list_ex)):
        actual_num_song.append(0)

    for i in temp.keys():
        x = []
        y = []
        if(len(temp[i])<10):
            continue
        print(i)
        print(temp[i])
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
        for k in range(0,len(y)):
            x.append(k+1)

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

    for i in range(3,len(list_ex)):
        ma3[i-3]=(average_line[i-3]+average_line[i-2]+average_line[i-1])/3
    plt.plot(x_line_ma3,ma3,'s-',color='green',label='ma3')
    for i in range(5,len(list_ex)):
        ma5[i-5]=(average_line[i-5]+average_line[i-4]+average_line[i-3]+average_line[i-2]+average_line[i-1])/5
    plt.plot(x_line_ma5,ma5,'s-',color='pink',label='ma5')

    plt.show()
        #plt.savefig('image1/《微微》.pdf')

