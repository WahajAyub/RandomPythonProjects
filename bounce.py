# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:47:34 2019

@author: wahaj
5"""
import numpy as np
import math

class Box:
    def __init__(self, mass, width, velocity, x):
        self.m = mass
        self.w = width
        self.v = velocity
        self.x = x
    
    def checkCollision (self, other):
        if ((self.x + self.w) >= other.x):
            return True
        else:
            return False
        
    def checkWallCollision (self):
        if (self.x <= 0):
            return True
        else:
            return False
    
    def updatePosition (self):
        self.x += self.v
#        print (self.x)
    
    def updateVelocity (self, other):
        newv1 = ((self.m - other.m)*self.v + (2*other.m)*other.v)/(self.m+other.m)
        newv2 = ((2*self.m)*self.v + (other.m - self.m)*other.v)/(self.m+other.m)
        self.v = newv1
        other.v = newv2
#        print("v", self.v)
#        print("v2", other.v)
    
    def reverseVelocity (self):
        self.v *= -1
    
    def checkIfFinalCollision (self, other):
#        print ("v1 {} v2 {}".format(self.v, other.v))
        if self.v >= 0:
            if other.v > self.v:
                return True
            else:
                return False
        else:
            return False


counter = 0

digits = int (input ("Enter Number of Digits: "))
timesteps = 100
a = Box(1, 20, 0, 100)
mb = math.pow(100, (digits-1))
b = Box((mb), 100, (-5/timesteps), 200)


while (True):
    a.updatePosition()
    b.updatePosition()
    if (a.checkCollision(b)):
        a.updateVelocity(b)
        counter += 1
        if (a.checkIfFinalCollision(b)):
            break
    if (a.checkWallCollision()):
        a.reverseVelocity()
        counter += 1
        if (a.checkIfFinalCollision(b)):
            break
#    print (counter)
print ("collisions", counter)
piestimate = counter/(math.pow(10, (digits-1)))
print ("pi is approximately equal to {}".format(piestimate))
