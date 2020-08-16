import socket

HEADERSIZE = 10


# SOCKET_HOST = socket.gethostname()
SOCKET_HOST = "server"
SOCKET_PORT = 1234


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SOCKET_HOST, SOCKET_PORT))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg.decode("utf-8")

        print(len(full_msg))


        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ""