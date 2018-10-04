#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:08:17 2018

@author: test
"""

import numpy as np
import matplotlib.pyplot as plt

C=1.0
I=1.0

dt=0.01

I = 2

Vth = 1

Vreset = 0

Vrest = 0.2

V = np.zeros([1000,1])

V[0]=0.2

R = [0.5,1.5]

nI = [2,4,6,8,10]


#define all of your variables
for nR in R:
    Vstar = Vrest + (I*nR)
    T = nR*C
    for k in range(1,999):
        V[k+1] = V[k] + dt*(-(V[k] - Vstar) / T)
        if V[k+1] > Vth:
            V[k+1] = Vreset
        
#Change/write your equation that demonstrates LIF
#V[k+1] is the voltage in the future
#V[k] is the voltage now
#the only thing that needs to change is the equation that is multiplied by dt
#can then go back and forth from the LIF and IF with some additional variable changes
        
    t = np.arange(0,len(V))*dt
    
    #plt.figure()     
    plt.plot(t,V)
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [mV]')
