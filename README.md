# CPSC525: CWE-502 Demo
A simple example of exploiting CWE-502 in Python using the pickle serialization library.

[CWE-502](https://cwe.mitre.org/data/definitions/502.html)

### Idea
*Note*: This is a work in progress and will be changed to be a more interesting attack.
 - `server.py` runs a server that listens for `client.py` connections.
 - `client.py` simply asks you for a username before pickling a `user.User` object to send it to the open server.
 - `server.py` expects a `user.User` object, unpickles it and calls `user.User.username` to print a connection message.

**The Vulnerability**:
 - As the server does zero validation on the received pickled object before unpickling it, it is very vulnerable to CWE-502.
 - If you instead run `evil_client.py`, this will connect to the open server and send an `EvilUser`.
 - This `EvilUser` currently does nothing but open a python shell on the running server. *This will need to be changed to do something cool instead*

### Sources:
https://realpython.com/python-pickle-module/

https://realpython.com/python-sockets/

https://davidhamann.de/2020/04/05/exploiting-python-pickle/
