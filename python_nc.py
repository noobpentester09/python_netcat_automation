#!/usr/bin/python
import socket
ip = raw_input("Enter the ip adress")
port = input("Enter the port number")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if s.connect_ex((ip , port)):
    print "The port %s is closed" %port
else:
    print "The port %s is open" %port


