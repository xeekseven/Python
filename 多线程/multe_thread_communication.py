import os,time,random,threading
from multiprocessing import Pool,Process,Queue

_queue = Queue()

def write(q):
    print("Parent id : %s" % os.getpid())
    while True:
        q.put(random.random())
        time.sleep(random.randint(1,4))
    

def read(q):
    print("Parent id r : %s" % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue' % value)

if __name__ == '__main__':
    th_w = threading.Thread(target=write,args=(_queue,))
    th_r = threading.Thread(target=read,args=(_queue,))
    th_w.setDaemon(True)
    #th_r.setDaemon(True)
    th_w.start()
    th_r.start()
    
    print("run start")