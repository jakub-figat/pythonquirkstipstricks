"""
You should override collections.abc objects
if you want to define custom collections based on built-in ones
"""

from collections.abc import MutableMapping


class CustomDict(MutableMapping):
    """
    Custom dict class with overridden __getitem__ method, so it prints message
    on every key access
    """
    def __init__(self, *args, **kwargs):
        self.dict = dict()
        self.update(dict(*args, **kwargs))

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __delitem__(self, key):
        del self.dict[key]

    def __getitem__(self, key):
        print(f"Key {key} is accessed")
        return self.dict[key]

    def __len__(self) -> int:
        return len(self.dict)

    def __iter__(self):
        return iter(dict)

    def __str__(self):
        return dict.__str__(self.dict)


custom_dict = CustomDict()
custom_dict["a"] = 2
custom_dict["b"] = 3

print(custom_dict["a"])
print(custom_dict["zxdkjaskjd"])