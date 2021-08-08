"""
Avoid deleting items from list while iterating over it
"""


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]


for number in list_of_numbers:
    list_of_numbers.remove(number)


print(list_of_numbers, "remove() while iterating")  # we expect []

"""
This is what really happens:
1. We start iterating over the list, the first item we get is 1.
2. We call remove method on list, so 1 gets deleted.
3. Before list[1] element is accessed, every element is shifted to the left,
since list[0] got deleted.
4. After that operation the list is [2, 3, 4, 5, 6, 7, 8], now we're moving to the 
list[1], which in that case is 3, instead of 2. This continues and we end up with
buggy functionality
"""


"""
What is interesting, using del keyword instead of remove() method
gives different results, but still it's mismatched behavior
"""

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for number in list_of_numbers:
    del number

print(list_of_numbers, "using del")  # we expect []


"""
The reason is that del deletes object only from local namespace,
not from the global namespace, therefore list_of_numbers remains unaffected,
while only number variable of type int is deleted.
"""
