import os 

def dealCellFile(filePath):
    cityDic = {}
    with open(filePath,'r',encoding='GBK',newline='\r\n') as f:
        for line in f.readlines():
            strlist = line.split('\t')
            type = strlist[-1].strip('\r\n')
            
            if type == '4G':
                key = '%s' % strlist[6].strip('.0')
            if type == '2G':
                key = '%s-%s' % (strlist[5].strip('.0'),strlist[6].strip('.0')) 
            cityDic[key] = strlist[0]
    return cityDic
            


if __name__ == '__main__':
    dic = dealCellFile('D:\\开发数据\\hadoop数据\\工参\\tb_cell.bcp');
    with open('result.txt','w',encoding='utf-8') as f:
        for value in dic:
            f.write('%s:%s\n' % (value,dic[value]))
            #print(dic[value])
    
