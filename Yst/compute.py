import codecs
import json
path1 = "C:/Users/ty/Desktop/抖查查榜单数据/JSON/"
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
    '7.5'
]
path2 = "file.json"
path3 = 'C:/Users/ty/Desktop/抖查查榜单数据/compute'
result = {}
for i in range(len(files)):
    #print(i,": =============")
    with open(path1+files[i]+path2,"r",encoding='UTF-8') as f:
        temp = json.loads(f.read())
        #print(temp)
        for j in temp:
            #print(j['标题']," ",j['数量'])
            if j['标题'] in result.keys():
                #print(result[j['标题']])
                tmp = result[j['标题']]
                tmp.append(files[i]+" "+j["数量"][0:-1])
                #print(tmp)
                result[j['标题']] = tmp
            else:
                result[j['标题']] = [files[i]+" "+j["数量"][0:-1]]
    #print("==================")
print(result)
j = json.dumps(result,ensure_ascii=False,indent=4)
with codecs.open('test_data.json', "w", "utf-8") as f:
    f.write(j)