"""
Python allows multiple inheritance, but this feature should be used with extra care,
especially when dealing with diamond inheritance.
Diamond inheritance occurs when a class subclasses two classes that have one common superclass
somewhere in hierarchy.
Suppose we have given class hierarchy:
"""


class Base:
    def __init__(self, value):
        print("Base constructor call")
        self.value = value


class TimesTwo(Base):
    def __init__(self, value):
        print("TimesTwo constructor call")
        Base.__init__(self, value)
        self.value *= 2


class PlusFive(Base):
    def __init__(self, value):
        print("PlusFive constructor call")
        Base.__init__(self, value)
        self.value += 5


class Calculation(TimesTwo, PlusFive):
    def __init__(self, value):
        TimesTwo.__init__(self, value)
        PlusFive.__init__(self, value)


calculation = Calculation(6)  # value should be 6 * 2 + 5 = 17
print(calculation.value)  # but what really happened is 6 + 5 = 11

