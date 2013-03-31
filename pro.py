#!/usr/bin/python
# -*- coding: utf-8 -*-
from clustering import cluster
from acquire import getdata_file,getdata_b,getdata_tcp
from sys import argv
from ann import train,simulate
from filtering import filter_xyz
#############################################################
#main function here is to call deferent functions each for
#training or for the purpose of running it 
#
#command line arguements
#	1.tarin or simulate
#	2.if train then filename
#	3.if simulate tcp or bluetooth
###############################################################
def main_():
	if len(argv) < 2:
		print 'The input format is\nmain train/test   [tcp/b] [filename]'
		return 0
	t=argv[1]
	mode='b'
	data=[]	
	if len(argv) == 4	:
		mode=argv[2]
	if t == 'test':
		if mode == 'b':
			data=getdata_b()
		elif mode == 'tcp':
			data=getdata_tcp()
		else:
			data=getdata_file(argv[3])
		data=filter_xyz(data)
		data14=cluster(data,14);
		simulate(data14);
	elif t == 'train':
		train()
	else:
		while(True):
			data=getdata_tcp()
			data=filter_xyz()
			data14=cluster(data,14)
			simulate(data14)
                 
if __name__ == "__main__":
	try:
		main_()
	except Exception, e:
		print e.message()

