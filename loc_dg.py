import os

file = 'data.txt'

data = []

prevNum = '0'
index = 0
with open(file,'r',encoding='utf8') as sf:
    for row in sf.readlines():
        #print(type(row))
        index+=1
        num = row
        if(num < prevNum):
            print(index)
        prevNum = num

