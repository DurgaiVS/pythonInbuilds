import multiprocessing


def mul():
    if __name__ == '__main__':
        print('Printed')
    else:
        print('HaHaHaHaHaHa')

if __name__ == '__main__':
    t1 = multiprocessing.Process(target=mul) 
    t1.start()
    t1.join()