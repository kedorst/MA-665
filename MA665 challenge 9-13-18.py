# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

np.random.rand(10,20)
#create a 10 x 20 matrix with random numbers

np.fill_diagonal(p,1)
#put 1s on the diagonal

o = np.tril(np.ones([10,20], int) )
#make a second matrix with a 10 x 20 with all zeros
#np.tril with traingles of 1s below the diagonal
 
q = np.array(p * o)
#multiply the two matrices

