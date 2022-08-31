import multiprocessing
import os
import time

def whileCheck():
    s = time.perf_counter()
    i = 0
    while i < 1000000000:
        i+=1
    e = time.perf_counter()
    print(f'PID: {os.getpid()}\tTIME: {e - s}\n')
    
def ipCmd():
    x = input('Enter any num')

if __name__ == '__main__':
    s = time.perf_counter()
    t1 = multiprocessing.Process(target=whileCheck)
    t2 = multiprocessing.Process(target=whileCheck)
    t3 = multiprocessing.Process(target=whileCheck)
    t4 = multiprocessing.Process(target=whileCheck)
    t5 = multiprocessing.Process(target=whileCheck)
    t6 = multiprocessing.Process(target=whileCheck)
    t7 = multiprocessing.Process(target=ipCmd)
    # t8 = multiprocessing.Process(target=whileCheck)
    # t9 = multiprocessing.Process(target=whileCheck)
    # t10 = multiprocessing.Process(target=whileCheck)
    # t11 = multiprocessing.Process(target=whileCheck)
    # t12 = multiprocessing.Process(target=whileCheck)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    # t8.start()
    # t9.start()
    # t10.start()
    # t11.start()
    # t12.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    # t8.join()
    # t9.join()
    # t10.join()
    # t11.join()
    # t12.join()

    e = time.perf_counter()
    print(f'TIME: {e - s}, MAIN: {os.getpid()}, T1: {t1.pid}, T2: {t2.pid}, T3: {t3.pid}, T4: {t4.pid}, T5: {t5.pid}, T6: {t6.pid}, T7: {t7.pid}')
    # print(f'T7: {t7.pid}, T8: {t8.pid}, T9: {t9.pid}, T10: {t10.pid}, T11: {t11.pid}, T12: {t12.pid}')