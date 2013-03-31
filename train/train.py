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

# Create network with 2 layers and random initialized
#norm = Norm(input)
#input = norm(input)
print input.shape
print target.shape
print '----------',minmax(input)
net = nl.net.newff(minmax(input), [12, 4], transf = [nl.trans.TanSig(), nl.trans.LogSig()])
net.trainf = nl.train.train_bfgs
error = net.train(input, target, epochs=1000, show=10, goal=0.02)
print '-------',error[-1]
net.save('net.net')
#Simulate network
print '\nprinting the simulated output';
net=nl.load('net.net')
output = net.sim(input)
out = output
for i in range(len(output)):
	m=max(output[i])
	print '[',m,']',
	for j in range(4):
		if output[i,j] == m:
			print j+1,
	print ';;',target[i]
net.save('net.net')
