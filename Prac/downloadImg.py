import time
import concurrent.futures
from urllib import request

arr = [i+1 for i in range(10)]

def loopThruM(i):
    print(f'Start Downloading{i}')
    time.sleep(i)
    print(f'Done downloading{i}')
def loopThruS(i):
    print(f'Start Downloading{i}')
    time.sleep(i)
    return f'Done downloading{i}'
    #for ex.sub, you have to return a val
    #for ex.map, you don't want to

startS = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    res = [executor.submit(loopThruS, ar) for ar in arr]
    for f in concurrent.futures.as_completed(res):
        print(f.result())
endS = time.perf_counter()


startM = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(loopThruM, arr)   
endM = time.perf_counter()
# end = time.perf_counter()   
print(f'S Took {round(endS-startS, 5)}s')
print(f'M Took {round(endM-startM, 5)}s')