import json


def stfCrsEntry(lock):
    lock.acquire()
    with open('staffData.json') as fS:
        stfData = json.load(fS)
    with open('courseData.json') as fC:
        crsData = json.load(fC)

    for i in stfData:
        if  i['title'] == 'S':
            for j in crsData:
                if j['idCrs'] in i['subHand'] and i['idStf'] not in j['stfHandling']:
                    j['stfHandling'].append(i['idStf'])

    with open('courseData.json', 'w') as fW:
        json.dump(crsData, fW, indent=7)
    lock.release()
