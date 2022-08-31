D = 10
V = 3.1
S = 'd'
I = 1+0j
x = 'd {0}    {0}      {0}  S P HIII  {1}'

y = {83:80} 
z = ('D', 'V')
# print(x.translate({83:70, 80:72, 72:71}))
# print(x.translate(x.maketrans('SP','PS', 'H')).format('D', 'V'))
# print(x.capitalize())#1st index to capital
# print(x.casefold())#to lower case
# print(isinstance(x,str))

dictio = {
    1: 'i',
    2: 'ii',
    3: 'iii',
    4: 'iiii'
}
# for i in dictio.keys():
    # print(i)
# print(True if dictio.get(5) else False)
arr = ['aaa', 'baa', 'caa', 'a', 'd']
print(arr.pop(2), 'EHEHEH')
ar = [a if 'a' in a else 'b' for a in arr ]
ra = [a for a in arr if 'aa' in a]
string = 'Hii this is Durgai'.replace(' ', '')
let = ['{}'.format(ii) for ii in string]
let.sort(key=str.lower,reverse=False)
let.reverse()
del let[0]
print(let)
# print(ar, ra)
tup = (1,2,3,4,'rf',6,7,'avad')
(one, two, *three, four) = tup
print(one)
print(two)
print(three)
print(four)
se = set((1,2,3,4,5,6,7,9,8))
se1 = set(('d', 's', 'j', 'k', 9))
se2 = se.union((se1))
se.update((11,))
se.add(10)
se.discard(8)
se3 = se.intersection(se1)
se4 = se.symmetric_difference(se1)
print(se3)
print(se4)
[print(see) for see in se2]

di = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four'
}

print(di.keys())
print(di.values())
print(di.items())
if 1 in di:
    print("yes")
di[1] = 'ttt'
di.update({2:"hehehe", 9: "ndsoajibo"})
di["he"] = "1111"
di.pop(3)
di.popitem()#removes last removed item
del di[4]
diii = dict(di)
print(diii)
o = 1
t = 2
h = 3
print('HI') if 0 == 2 else print("HOO") if t == 3 else print("HEE") if h == 2 else print("PoyaYov")
print("magizhcih") if o == 1 and t == 2 else print("..") if 0 == 2 or h == 3 else print(",,,")


for i in range(2,20,2):#from 2 to 20 by incrementing by 2
    print(i)
else:#Note: The else block will NOT be executed if the loop is stopped by a break statement.
    print("Finally Finished")


def myFunc(name, Fname = 'DVS'):
    print(name)
    print(Fname)
def myF(n, *F):
    print(n)
    print(F)
def mF(**n):
    print(n)
myFunc( "DMM" )
myF(1,2,3,4,5,6,7)
# mF(1,2,3,4,5,'ji',6,7,8)

def li(l):
    return {x for x in l}

print(li([1,2,3,4,5,6,7,8,2,3,4,5,6,7,1,8]))

op = 10
def lam(n):
    op = 12
    print('op', op)
    return lambda a : n * a
le = lam(10)(5)
print('opG', op)
print(le)