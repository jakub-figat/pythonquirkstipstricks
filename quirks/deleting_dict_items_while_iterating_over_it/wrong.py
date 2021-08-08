import string

"""
Similar to previous example, deleting items from dict while iterating over will end up
in even nastier result, the RuntimeError.
"""

#  {"a": 1, "b": 2, ...}
alphabet_dict = {
    letter: index + 1
    for index, letter in enumerate(string.ascii_lowercase)
}


for element in alphabet_dict:
    del alphabet_dict[element]


"""
The solution is iterating over the copy of keys
"""

#  copy of keys()
for element in list(alphabet_dict.keys()):
    del alphabet_dict[element]

print(alphabet_dict, "iterating over keys() copy")

