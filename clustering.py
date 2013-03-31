#!/usr/bin/python
# -*- coding: utf-8 -*-
from scipy.cluster.vq import whiten,kmeans2
from numpy import reshape		
#######################################################
# Function to do clustering on set of data
# cluster :it returns c_num clusters from the input vals
# 		the algorithm used here is kmeans algorithm
#########################################################
def kcluster(vals,c_num):
	vals=reshape(vals,(-1,3))
	whiten(vals)
	l,label=kmeans2(vals,14,iter=40)
	return l

def cluster(vals ,c_num):
	vals=reshape(vals,(-1,3))
	try:
		whiten(vals)
	except Exception,e:
		print 'Exception at \'whiten \'\n'+e.message
	diff=float(len(vals))/c_num;
	arr=[vals[int(i*diff)] for i in range(c_num)]
	arr=reshape(arr,(-1,3))
	try:
		l,labels=kmeans2(vals,arr,iter=40)
	except Exception, e:
		print e.message
		raise e
	
	return l