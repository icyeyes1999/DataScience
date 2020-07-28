import codecs
import json
path1 = "C:/Users/RIO/Desktop/抖查查榜单数据/JSON/"
files = [
    '6.16',
    '6.17',
    '6.18',
    '6.19',
    '6.21',
    '6.22',
    '6.23',
    '6.24',
    '6.26',
    '6.27',
    '6.28',
    '6.29',
    '6.30',
    '7.1',
    '7.2',
    '7.3',
    '7.4',
    '7.5',
    '7.6',
    '7.8',
    '7.11',
    '7.16',
    '7.17',
    '7.18',
    '7.20',
    '7.21',
]
path2 = "file.json"
path3 = 'C:/Users/RIO/Desktop/抖查查榜单数据/compute'
result = {
    'pos':[],
    'T':[],
    'E':[],
    'group':[],
    'name':[],
    'lastDate':[],
    'base':[],
    'initDate':[],
    'length':[],
    'hotestVideo':[]
}
for i in range(len(files)):
    #print(i,": =============")
    with open(path1+files[i]+path2,"r",encoding='UTF-8') as f:
        temp = json.loads(f.read())
        #print(temp)
        for j in temp:
            #print(j['标题']," ",j['数量'])
            if j['标题'] in result['name']:
                tmp = result['name'].index(j['标题'])
                #print(tmp)
                cha=float(files[i])-result['lastDate'][tmp]
                if(cha>=0.1 and cha<=0.6):
                    # result['T'][tmp]+=cha*10
                    result['T'][tmp]+=int(cha*10)
                elif(cha<0.1 and cha>0):
                    result['T'][tmp] += int(cha * 100+0.05)
                elif(cha<0):
                    temp1=int(float(files[i]))
                    result['T'][tmp]+=int((float(files[i])-temp1)*100-(result['lastDate'][tmp]-temp1)*10)
                else:
                    result['T'][tmp]+=int(((float(files[i])-7)*10+(6.31-result['lastDate'][tmp])*100))
                if j==temp[len(temp)-1]:
                    result['E'][tmp]=0
                if float(j['数量'][0:-1])>100:
                    result['group'][tmp]='largeAmount'
                result['lastDate'][tmp]=float(files[i])
            else:
                result['pos'].append(len(result['group']))
                result['T'].append(1)
                result['E'].append(1)
                temp2=j['数量'][0:-1]
                if temp2=='':
                    temp2=0
                if float(temp2)>100:
                    result['group'].append('largeAmount')
                else:
                    result['group'].append('smallAmount')
                result['name'].append(j['标题'])
                result['lastDate'].append(float(files[i]))
                if(files[i][0]=='6'):
                    temp3=files[i][2:]
                    temp3=int(temp3)
                    temp3-=15
                else:
                    temp3=files[i][2:]
                    temp3=int(temp3)
                    temp3+=15
                result['initDate'].append(temp3)
                result['base'].append(float(temp2))
                result['hotestVideo'].append(float(j['关键词'][0:-1]))
                temp4=j['时间'][5:-1]
                try:
                    temp4=float(temp4)
                except:
                    temp4=0
                result['length'].append(temp4)
    # print("==================")
for i in range(0,len(result['pos'])):
    if result['T'][i]==1:
        result['E'][i]=0
print(result)
j = json.dumps(result,ensure_ascii=False,indent=4)
with codecs.open('test_data_Cox.json', "w", "utf-8") as f:
    f.write(j)