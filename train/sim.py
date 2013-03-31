#!/usr/bin/python
import neurolab as nl
import numpy as np
import input
import target
from neurolab.tool import minmax

# Create train samples
input = np.array(input.data)
target = np.asfarray(target.data)
input = input[: target.shape[0]]
net=nl.load('net.net')
output = net.sim(input)
err=0
for i in range(len(output)):
	m=max(output[i])
	for j in range(4):
		if output[i,j] == m:
			if target[i][j] == 0:
				err+=1
print len(target),err
