# Instead serialize our objects as a different format
# JSON or XML are commonly used formats
# They are more limited than a byte stream, but prevent arbitrary code
# execution
import json

# Define the same two classes as in insecure.py
class GoodClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def foo(self):
        print(f"Hello, my name is {self.name}. I am {str(self.age)} years old.")

class MaliciousClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def foo(self):
        print("You have been hacked. Give us $1000000 to become unhacked.")

# Create our own serialization function, that converts what we want to
# persist into json
def serialize(obj):
    d = { "name": obj.name, "age": obj.age }
    return json.dumps(d)

# Create our own deserialization method, that converts a json string into
# a GoodClass object
def deserialize(serialized):
    d = json.loads(serialized)
    return GoodClass(d["name"], d["age"])

# Serialize and deserialize using json instead of a byte stream
obj = GoodClass("Mocha", 99)
serialized = serialize(obj)
deserialized = deserialize(serialized)
deserialized.foo()
# Hello, my name is Mocha. I am 99 years old.

obj = MaliciousClass("Bad Actor", -1)
serialized = serialize(obj)
deserialized = deserialize(serialized)
deserialized.foo()
# Hello, my name is Bad Actor. I am -1 years old.
