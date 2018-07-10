from multiprocessing import Process,Pool
import os,time


def single_thread():
    print('Parent : %s' % os.getpid())
    p = Process(target=run_proc, args = ('test',))
    p.start()
    p.join()

def pool_thread():
    pool = Pool(2)
    for index in range(5):
        pool.apply_async(run_proc, args=(index,))
    pool.close()
    pool.join()
    print('run end')

# 子进程要执行的代码
def run_proc(name):
    time.sleep(5)
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    #single_thread()
    pool_thread()