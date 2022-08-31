from students import stdDataEnter
from staffs import staffDataEnter
from courses import crsDataEnter
from attStd import updateAtt

if __name__ == '__main__':
    x = 1
    while int(x):
        x = input('PRESS FOR\nStaff:1\tStudent:2\tCourse:3\tAttendance:4\tExit:0\n')
        if int(x) == 1: staffDataEnter()
        elif int(x) == 2: stdDataEnter()
        elif int(x) == 3: crsDataEnter()
        elif int(x) == 4: updateAtt()
        else: continue