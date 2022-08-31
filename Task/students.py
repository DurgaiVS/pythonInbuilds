import json
import multiprocessing
import threading

def appendData(self, lock):
        lock.acquire()
        try:
            with open('studentData.json') as f:
                data = json.load(f)
                data.append(self)
                f.close()
            with open('studentData.json', 'w') as f:
                json.dump(data, f, indent=4)
                f.close()
        finally:
            lock.release()

def attStd(self, lock, lockM):
    lockM.acquire()
    lock.acquire()
    try:
        id = self['idStd']
        stfChsn = self['stfChosen']
        with open('attendanceStd.json') as fa:
            dataAtt = json.load(fa)
            dataAtt[id] = {}
            dataAtt[id]['timetable'] = {
                'T': [],
                'P': []
            } #[]
            i = 10
            for iC, iS, iT in stfChsn: 
                if iT == 'T': 
                    dataAtt[id]['timetable'][iT].append([i,iC + '/' + iS])
                    dataAtt[id][iC + '/' + iS] = 0
                else: 
                    dataAtt[id]['timetable'][iT].append([iC + '/' + iS])
                    dataAtt[id][iC + '/' + iS] = 0
                    continue
                i += 1
                if i == 13: i += 1
        with open('attendanceStd.json', 'w') as fw:
            json.dump(dataAtt, fw, indent=2)
    finally:
        lock.release()
        lockM.release()

def stdDataEnter():
            with open('courseData.json') as f:
                dataC = json.load(f)
            with open('staffData.json') as ff:
                dataS = json.load(ff)

            Name = input('NAME :')
            Dob = input('DOB :')
            Programme = input('PROGRAMME :')
            if Programme == 'BE': Dept = input('DEPT :')
            else: Dept = None
            Sem = 1
            StfChosen = []

            for i in dataC:
                if i['sem'] == str(Sem) and i['programme'] == Programme:
                    if Dept != None and Dept in i['dept'] or Dept == None:
                        stfDet = []
                        for j in dataS:
                            if j['idStf'] in i['stfHandling']:
                                stfDet.append((j['idStf'], j['name']))
                        
                        if len(stfDet) > 1:
                            print(f"Subject Name: {i['crsName']}\tSubject Code: {i['idCrs']}\tStaffs Handling: {i['stfHandling']}")
                            print(stfDet) 
                            x = input('Enter the staff id you have chosen: ')
                        elif len(stfDet) == 1: x = stfDet[0][0]
                        StfChosen.append([i['idCrs'],x,i['crsType']])

            Student(Name, Dob, Dept, Programme, Sem, StfChosen)
            m1 = multiprocessing.Process(target=appendData, args=(self,multiprocessing.Lock()))
            m1.start()
            m1.join()

self = dict({})

class Student:
    def idd(this, dept, prog, lock, mLock):
        mLock.acquire()
        lock.acquire()
        try:
            with open('idStd.json') as f:
                idStd = json.load(f)
                if prog == 'BE': 
                    idStd[prog][dept] += 1
                    this['idStd'] = dept + '.' + str(idStd[prog][dept]) 
                else: 
                    idStd[prog] += 1
                    this['idStd'] = prog + '.' + str(idStd[prog])
                f.close()

            with open('idStd.json', 'w') as f:
                json.dump(idStd, f, indent=5)
                f.close()
        finally:
            lock.release()
            mLock.release()

    def __init__(x, name, dob, dept, programme, sem, stfChosen):
        self['name'] = name
        self['dob']  = dob
        self['dept']  = dept
        self['programme']  = programme
        self['sem'] = sem
        self['stfChosen'] = stfChosen
        self['idStd'] = None
        m1 = threading.Thread(target=Student.idd, args=(self,dept,programme, threading.Lock(), multiprocessing.Lock()))
        m2 = threading.Thread(target=attStd, args=(self,threading.Lock(), multiprocessing.Lock()))

        m1.start()
        m1.join()

        m2.start()
        m2.join()