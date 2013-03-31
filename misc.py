#!/usr/bin/python
# -*- coding: utf-8 -*
"""
###############################################################
# this module contains all the functions
# that are usefull in all the files which 
# does not have any special purpose
#
#
# isNaN --check if its NotaNumber
# shape_dict--returns a dictinary 
# rename_for_Shapes :rename all the files in the folder Shapes
# log_to_files : it extracts the log file into text files for 
################################################################
"""
import os

def isNaN(x):
    try: 
    	float(x)
    except ValueError:
    	return True
    return False
def shape_dict():
	return {'T':[1,0,0,0],'C':[0,1,0,0],'R':[0,0,1,0],'L':[0,0,0,1]}

def rename_for_Shapes():
	j=0
	for i in os.listdir('.'):
		os.rename(i,i.capitalize()[0]+str(j)+".txt")
		j+=1
def clrscr():
	from os import system
	system('clear;clear;clear')
        
def log_to_files(filename):
	from os import chdir,listdir, path
	fin=open(filename)
	chdir('/home/sarath/gesture/my_part/Shapes')
	F=path.basename(filename)[0]
	j=len(listdir('.'))
	fout=open(F+str(j)+'.txt','w')
	for i in fin:
		if 'end' in i:
			j+=1
			fout=open(F+str(j)+'.txt','w')
		else:
			fout.write(i)
	chdir('..')

def print_array(array):
	print array

