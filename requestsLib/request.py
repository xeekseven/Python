import requests
import re
import sys
from lxml import etree
import time,threading


def getBitCoinInfo():
    url = 'https://bitcoinwisdom.com/'
    html = requests.get(url)
    res = etree.HTML(html.text)
    change_per_list = res.xpath("//tr[@id='o_btcusd']/td/span/text()")
    price = res.xpath("//tr[@id='o_btcusd']/td/text()")
    if len(change_per_list)!=4:
        pass
    today_per = change_per_list[0]
    _24hour_per = change_per_list[1]
    _7day_per = change_per_list[2]
    _30day_per = change_per_list[3]
    print(today_per)
    print(float(price[0])*6.4875)
    
if __name__ == '__main__':
    t = threading.Thread(target=getBitCoinInfo, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)