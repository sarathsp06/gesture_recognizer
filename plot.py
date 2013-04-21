#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 07:36:55 2013

@author: sarath
"""
def plot_all(nxdata,nydata,nzdata,xdata=0,ydata=0,zdata=0):
	print nxdata
	from pylab import plot,subplot,show,xlabel,title,grid
	nc=1
	if type(xdata) is not int:
		nc=2
	if nc is 2:
		subplot(3,2,2)
		plot(xdata,ydata,'*')
		xlabel('XvsY-DATA')
		subplot(3,2,4)
		plot(ydata,xdata,'*')
		xlabel('YvsX-DATA')
		subplot(3,2,6)
		plot(zdata)
		xlabel('Z-DATA')
	i=1
	subplot(3,nc,i)
	title("ploting X vs Y")
	grid(True)
	plot(nxdata,nydata)
	xlabel('X vs Y')
	subplot(3,nc,i+nc)
	grid(True)	
	plot(nydata,nxdata)
	xlabel('YvsX')
	subplot(3,nc,i+2*nc)
	grid(True)	
	plot(nzdata,nxdata)
	xlabel('Z vs X')
	grid(True)
	show()

def plot_3d(nxdata,nydata,nzdata,label="#d-representation"):
	import matplotlib as mpl
	from pylab import figure,show
	from mpl_toolkits.mplot3d import Axes3D
	mpl.rcParams['legend.fontsize'] = 10
	fig = figure()
	ax = fig.gca(projection='3d')
	ax.plot(nxdata, nydata, nzdata, label='3D Representation of th edata')
	ax.legend()
	show()




