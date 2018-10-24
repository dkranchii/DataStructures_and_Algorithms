#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:26:14 2018

@author: kdp
"""

# Time Complexity O(n square)

def bubblesort(A):
    n = len(A)-1
    swapped =1 
    for j in range(n, 0, -1):
        if swapped ==1:
            swapped=0    
            for i in range(0, n):
                if A[i] > A[i+1]:
                    A[i], A[i+1] = A[i+1], A[i]
                    swapped=1
    #test
    print(A)
    return A
    
# test:
A=[1,3,33,55,12,22]
bubblesort(A)


#Output
#[1, 3, 12, 22, 33, 55]