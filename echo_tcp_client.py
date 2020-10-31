import socket
import sys

HOST, APPLICATION_PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, APPLICATION_PORT))

    s.sendall(bytes(data, "utf-8"))
    print("sent:     " + data)

    received = str(s.recv(10000), "utf-8")
    print("received: " + received)