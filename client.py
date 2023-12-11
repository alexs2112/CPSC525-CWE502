import socket, pickle, user

HOST = "127.0.0.1"
PORT = 12345

print("Hello, what is your username?")
username = input(">>> ")
user = user.User(username)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    
    # Send the length of the object, and then the object as a list of bytes
    obj = pickle.dumps(user)
    print(f"Length of object: {str(len(obj))}")
    sock.sendall(len(obj).to_bytes(4, "little"))
    sock.sendall(obj)
