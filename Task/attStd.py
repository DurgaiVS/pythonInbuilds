import json
from datetime import datetime
import multiprocessing
import threading

def updateAtt():
    now = datetime.now()
    if int(now.strftime('%M')) <= 15 and now.strftime('%H') in ['10', '11', '12', '14']:
        lock = threading.Lock()
        lockM = multiprocessing.Lock()
        lockM.acquire()
        lock.acquire()
        try:
            with open('attendanceStd.json') as f:
                data = json.load(f)
                stdID = input('Enter the students: [seperate ids with comma (,)]')
                stdIDs = stdID.split(',')
                if now.strftime('%A') in ['Wednesday', 'Saturday'] and int(now.strftime('%H')) >= 12:
                    if now.strftime('%H') == '12':
                        for i in stdIDs:
                            data[i][data[i]['timetable']['P'][0]] += 1
                    elif now.strftime('%H') == '14':
                        for i in stdIDs:
                            data[i][data[i]['timetable']['P'][1]] += 1
                
                else:
                    if now.strftime('%A') != 'Saturday':
                        for i in stdIDs:
                            for j, k in data[i]['timetable']['T']:
                                if now.strftime('%H') == str(j):
                                    data[i][k] += 1
                    
                    else:
                        for i in stdIDs:
                            for j, k in data[i]['timetable']['T']:
                                if int(now.strftime('%H')) + 2 == j and j == 12 or int(now.strftime('%H')) + 3 == j and j == 14:
                                    data[i][k] += 1

            with open('attendanceStd.json', 'w') as fw:
                json.dump(data, fw, indent=3)
        finally:
            lock.release()
            lockM.release()
    elif now.strftime('%H') not in ['10', '11', '12', '14', '15']:
        print('\nNot the attendance time\n')
    else: print('Sorry, TOO late for attendance')