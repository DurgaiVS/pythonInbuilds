import threading

def odd(i, ii, iii):
    print('The thread name is {}'.format(threading.current_thread().name))
    while i < ii:
        # print(i)
        i+=iii
    print(i)
'''
def even(i):
    while i < 10000:
        print(i)
        i+=2'''

if __name__ == '__main__':
    t1 = threading.Thread(target=odd,args=(0, 10000, 2))
    t2 = threading.Thread(target=odd,args=(1, 10000, 2))


    t1.start()
    t2.start()
    odd(10000, 20000, 1)
    # print('The thread name is {}'.format(threading.current_thread().name))

    t1.join()
    t2.join()

    print('DONE')