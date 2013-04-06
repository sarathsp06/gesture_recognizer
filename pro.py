#!/usr/bin/python
# -*- coding: utf-8 -*-
from clustering import cluster
from acquire import getdata_file,getdata_b,getdata_tcp
from sys import argv
from ann import train,simulate,test
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
	mode='tcp'
	data=[]	
	if len(argv) == 4	:
		mode=argv[2]
	if mode == 'tcp':
		getdata = getdata_tcp
	else :
		getdata = getdata_b
	if t == 'test':
		if len(argv) == 2:
			test()
		else:
			fname=argv[3]
			data=getdata_file(fname)
			data=filter_xyz(data)
			data14=cluster(data,14);
			simulate(data14);	
	elif t == 'train':
		train()
			
	else:
		while(True):
			data=getdata()
			data=filter_xyz()
			data14=cluster(data,14)
			simulate(data14)
                 
if __name__ == "__main__":
	try:
		main_()
	except Exception, e:
		print "Exception :",e.message

