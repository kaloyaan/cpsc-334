import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
s.bind(('172.29.32.254', 8090))
s.listen(0)

while True:
    print("Listening..")
    client, addr = s.accept()

    while True:
        print(".")
        content = client.recv(2048)
        print(content)
        content = 0
    client.close()
