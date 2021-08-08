"""
If we want to check whether the variable type is bool or not, we can get into trouble
"""

true = True
false = False

one = 1
zero = 0

print(isinstance(true, bool))  # these two make sense
print(isinstance(false, bool))

print(isinstance(true, int))  # we expect it to be false

print(true == one)  # this one is interesting too
