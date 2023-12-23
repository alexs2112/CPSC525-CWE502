# CPSC525: CWE-502 Demo
A simple example of exploiting CWE-502 in Python using the pickle serialization library.

[CWE-502](https://cwe.mitre.org/data/definitions/502.html)

### How To Run
 - On one terminal: `python3 server.py`
 - On another terminal: `python3 client.py`
 - If you instead run `python3 evil_client.py` then malicious serialized data is sent to the server. This will cause "malware" to be curled to the box.

### Idea
 - `server.py` runs a server that listens for `client.py` connections.
 - `client.py` asks you for a username before pickling a `user.User` object to send it to the open server. It then turns into a basic echo client that repeats what you tell it.
 - `server.py` expects a `user.User` object, unpickles it and calls `user.User.username` to print a connection message. It then echoes all messages sent from the client.
```
.../project$ python client.py
Hello, what is your username?
>>> Alex
Length of object: 53
>>> Hello
Hello
>>> Yeet
Yeet
```
```
.../project$ python server.py
Server is listening on ('127.0.0.1', 12345)
Connected to ('127.0.0.1', 55844).
Length of Message: 53
Received new user Alex.
[recv] Hello
[recv] Yeet
```

**The Vulnerability**:
 - As the server does zero validation on the received pickled object before unpickling it, it is very vulnerable to CWE-502.
 - If you instead run `evil_client.py`, this will connect to the open server and send an `EvilUser`.
 - This `EvilUser` calls a `curl` command to install very potent malware onto the server. This is present in [malware.txt](malware/malware.txt) (WARNING: Open at own risk)
```
.../project$ python3 evil_client.py
Length of object: 190
```
```
.../project$ python server.py
Server is listening on ('127.0.0.1', 12345)
Connected to ('127.0.0.1', 54004).
Length of Message: 190

you just got hacked!

.../project$ ll | grep malware
-rw-r--r--  1 <...> <...>   14 Dec 11 11:08 malware.txt
```

### Sources:
https://realpython.com/python-pickle-module/

https://realpython.com/python-sockets/

https://davidhamann.de/2020/04/05/exploiting-python-pickle/
