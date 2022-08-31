import multiprocessing
from os import getpid

def putQ(listt, q):
    for l in listt:
        q.put(l * l * l)

def getQ(q):
    while not q.empty():
        print(q.get())
    print('Queue is empty')

if __name__ == '__main__':
    arr = [i+1 for i in range(10)]
    q = multiprocessing.Queue()

    t1 = multiprocessing.Process(target=putQ,args=(arr,q))
    t2 = multiprocessing.Process(target=getQ,args=(q,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print(f'MAIN: {getpid()} \n T1: {t1.pid} \n T2: {t2.pid}')