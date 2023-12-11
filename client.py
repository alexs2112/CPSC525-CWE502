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

    while True:
        r = input(">>> ")
        data = r.encode("utf-8")

        # Send the length of the data and the data itself to the server
        sock.sendall(len(data).to_bytes(4, "little"))
        sock.sendall(data)

        # Receive the same data echoed back to the client
        data = sock.recv(len(data))
        if not data:
            print("Server connection is closed")
            break
        print(data.decode('utf-8'))
