from os import getpid
import time
from threading import current_thread
import concurrent.futures

s = time.perf_counter()

arr = [i+1 for i in range(10)]

def mulPro(i):
    print(f'Start Sleeping{i}')
    print(f'{current_thread().name}|| {getpid()}')
    time.sleep(i)
    return f'Finished Sleeping{i}'

if __name__ == '__main__':
    print(f'{current_thread().name}|| {getpid()}')
    with concurrent.futures.ProcessPoolExecutor() as exec:
        res = exec.map(mulPro, arr)
        for r in res:
            print(f'{r} : {current_thread().name}|| {getpid()}')

#     with concurrent.futures.ProcessPoolExecutor() as exec:
#         f = [exec.submit(mulPro, i) for i in arr]
#         for i in concurrent.futures.as_completed(f):
#             print(i.result())

    e = time.perf_counter()

    print(f'Finished in {round(e-s, 3)}')