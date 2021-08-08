import json


"""
Typically, we define a class before runtime, using class keyword.
But there's also possibility to define classes at runtime,
using type(class_name, subclasses, namespace) built-in function.
Suppose we want to dynamically define a class with constants as class attributes, based on some external file.
"""

with open("constants.json", mode="r") as json_file:
    constants = json.load(json_file)

constants = {key.upper(): value for key, value in constants.items()}

SpeedConstants = type("SpeedConstants", (), constants)

print(SpeedConstants.__dict__.get("SPEED_OF_LIGHT"))
print(SpeedConstants.__dict__.get("SPEED_OF_SOUND_IN_AIR"))
