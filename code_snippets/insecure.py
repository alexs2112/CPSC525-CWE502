# The python pickle module serializes objects by converting the entire thing
# to a byte stream, methods and all
# This is a common serialization method and is a prime example of CWE-502
import pickle

# Define two classes with the same method name that will be deserialized
class GoodClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def foo(self):
        print(f"Hello, my name is {self.name}. I am {str(self.age)} years old.")

class MaliciousClass:
    def foo(self):
        print("You have been hacked. Give us $1000000 to become unhacked.")

# Instantiate the expected class
obj = GoodClass("Mocha", 99)

# Somehow inject a serialized copy of the malicious class to be serialized
obj = MaliciousClass()

# Serialize obj, this is now the malicious class and not the expected one
serialized = pickle.dumps(obj)

# Expect an instance of GoodClass, call foo() on it without validation
deserialized = pickle.loads(serialized)
deserialized.foo()
# You have been hacked. Give us $1000000 to become unhacked.
