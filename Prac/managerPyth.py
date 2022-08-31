import multiprocessing
import time
from os import getpid

def printing(records):
    # print(f'')
    print(records)
    # for k in records:
    #     print(f'{k}:{records[k]}\n')

def insert(key, value, records):
    records[key] = value

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        re = manager.dict({
            'name':'DVS',
            'age':'22',
            'dob':'3-9-2001',
            'phn':'9360434308'
        })
        r = ['email','durgaivel0309@gmail.com']

        t1 = multiprocessing.Process(target=insert,args=(r[0], r[1],re))
        t2 = multiprocessing.Process(target=printing,args=(re,))

        t1.start()
        t1.join()

        t2.start()
        t2.join()

        print(f'MAIN: {getpid()} \n T1: {t1.pid} \n T2: {t2.pid}')