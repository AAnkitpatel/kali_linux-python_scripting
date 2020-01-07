import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 12000))
sock.listen(2)
conn, addr = sock.accept()
data = conn.recv(1024).decode("ascii")
