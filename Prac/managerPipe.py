import multiprocessing
from os import getpid

def sender(toName, msgs):
    for i in msgs:
        toName.send(i)
        print(f'SENT: {i}')
    toName.close()

def receiver(fromName):
    while 1:
        msgs = fromName.recv()
        for i in msgs:
            print(f'RECD: {i}')

if __name__ == '__main__':
    msgs = ['HI', 'Hello', 'HRU', 'I"M FINE', 'GOOD']

    parent, child = multiprocessing.Pipe()

    t1 = multiprocessing.Process(target=sender,args=(parent, msgs))
    t2 = multiprocessing.Process(target=receiver,args=(child,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f'MAIN: {getpid} \n T1: {t1.pid} \n T2: {t2.pid}')