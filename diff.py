# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:11:47 2019

@author: wahaj
"""
import numpy as np

deltax = 0.00000001
def getnewy(x, y):
    return y + deltax*y

y = 1
x = 0
x_target  = int (input("enter x value:"))

for x in np.arange(0, x_target, deltax):
    y=getnewy(x,y)
    
print ("e^%s is (approximately) equal to %s" % (x_target, y))
