from concurrent import futures
import multiprocessing
from re import I
import threading
from os import getpid
# import threading
import time

def inc():
    global i
    i+=1

def task(ii, x):
    print(f'T{ii} PID to {getpid()}')
    s = time.perf_counter()
    x.acquire()
    global i
    # print(f'T{ii} to {threading.current_thread().name}')
    ss = time.perf_counter()
    i = 0
    if(1):
        while i < 10000000:
            inc()
        print(f'locked by {getpid()}')
        e = time.perf_counter()
        ee= time.perf_counter()
        x.release()
        print(f'released by {getpid()} : {round(ee-ss, 5)}')
    return f'Task {ii}:- PID NO:{getpid()} NAME:{threading.current_thread().name} Comp in:{round(e - s, 7)}s'

def ipTsk():
    s = time.perf_counter()
    # print(f'PID task to {threading.current_thread().name}')
    # print(f'IP PID{getpid()}')
    x = input('Enter the ip')
    e = time.perf_counter()
    return f'IP:- PID NO:{getpid()} NAME:{threading.current_thread().name} Comp in:{round(e - s, 7)}s'


def opTsk():
    s = time.perf_counter()
    # i = 0
    global i
    # print(f'OP task to {threading.current_thread().name}')
    # print(f' OP PID {getpid()}')
    while i < 1000:
        print(i)
        i+=1
    e = time.perf_counter()
    return f'OP:- PID NO:{getpid()} NAME:{threading.current_thread().name} Comp in:{round(e - s, 7)}s'

def init(l):
    global lock
    lock = l

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    x = multiprocessing.Lock()
    global i
    # i = 0
    s = time.perf_counter()
    print(f'Thread of main program {threading.current_thread().name}')
    print(f'PID of main program {getpid()}')

    t1 = multiprocessing.Process(target=task, args=(1,x))
    t2 = multiprocessing.Process(target=task, args=(2,x))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # t1 = multiprocessing.Pool(task, initializer=init,initargs=(x,))
    # with futures.ProcessPoolExecutor() as exec:
        # x1 = exec.submit(task, [1,x])
        # x2 = exec.submit(task, [2,x])
    #     # x7 = exec.submit(ipTsk,)
    #     x4 = exec.submit(opTsk,)

        # print(x1.result())
        # print(x2.result())
    #     # print(x7.result())
    #     print(x4.result())

    # print(opTsk())
    # print(ipTsk())
    # print(task(1))
    # print(task(2))

    e = time.perf_counter()

    print(f'Prog got over in {round(e - s, 7)}')