"""
A fix to this problem is iterating over the copy of the original iterable.
"""

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]


for number in list_of_numbers[:]:  # copy of the list
    list_of_numbers.remove(number)


print(list_of_numbers, "iterating over copy")  # [], as expected

"""
Or we can just use list comprehension if the delete happens on condition
"""

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_list_of_numbers = [number for number in list_of_numbers if number % 2 == 0]

print(even_list_of_numbers)
