import numpy as np
import matplotlib.pyplot as plt
import json
#折线图
# 一共20天 6.20-7.5 有些天掉出榜单
with open("test_data.json", "r", encoding='UTF-8') as f:
    temp = json.loads(f.read())
    index_1 = 1
    for i in temp.keys():
        x = []
        y = []
        print(i)
        print(temp[i])
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
        plt.plot(x, y, 's-', color='r', label="song"+str(index_1))  # s-:方形
        index_1=index_1+1
        print(index_1)
        plt.xlabel("data")  # 横坐标名字
        plt.ylabel("hot")  # 纵坐标名字
        plt.legend(loc="best")  # 图例
        # plt.savefig('.../image_learn/'+i+'.png')
        # plt.close()
    plt.show()
        #plt.savefig('image1/《微微》.pdf')

