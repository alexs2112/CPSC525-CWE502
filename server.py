import socket, pickle, user

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    print(f"Server is listening on {(HOST, PORT)}")

    # Wait for incoming connection
    conn, addr = sock.accept()
    with conn:
        print(f"Connected to {addr}.")

        # 4 bytes to tell us the length of the expected message
        len = int.from_bytes(conn.recv(4), "little")
        print(f"Length of Message: {len}")

        data = conn.recv(len)

# Load the received object, expect it to be of type user.User
obj = pickle.loads(data)
print(f"Received new user {obj.username}.")
