#!/usr/bin/python
# -*- coding: utf-8 -*-
from numpy import fft,array
###################################################################
# contins functions for filtering
# ffilter :input data and cut freequency return data after filtering
# 		the ffilter here is working on fft of data
# filter_xyz :it filters all the xyz values of the table
# 		using the function ffilter
##################################################################
def ffilter(data,cut):
	i=0
	for i in range(len(data)):
		if i >= cut :
			data[i]=0
		
	return data

	
def filter_xyz(data): 
	xdata=[a[0] for a in data]
	ydata=[a[1] for a in data]
	zdata=[a[2] for a in data]
	samples=len(ydata)
	xdata=array(xdata)
	ydata=array(ydata)
	zdata=array(zdata)
	try:
#----------------------------------
		xfft=(fft.rfft(xdata))
		yfft=(fft.rfft(ydata))
		zfft=(fft.rfft(zdata))
	

#-------------filtering part --------------
		cutoff=samples/3*2
		xfft=ffilter(xfft,cutoff)	
		yfft=ffilter(yfft,cutoff)
		zfft=ffilter(zfft,cutoff)

		nxdata=fft.irfft(xfft)	
		nydata=fft.irfft(yfft)
		nzdata=fft.irfft(zfft)
	except:
		raise ValueError('null value')
	size=len(nxdata)
	data=[[nxdata[i],nydata[i],nzdata[i]] for i in range(size)]
	return data
    
    
