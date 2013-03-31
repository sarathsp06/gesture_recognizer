#!/usr/bin/python
# -*- coding: utf-8 -*-
from numpy import reshape,asfarray
from os import system,chdir
from acquire import get_train_data
from misc import shape_dict ,print_array
import neurolab as nl
import cPickle
################################################
# Functions to do the ann operations
# train :trains a set of data from the folder 'Shape'
#         and train on them
# simulate :simulate a input as given in input
################################################
def train(): 
    input,target=get_train_data();  
    input=reshape(input,(-1,42))/10
    er=len(input)
    while er > len(input)/20:
        er=0;
        net = nl.net.newff(nl.tool.minmax(input), [12, 4], transf = [nl.trans.TanSig(), nl.trans.LogSig()])
        net.trainf = nl.train.train_bfgs   
        error = net.train(input, target, epochs=1000, show=10, goal=0.01)
        output = net.sim(input)
        out=[[0 for i in range(4)] for j in range(len(output))]
        for i in range(len(output)):
            m=max(output[i])
            for j in range(4):
                if output[i,j] == m:
                    out[i][j] =1
            if out[i] != target[i]:
                er+=1
        print 'Error :',er
    print len(target),er
    chdir('/home/sarath/gesture/my_part')
    cPickle.dump(net,open('net.net','w')) 

def test():
    input,target=get_train_data();
    input=reshape(input,(-1,42))/10
    chdir('/home/sarath/gesture/my_part')
    net=cPickle.load(open('net.net','r'))
    output = net.sim(input)
    #after gettig the simulated data checking how well it works
    err=0
    out=[[0 for i in range(4)] for j in range(len(output))]
    for i in range(len(output)):
        m=max(output[i])
        for j in range(4):
            if output[i,j] == m:
                out[i][j] =1
        print out[i] == target[i]

def simulate(input):
    chdir('/home/sarath/gesture/my_part')
    net=cPickle.load(open('net.net','r'))
    shape=shape_dict()
    in_put=[]
    for i in input:
        in_put.extend(i)
    try:
        out=tuple(net.sim([in_put])[0])
    except:
        print 'simulation error'
        return
    out=list(out)
    print 'out as  list'
    print out
    for i in range(4):
        if i == out.index(max(out)):
            out[i]=1
        else:
            out[i]=0
    out=out.index(1)
    print out
       

    if out == shape['T'].index(1):
        gesture="Triangle"
    elif out == shape['R'].index(1):
        gesture = 'Rectangle'
    elif out == shape['L'].index(1):
        gesture = 'Line'
    elif out == shape['C'].index(1):
        gesture = 'circle'
    else :
        gesture='not defined'
    


    out="notify-send 'the figure is %s '" % (gesture)
    print out
    system(out)
