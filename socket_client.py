#!/usr/bin/python3
# -*- coding:utf-8 -*-

# Author   : JasonHung
# Date     : 20230220
# Update   : 20230302
# Function : Tinfar test socket server

import  socket

host = '0.0.0.0'
port = 7000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))

outdata = 'Hello tcp'
print('send : ' + outdata)
s.sendall(outdata.encode("utf-8"))

indata = s.recv(1024)
print('recv : ' + indata.decode("utf-8"))

s.close()

