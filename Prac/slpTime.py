import time
import threading
global x
x = 0
start = time.perf_counter()

def slpTime(lock):
    global x
    print('Before sleep {}'.format(threading.current_thread().name))
    lock.acquire()
    x+=1
    lock.release()
    print('{0}{1}'.format(x, threading.current_thread().name))
    x+=1
    time.sleep(1)
    print('{0}{1}'.format(x, threading.current_thread().name))
    print('After sleep {}'.format(threading.current_thread().name))

if __name__ == '__main__':
    lock = threading.Lock()
    t1 = threading.Thread(target=slpTime, args=(lock,))
    t2 = threading.Thread(target=slpTime, args=(lock,))
    # slpTime()
    t1.start()
    t2.start()

    t1.join()
    t2.join()

finish = time.perf_counter()

print('Took {}s'.format(round(finish - start, 5)))