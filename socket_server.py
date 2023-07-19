#!/usr/bin/python3
# -*- coding:utf-8 -*-

# Author   : JasonHung
# Date     : 20230220
# Update   : 20230302
# Function : Tinfar test socket server

import  socket

host = '0.0.0.0'
port = 7000

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
s.bind((host, port))
s.listen(1)

print('Server start : ' + str(host) + ' , port ' + str(port))
print('wait for conenction...')

while True:
    conn , addr = s.accept()
    print('connection by ' + str(addr))

    indata = conn.recv(1024)
    print('recv : ' + indata.decode("utf-8"))

    outdata = 'echo ' + indata.decode("utf-8")
    conn.send(outdata.encode("utf-8"))
    conn.close()






