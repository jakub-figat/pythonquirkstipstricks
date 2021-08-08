"""
To avoid this, we can set default argument to None, and then instantiate object
in the function scope
"""


def append_to_list_fixed(element, _list=None):
    if _list is None:
        _list = []

    _list.append(element)
    return _list


new_list_1 = []
new_list_1 = append_to_list_fixed(1, new_list_1)
new_list_1 = append_to_list_fixed(2, new_list_1)
print(new_list_1)  # [1, 2], as expected

new_list_2 = append_to_list_fixed(5)
new_list_2 = append_to_list_fixed(6, new_list_2)
print(new_list_2)  # [5, 6], as expected

new_list_3 = append_to_list_fixed(10)
new_list_3 = append_to_list_fixed(20, new_list_3)
print(new_list_3)  # [10, 20], finally as expected
