#!/usr/bin/python
# -*- coding: utf-8 -*-
# quitbutton.py
import sys,os
from PyQt4 import QtGui, QtCore
def call_train():
	os.system('./pro.py train')
def call_test():
	os.system('./pro.py run')

class main_window(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
        	self.setGeometry(0, 0,760,120)
		self.setWindowTitle('Project')
		self.Train = QtGui.QPushButton('Train', self)
		self.Simulate = QtGui.QPushButton('Simulate',self)
		self.layout=QtGui.QGridLayout();
		self.layout.addWidget(self.Train,4,1)
		self.layout.addWidget(self.Simulate,4,2)
		self.layout.setSpacing(10)
		self.setLayout(self.layout)
		self.connect(self.Simulate,QtCore.SIGNAL('clicked()'),call_test)
		self.connect(self.Train, QtCore.SIGNAL('clicked()'),call_train)
app = QtGui.QApplication(sys.argv)
window = main_window()
window.show()
sys.exit(app.exec_())

