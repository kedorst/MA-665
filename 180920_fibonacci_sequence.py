#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 12:08:30 2018

@author: test
"""

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 12
print("Fibonacci sequence:")
for i in range(nterms):
    print(recur_fibo(i))