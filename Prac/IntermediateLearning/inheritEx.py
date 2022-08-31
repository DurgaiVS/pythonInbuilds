class Head:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def h(self):
        return f'{self.name}, {self.age}'

    # property decorators:-  getter, setter, deleter
    @property
    def gs_name(self):
        return self.name

    @gs_name.setter
    def gs_name(self, name):
        self.name = name

    @gs_name.deleter
    def gs_name(self):
        self.name = None
        print('DELETE name!')


class Tail(Head):
    def __init__(self, name, age, dob):
        super().__init__(name, age)
        self.dob = dob

    @property
    def gs_age(self):
        return self.age

    @gs_age.setter
    def gs_age(self, age):
        self.age = age


hh = Head('DVS', 15)
hh.gs_name = 'Durgai'
print(hh.gs_name)
print(hh.h)
# HH = Head('DVS', 20)
# TT = Tail('Durgai', 20, '03/09/2001')
# print(isinstance(TT, Tail))
# print(issubclass(Tail, Head))
# print(TT.gs_name())
