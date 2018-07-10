import requests
import re
import sys
from lxml import etree
import time,threading

userAgentList = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36']


def GetSubwayInfo():
    try:
        num = 1/0;
        pass
    except Exception as e:
        print('Error:%s' % e)
        raise
    finally:
        pass
    
if __name__ == '__main__':
    GetSubwayInfo()
    #r = requests.get('http://docs.python-requests.org/zh_CN/latest/user/quickstart.html')
    headers = {'user-agent':userAgentList[0]}
    r = requests.get('https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=17&city=440100&geoobj=113.941508%7C22.543014%7C113.953525%7C22.546185&keywords=地铁2号线',headers=headers)
    print(r.content.decode('utf-8'))
    print("我擦")
    #print(r.content)
    