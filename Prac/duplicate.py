import math

f = open('./start.py', 'r')
print(f.readline(5))

x = '  kdjsvb    '
print(x.split("k"))

ip = input("Enter the ip")
pp = ['{}'.format(i) for i in ip]
print(pp)

x1 = int(input('Num 1: '))
x2 = int(input('Num 2: '))
print(x1 + x2)
print(x1 - x2)
print(x1 * x2)
print(x1 / x2)
print(x1 % x2)
print(x1 ** x2)
print(x1 & x2)
print(x1 | x2)



x = [1,2,3,4,5,6,7,8,9,0,9,8,8,7,7,6,6,5,5,1,4,4,4,3,3,3,2,2,21,1,1]
y = {}
z = set(x)
a = list(dict.fromkeys(x))
for i in x:
    if y.get(i):
        y[i] += 1
    else:
        y[i] = 1
print(y, z, a)

strRev = 'Hii Bro, How are you'[::-1]
print(strRev)#string reversed