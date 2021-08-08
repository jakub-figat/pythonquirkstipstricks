"""
We would expect empty list as a default argument to be initialized for every function call,
Instead, the object is initialized once and every function call accesses the same instance.
This strange behavior can lead to nasty bugs and happens everytime we pass a
mutable object as a default argument
"""


def append_to_list(element, _list=[]):
    _list.append(element)
    return _list


new_list_1 = []
new_list_1 = append_to_list(1, new_list_1)
new_list_1 = append_to_list(2, new_list_1)
print(new_list_1)  # [1, 2], as expected

new_list_2 = append_to_list(5)
new_list_2 = append_to_list(6, new_list_2)
print(new_list_2)  # [5, 6], as expected

new_list_3 = append_to_list(10)
new_list_3 = append_to_list(20, new_list_3)
print(new_list_3)  # we would expect [10, 20], but instead something weird is happening...


"""
Unfortunately, the same thing happens with classes
"""


class DictContainer:
    def __init__(self, _dict={}):
        self.dict = _dict


container_1 = DictContainer()
container_2 = DictContainer()

container_1.dict["key"] = "value"
print(container_2.dict)  # we would expect it to be {}
