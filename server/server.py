import socket
import time


HEADERSIZE = 10

SOCKET_HOST = socket.gethostname()
SOCKET_PORT = 1234

print("Running socket ar {}:{}".format(SOCKET_HOST, SOCKET_PORT))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SOCKET_HOST, SOCKET_PORT))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADERSIZE}}"+msg

    clientsocket.send(bytes(msg,"utf-8"))

    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}"+msg

        print(msg)

        clientsocket.send(bytes(msg,"utf-8"))