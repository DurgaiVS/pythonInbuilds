import threading
import os
arr = [[], []]
arrT = []
def adding(x, a, xx):
    arrT.append(f'PID-{os.getpid()}, {x}')
    for i in range(a, x, 1):
        arr[xx].append(x * x)


t1 = threading.Thread(target=adding, args=(10, 0, 0))
t2 = threading.Thread(target=adding, args=(20, 10, 1))

t1.start()
t2.start()

t1.join()
t2.join()

print(arr)
print(arrT)