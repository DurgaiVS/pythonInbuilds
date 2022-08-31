import itertools
# from re import A
import threading
import multiprocessing
import time
from os import getpid

def inc(a):
    # global a
    a+=1
    return a
    # print(a)

def opTsk():
    # print(f'OP task to {getpid()}')
    s = time.perf_counter()
    x = itertools.count()
    for i in x:
        print(x)
        if i == 10000: break
    e = time.perf_counter()
    print(f'OP:- PID: {getpid()}, Took {round(e - s, 10)}')

def proc(iii, lock, a, value):
    # global a
    s = time.perf_counter()
    # i = 0
    lock.acquire()
    while a < 10000000:
        # i+=1
        a = inc(a)
        ii = a * (a + (20 / 100) - 333)
    value.value = a
    lock.release()
    e = time.perf_counter()
    print(f'PROC{iii}:- PID: {getpid()}, Took {round(e - s, 10)}')

def ipTsk():
    # print(f'IP task to {getpid()}')
    s = time.perf_counter()
    x = input('Enter ip: \n')
    e = time.perf_counter()
    print(f'IP:- PID: {getpid()}, Took {round(e - s, 10)}')

if __name__ == '__main__':
    global a
    a = 0
    s = time.perf_counter()
    lock = multiprocessing.Lock()
    result = multiprocessing.Value('i')# .Value('i',10) , 10 specifies the value
    '''
    To pass array bw processes, you can, 
    arr = multiprocessing.Array('dataType', length)
    [dataType: 'i'-int & 'd'-float]
    and pass as argument in 
#!  multiprocess.Process(target=, args=(arr)).
    now, append value inside the arr in that process.
#?  Comms can only happen bw parent and child processes.
    '''
    # lock = threading.Lock()
    # print(f'PROG PID: {getpid()}')
    # t1 = multiprocessing.Process(target=opTsk)
    # t2 = multiprocessing.Process(target=ipTsk)
    t3 = multiprocessing.Process(target=proc, args=(1,lock,a,result))
    t4 = multiprocessing.Process(target=proc, args=(2,lock,a))

    # t2.start()
    # t1.start()
    t3.start()
    t4.start()

    # opTsk()
    # proc(1)
    if t3.is_alive() and t4.is_alive():
        print(f'T3:{t3.is_alive}, T4:{t4.is_alive}')

    # t1.join()
    # t2.join()
    t3.join()
    t4.join()

    # inc()

    e = time.perf_counter()
    print(f'PROGRAM PID: {getpid()}, TOOK {round(e - s, 10)}\n t1 = {t3.pid}, t1 = {t4.pid}')