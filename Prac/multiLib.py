import multiprocessing
import threading
# import threading
import os
import time

def sleepy_man():
    print(f'Starting to sleep, PID: {os.getpid()}')
    time.sleep(1)
    print(f'Done sleeping, PID: {os.getpid()}')

if __name__ == '__main__':
    print(f'PID: {os.getpid()}')
    tic = time.time()
    p1 =  multiprocessing.Process(target= sleepy_man)
    p2 =  multiprocessing.Process(target= sleepy_man)
    p1.start()
    p2.start()
    p3 = multiprocessing.Queue(maxsize=10, )
    print(f'I come inbw the process, PID: {os.getpid()}')
    p1.join()
    p2.join()
    toc = time.time()
    print('Done in {:.4f} seconds'.format(toc-tic))