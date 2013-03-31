#!/usr/bin/python
# -*- coding: utf-8 -*
from misc import isNaN
from sys import argv
import bluetooth
from socket import *                    # get socket constructor and constants
import numpy as np


############################################################################
# Conatins functions for Communication

# bserver:bluetooth server
# bclient_for_train:bluetooth client intented to send file from own machine
# tcp_server :tcp_server for communication via internet or Wifi
# main :funcion to simply integrate these
##########################################################################
def bserver():	
	server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	port = bluetooth.PORT_ANY 
	server_sock.bind(("",port))
	print server_sock.getsockname() ,'is listening '
	server_sock.listen(1)
	client_sock,address = server_sock.accept()
	data=[]
	try:
		line=client_sock.recv(1024)
		while(line.strip() != 'start'):
			line=client_sock.recv(1024)
		while True:
			line = client_sock.recv(1024)
			if len(data) == 0: break
			for val in line.split(' '):
				if not isNaN(val):
					data.append(float(val))
		data=np.reshape(data,[-1,3])

	except IOError:
		pass

	print "disconnected"
	client_sock.close()
	server_sock.close()
	return data
def bclient():
	bd_addr = "00:1B:10:00:2A:EC"
	port = 1
	sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	sock.connect((bd_addr, port))
	sock.send("hello!!")
	sock.close()

def bclient_for_train(filename):
  	bd_addr = "00:1B:10:00:2A:EC"
	port = 10
	sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	sock.connect((bd_addr, port))
	fin=open(filename)
	sock.send('start')
	for line in fin:
		sock.send(line)
	sock.send('Quit')
	
	sock.close()


def tcp_server():
	#"""For Wifi Communiction the client may use  the name sarath as server address"""
	myHost = '10.42.0.22'                             # server machine, '' means local host
	local=''
	myPort = 3001                          # listen on a non-reserved port number
	sockobj = socket(AF_INET, SOCK_STREAM)      
	try:
		sockobj.bind((myHost, myPort))               
	except:
		print 'not possible at remote'
		sockobj.bind((local,myPort))	
	sockobj.listen(1)    
	print 'listening on tcp',str(sockobj)
	data=[]                       
	try:
		connection, address = sockobj.accept()  
		print 'Server connected by', address
		connection.recv(1024)
		connection.send(open('Communication.py').read())
		try:
			line=connection.recv(1024)
			while 'start' not in line.strip():
				line=connection.recv(1024)
               		while True:
                       		line = connection.recv(1024)
				if 'end' in line.strip():
                      			break
                    		else:
                       			for val in line.split(' '):
                       				if not isNaN(val):
                           				data.append(float(val))
                	data=np.reshape(data,[-1,3])
        	except IOError:
               		print 'Exception inside '
			print 'trying to close'
		connection.close()
		print 'Connection closed'
	except :
		print 'Exception out'
	finally:
		return data

def main():
	if argv[1] == 'bserver':
        	bserver()
	elif argv[1] == 'bclient':
        	bclient()
	else:
		tcp_server()

	"""
	The server is started once the function is called and goes on listening 
	when a bluetooth request is there at the specified port
	it will start reading data frm it and will store it into a 3dimensioanal array
	then return the data as a n*3 matrix
	"""
if __name__ == "__main__":
	main()
