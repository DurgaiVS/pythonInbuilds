from start import op
import start as ss
# print(dir(ss))#list all names defined
# print(ss.o, 'HHHHHHH')
# print(op, '...')
class MyPy:
    def __init__(this, name, age, *rest):
            this.name = name
            this.age = age
            this.arr = rest

    def __complex__():
        pass
        
    def pri(this):
        print("Hello I'm " + this.name + ", and I'm {} years old.".format(this.age))
        print(this.arr)
py = MyPy("DVS", 56, 'ji', 'fi')
py.age = 70
# del py.arr
# py.pri()

class Child(MyPy):
    def __init__(this, name, age, dob,*rest):
        super().__init__(name, age, *rest)
        this.dob = dob

    def __iter__(this):
        this.it = 1
        return this

    def __next__(this):
        x = this.it
        if x <= 100:
            this.it += this.age
            return x
        else:
            raise StopIteration
    
    def priii(this):
        print(this.dob)

pp = Child('DVS', 44, 90,'d', 'n')
# pp.priii()
classIter = iter(pp)
# print(next(classIter))
# print(next(classIter))
# print(next(classIter))
# print(next(classIter))