import concurrent.futures
import threading
import os

def inc():
    global i
    i += 1

def odd(ii, iii, k, lock):
    global i
    print('The thread name is {}'.format(threading.current_thread().name))
    while i < ii:
        # print(i)
        if i == 0: 
            lock.acquire()
            print(f'locked by {iii} | {threading.current_thread().name} : {os.getpid()}') 
        inc()
        if i == ii - 1: 
            lock.release()
            print(f'released by {iii} | {threading.current_thread().name} : {os.getpid()}') 
        print(i, k)

'''
def even(i):
    while i < 10000:
        print(i)
        i+=2'''

if __name__ == '__main__':
    global i
    i = 0
    lock = threading.Lock()
    with concurrent.futures.ProcessPoolExecutor() as exec:
        t1 = exec.map(odd,[lock, lock])
        # t2 = exec.submit(odd,(100, 2, 'even', lock))
        # concurrent.futures.as_completed(t1).result()
        # concurrent.futures.as_completed(t2).result()
    # odd(10000,20000, 1)
    # print('The thread name is {}'.format(threading.current_thread().name))

    # t1.join()
    # t2.join()

    print('DONE')