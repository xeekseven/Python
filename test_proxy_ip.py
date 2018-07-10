import urllib.request
import re


class TestProxy(object):
    def __init__(self):
        self.ip = '163.177.151.23'
        self.port = '80'
        self.url = 'http://www.whatismyip.com.tw/'
        self.timeout = 3

        self.regex = re.compile(r'baidu.com')

        self.run()

    def run(self):
        self.linkWithProxy()

    def linkWithProxy(self):
        server = 'http://'+ self.ip + ':'+ self.port


        url = self.url #打算抓取内容的网页
        proxy_ip={'http': server}  #想验证的代理IP
        proxy_support = urllib.request.ProxyHandler(proxy_ip)
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64)")]
        urllib.request.install_opener(opener)
        print(urllib.request.urlopen(url).read().decode('utf-8'))
        '''
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({'http':server}))
        urllib.request.install_opener(opener)
        try:
            response = urllib.request.urlopen(self.url, timeout=self.timeout)
        except:
            print('%s connect failed' % server)
            return
        else:
            try:
                str = response.read()
            except:
                print('%s connect failed' % server)
                return
            if self.regex.search(str):
                print('%s connect success .......' % server)
                print(self.ip + ':' + self.port)
        '''

if __name__ == '__main__':
    Tp = TestProxy()
