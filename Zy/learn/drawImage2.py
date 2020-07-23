import matplotlib.pyplot as plt
import json
#折线图
with open("test_data.json", "r", encoding='UTF-8') as f:
    temp = json.loads(f.read())
    for i in temp.keys():
        x = []
        y = []
        print(i)
        print(temp[i])
        if(len(temp[i])<10):
            continue
        numlist = temp[i]
        for j in range(1,len(numlist)):
            num1 = list(map(float,numlist[j].split()))
            num2 = list(map(float, numlist[j-1].split()))
            y.append(num1[1]-num2[1])
        for k in range(0,len(y)):
            x.append(k+1)
        plt.plot(x, y, 's-', color='r', label="ATT-RLSTM")  # s-:方形
        plt.xlabel("time")  # 横坐标名字
        plt.ylabel("addHot")  # 纵坐标名字
        plt.legend(loc="best")  # 图例
        # plt.savefig('image2/'+i+'.png')
        # plt.close()
        plt.show()
        #plt.savefig('image1/《微微》.pdf')

