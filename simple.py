import pickle

class GoodClass:
    def foo(self):
        print("Hello (affectionate)")

class MaliciousClass:
    def foo(self):
        print("Hello (derogatory)")

yeet = GoodClass()
p = pickle.dumps(yeet)

# Inject our own malicious class somehow
yeet2 = MaliciousClass()
p = pickle.dumps(yeet2)

# Expect GoodClass and calls foo() on it
heeg = pickle.loads(p)
heeg.foo()
