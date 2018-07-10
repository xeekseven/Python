import requests
import re
import sys
from lxml import etree
import time,threading

notExistDbPoiidText = 'BZDBPW025M,B0FFGQ5T8O,BZDBPV01V1,B0FFGQ4QZC'

def getPoiidInfo():
    url = 'https://ditu.amap.com/detail/get/detail?id='
    namePatten = r"(?<=\"distance\"\S\d\S\"name\"\S\")\S+(?=\",\"geodata)"
    #"x":"116.438758"
    xPatten = r"(?<=\"x\"\S\")\d+\S\d+(?=\")"
    yPatten = r"(?<=\"y\"\S\")\d+\S\d+(?=\")"
    typePatten = r"(?<=\"tag\"\S\")\S+(?=\"\S\S\"spec)"
    longAddrPatten = r"(?<=\"address\"\S\")\S+(?=\"\S\"tag)"
    addrPatten = r"\S+(?=\"\S\"bcs)"
    for item in notExistDbPoiidText.split(','):
        realUrl = url+item
        #print(realUrl)
        result = requests.get(realUrl).text
        poiId = item
        #(?<=\"distance\"\\S\\d+\\S\"name\"\\S\")\\S+(?=\",\"geodata)
        poiName = re.search(namePatten,result,re.M|re.I).group()
        poiAddr = re.search(longAddrPatten,result,re.M|re.I).group()
        if poiAddr.find('bcs') > -1:
            poiAddr = re.search(addrPatten,poiAddr,re.M|re.I).group()
        poiType = re.search(typePatten,result,re.M|re.I).group()
        poiLng = re.search(xPatten,result,re.M|re.I).group()
        poiLat = re.search(yPatten,result,re.M|re.I).group()
        print("insert into tb_cfg_poi values('{0}','{1}','{2}','{3}',{4},{5},NULL,NULL)".format(poiId,poiName,poiAddr,poiType,poiLng,poiLat))

    
if __name__ == '__main__':
    print('北京市西城区","bcs":"白纸坊'.index('bcs'))
    if '北京市西城区","bcs":"白纸坊'.index('bcs') > -1:
         print('北京市西城区","bcs":"白纸坊'.index('bcs'))
    getPoiidInfo()
    