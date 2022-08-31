import json
import multiprocessing
# import threading
from stfCrsEntry import stfCrsEntry

def appendData(self, lock):
        lock.acquire()
        try:
            with open('courseData.json') as f:
                data = json.load(f)
                data.append(self)
                f.close()
            with open('courseData.json', 'w') as f:
                json.dump(data, f, indent=4)
                f.close()
        finally:
            lock.release()

def crsDataEnter():
            Name = input('NAME: ')
            IdCrs = input('idCrs: ')
            Programme = input('PROGRAMME: ')
            if Programme == 'BE': 
                Dep = input('DEPT: [seperate with comma (,)]\n')
                Dept = Dep.split(",")
            else: Dept = None
            CrsType = input('Enter the course type: [\'P\' - practical or \'T\' - theory]\n')
            Sem = input('SEM: ')
            StfHandling = []
            Course(Name, IdCrs, Dept, Programme, Sem, CrsType, StfHandling)
            m1 = multiprocessing.Process(target=appendData, args=(self,multiprocessing.Lock()))
            m1.start()
            m1.join()
            t1 = multiprocessing.Process(target=stfCrsEntry, args=(multiprocessing.Lock(),))
            t1.start()
            t1.join()

self = dict({})

class Course:
    def __init__(x, name, idCrs, dept, programme, sem, crsType, stfHandling):
        self['crsName'] = name
        self['idCrs']  = idCrs
        self['dept']  = dept
        self['programme']  = programme
        self['sem'] = sem
        self['crsType'] = crsType
        self['stfHandling'] = stfHandling