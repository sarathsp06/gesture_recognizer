#!/usr/bin/python
# -*- coding: utf-8 -*
import numpy as np
from  Communication import bserver,tcp_server
from misc import isNaN,shape_dict
######################################################
# This module contains all the functions for getting data
# 
# getdata_file :read data from the specific file
# getdata_b :start bluetooth server and getdata
# getdata_tcp :get data via WiFi or internet
# get_train_data :get data for training which may return
# 			the input and target as out put
######################################################

def getdata_file(a):
    from os import getcwd,chdir,path
    input=open(a)
    if path.basename(getcwd()) != 'Shapes':
    	chdir('Shapes')
    data=[]
    for line in input:
        line=line[0:line.find('\n')]
        for val in line.split(' '):
             if not isNaN(val):
                 data.append(float(val))
    data=np.reshape(data,[-1,3])
    data[:,1]=data[:,1]-9.8
    data[:,2]= 1
    return data
    
#read data from bluwtooth instead of  file
def getdata_b():
	data=[]
	try:
		data=bserver()
	except:
		data=[0,0,0]
	finally:
        	return data

#getdata via tcp
def getdata_tcp():
	data=[]
	try:
		data=tcp_server()
	except:
		data=[0,0,0]
	finally:
        	return data
########################################################
# the data will be send to the calling function as
# two list of data one indicating the input
# while thw other is indicating the output target
# input n*14 and output n
#######################################################
def get_train_data():
	from os  import listdir,chdir,remove,rename
	from filtering import filter_xyz
	from clustering import cluster
	table=shape_dict()
	in_put=[]
	target=[]
	chdir('./Shapes')
	for i in listdir('.'):
		try:
			
			data=getdata_file(i)
			data=filter_xyz(data)
			data14=cluster(data,14);
			in_put.append(data14)
			target.append(table[i[0]])
		except:
			print '\t\t\tERROR in file ',i,'removing ',i
 			remove(i)
			pass
	chdir('..')
	return in_put,target	
