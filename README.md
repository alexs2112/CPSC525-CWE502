# CPSC525: CWE-502 Demo
A simple example of exploiting CWE-502 in Python using the pickle serialization library.

[CWE-502](https://cwe.mitre.org/data/definitions/502.html)

### Idea
*Note*: This is a work in progress and will be changed to be a more interesting attack.
 - `server.py` runs a server that listens for `client.py` connections.
 - `client.py` simply asks you for a username before pickling a `user.User` object to send it to the open server.
 - `server.py` expects a `user.User` object, unpickles it and calls `user.User.username` to print a connection message.
```
C:\CWE502>python client.py
Hello, what is your username?
>>> Alex
Length of object: 53
```
```
C:\CWE502>python server.py
Server is listening on ('127.0.0.1', 12345)
Connected to ('127.0.0.1', 55844).
Length of Message: 53
Received new user Alex.
```

**The Vulnerability**:
 - As the server does zero validation on the received pickled object before unpickling it, it is very vulnerable to CWE-502.
 - If you instead run `evil_client.py`, this will connect to the open server and send an `EvilUser`.
 - This `EvilUser` currently does nothing but open a python shell on the running server. *This will need to be changed to do something cool instead*

```
C:\CWE502>python evil_client.py
Length of object: 41
```
```
C:\CWE502>python server.py
Server is listening on ('127.0.0.1', 12345)
Connected to ('127.0.0.1', 55846).
Length of Message: 41
Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Sources:
https://realpython.com/python-pickle-module/

https://realpython.com/python-sockets/

https://davidhamann.de/2020/04/05/exploiting-python-pickle/
