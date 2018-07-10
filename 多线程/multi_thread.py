import time,threading
from multiprocessing import Queue

def loop():
    print('thread is running %s' % threading.current_thread().name)
    index = 0
    while(index < 5):
        index+=1
        print('thread %s > %s' % (threading.current_thread().name,index))
        time.sleep(1)

if __name__ == '__main__':
    th = threading.Thread(target=loop,name='GoThread')
    th.start()
    th.join()
    print('end')
