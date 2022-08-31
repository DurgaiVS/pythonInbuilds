import json
import multiprocessing
import threading
from stfCrsEntry import stfCrsEntry

def appendData(self, lock):
        lock.acquire()
        try:
            with open('staffData.json') as f:
                data = json.load(f)
                data.append(self)
                f.close()
            with open('staffData.json', 'w') as f:
                json.dump(data, f, indent=4)
                f.close()
        finally:
            lock.release()

def staffDataEnter():
            Name = input('NAME: ')
            Dob = input('DOB: ')
            Title = input('JOB_title: ')
            Position = input('Position: ')
            if Title == 'S':
                Subs = input('SubHand: [Seperate with comma (,)]\n')
                SubHand = Subs.split(",")
                Programme = input('PROGRAMME: ')
                if Programme == 'BE': Dept = input('DEPT: ')
                else: Dept = None
            else:
                Programme = None 
                SubHand = None
                Dept = None
            Staff(Name, Dob, Dept, Programme,Title, Position, SubHand)
            m1 = multiprocessing.Process(target=appendData, args=(self,multiprocessing.Lock()))
            m1.start()
            m1.join()
            t1 = multiprocessing.Process(target=stfCrsEntry, args=(multiprocessing.Lock(),))
            t1.start()
            t1.join()

self = dict({})

class Staff:
    def idd(this, title, lock, mLock):
        mLock.acquire()
        lock.acquire()
        try:
            with open('idStf.json') as f:
                idStf = json.load(f) 
                idStf[title] += 1
                this['idStf'] = title + '.' + str(idStf[title]) 
                f.close()
            with open('idStf.json', 'w') as f:
                json.dump(idStf, f, indent=5)
                f.close()
        finally:    
            lock.release()
            mLock.release()

    def __init__(x, name, dob, dept, programme, title, position, subHand):
        self['name'] = name
        self['dob']  = dob
        self['dept']  = dept
        self['programme']  = programme
        self['title'] = title
        self['position'] = position
        self['subHand'] = subHand
        self['idStf'] = None
        m1 = threading.Thread(target=Staff.idd, args=(self, title, threading.Lock(), multiprocessing.Lock()))
        m1.start()
        m1.join()