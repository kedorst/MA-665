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

R = 0.5

Vstar = Vrest + (I*R)

T = R*C      

#Change/write your equation that demonstrates LIF
#V[k+1] is the voltage in the future
#V[k] is the voltage now
#the only thing that needs to change is the equation that is multiplied by dt
#can then go back and forth from the LIF and IF with some additional variable changes
        
for k in range(1,999):
    V[k+1] = V[k] + dt*(-(V[k] - Vstar) / T)
    if V[k+1] > Vth:
        V[k+1] = Vreset
        
t = np.arange(0,len(V))*dt

plt.figure()            
plt.plot(t,V)
plt.xlabel('Time [s]')
plt.ylabel('Voltage [mV]')

#okay let's try firing rate

nI = [2.0,4.0,6.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0]

F = np.zeros([10,1])

for q in range (0,9):
    F[q+1] = F[q] + (nI / ((Vth-Vreset) * C))


plt.figure()
plt.plot(nI,F)
plt.xlabel('Input Current ([mA]')
plt.ylabel('Firing Rate [Hz]]')