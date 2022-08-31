import threading
import os
import time

def task(ii):
    i = 0
    print(f'T{ii} to {threading.current_thread().name}')
    print(f'T{ii} to {os.getpid()}')
    while i < 10000000:
        i+=1
    print(f'Task ovr {ii}')

def ipTsk():
    print(f'IP task to {threading.current_thread().name}')
    print(f'IP task to {os.getpid()}')
    x = input('Enter the ip')

def opTsk():
    i = 0
    print(f'OP task to {threading.current_thread().name}')
    print(f'OP task to {os.getpid()}')
    while i < 1000000:
        # print(i)
        i+=1

if __name__ == '__main__':
    print(f'Thread of main program {threading.current_thread().name}')
    print(f'ID of main program {os.getpid()}')

    t1 = threading.Thread(target=task, args=(1,))
    t2 = threading.Thread(target=task, args=(2,))
    t3 = threading.Thread(target=ipTsk)
    # t4 = threading.Thread(target=opTsk)


    t3.start()
    t1.start()
    t2.start()
    # t4.start()

    t1.join()
    t3.join()
    t2.join()
    # t4.join()