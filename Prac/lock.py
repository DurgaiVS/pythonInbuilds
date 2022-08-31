# from asyncio import futures
import concurrent.futures
import threading
import os
import time

global i
i = 0

def inc():
    global i
    i+=1

def task(lock):
    print(f' PID:{os.getpid()}')
    s = time.perf_counter()
    lock.acquire()
    print(f' Locked by {os.getpid()}')
    global i
    while i < 10000000:
        if i + 1 == 10000000: lock.release() & print(f' Lock released by{os.getpid()}')
        inc()
    e = time.perf_counter()
    print(f'Time taken by  is {round(e - s, 10)}')

if __name__ == '__main__':
    print(f'MAIN PID: {os.getpid()}')
    lock = threading.Lock()
    with concurrent.futures.ProcessPoolExecutor() as exec:
        t = [exec.submit(task, lock) for _ in [1,2]]
        
        for i in concurrent.futures.as_completed(t):
            i.result()