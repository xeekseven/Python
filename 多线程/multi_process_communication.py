import os,time,random
from multiprocessing import Pool,Process,Queue

_queue = Queue()

def write(value):
    print("Parent id : %s" % os.getpid())
    _queue.put(value)

