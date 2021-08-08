"""
To fix these issues, we could make use of super().
Call to super will make sure that every method in MRO (method resolution order) is called only once.
MRO is the order that superclasses are initialized. Can be accessed with class.__mro__ or class.mro().
"""


class Base:
    def __init__(self, value):
        print("Base constructor call")
        self.value = value


class TimesTwo(Base):
    def __init__(self, value):
        print("TimesTwo constructor call")
        super().__init__(value)
        self.value *= 2


class PlusFive(Base):
    def __init__(self, value):
        print("PlusFive constructor call")
        super().__init__(value)
        self.value += 5


class Calculation(TimesTwo, PlusFive):
    def __init__(self, value):
        super().__init__(value)


print(*(klass.__name__ for klass in Calculation.mro()), sep=" --> ")  # MRO

calculation = Calculation(6)  # according to MRO, value should be (6 + 5) * 2 = 22
print(calculation.value)
