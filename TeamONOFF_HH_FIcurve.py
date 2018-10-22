# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Team: "Did you turn it off and on?" -- Kaitlyn Michael Luis Margaret

# Hodgkin Huxley stuff

import numpy as np
from HH_functions import HH
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# plotting FI

# step 1: need multiple input currents
    
I0 = np.linspace(1,10,10)
n_spikes = []

# step 2: choose a value T for time of stim

T0 = 200

# step 3: establish a voltage threshold for "spikes"

V = np.array()
Vth = 0

# step 4: for loop for each input current value in HH model

for k in range(0, len(I0)
    [V,m,n,h,t]=HH(I0[k], T0)
    spike = V[V > Vth]
    peaks = find_peaks(spike)[0]
    rate = len(peaks)
    fRateVector = fRateVector + [rate]
    
# step 5: attempt to plot everything and hope for the best
    
plt.figure()
plt.plot(fRateVector,I0)
plt.xlabel('Current')
plt.ylabel('Frequency')
