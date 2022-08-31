import multiprocessing as m
import os
import time
import sys

def pri(l, n):
    s = time.perf_counter()
    l.acquire()
    print(f'locked by {os.getpid()}')
    try:
        time.sleep(10)
        print(n)
    finally:
        l.release()
        e = time.perf_counter()
        print('{} TOOK : {:4f}'.format(os.getpid(),e - s))

def two(l,n):
    l.acquire()
    s = time.perf_counter()
    print(f'locked by {os.getpid()}')
    l.release()
    e = time.perf_counter()
    print(n, f'TOOK {e - s}')
        
if __name__ == '__main__':
    s = time.perf_counter()
    l = m.Lock()

    t1 = m.Process(target=pri, args=(l,10))
    t2 = m.Process(target=two, args=(l,20))
    t3 = m.set_executable(os.path.join(sys.exec_prefix, 'realMulPro.py'))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    e = time.perf_counter()

    print(m.cpu_count())

    print(f'MAIN: {os.getpid()} \n T1: {t1.pid} \n T2: {t2.pid} \n TIME: {e - s}')