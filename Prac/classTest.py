import inspect
from queue import Queue

class firClass:
    # DataModel methods are those with 2 underscores
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # This method can only return string value
        return f'{self.mul}'
        # x = {
        #     'name': self.name,
        #     'age': self.age
        # }
        # return x

    def __mul__(self, other):
        # This method will execute when an object instance is
        # multiplied with any number
        if type(other) is not int:
            raise Exception('Invalid argument, must be int')
        self.mul = f'{self.name} ' * other

    def __call__(self):
        # This will execute when we call with the object instance
        print(self.name, self.age, self.mul)

    def __len__(self):
        return len(self.name)

    def findIt(self):
        # This will execute when we call the len of object instance
        print(f'{self.name} is {self.age} years old.')


# print(inspect.getsource(Queue))

class q(Queue):
    def __repr__(self):
        return f'Queue({self._qsize()})'

    def __add__(self, other):
        self.put(other)

    def __sub__(self, other):
        if not self.empty():
            return self.get()
        else:
            raise Exception('EMPTY')


a = firClass('Durgai', 50)
a * 3
print(a)
a()
print(len(a))


qu = q()
qu + 'HI'
qu + 'HELLO'
print(qu - 0)
print(qu - 1)
print(qu - 99)
print(qu)