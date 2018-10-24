#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:33:41 2018

@author: kdp
"""

# Worst case O(N square)
# 

def insertionSort(A):
    hi = len(A)
    
    for i in range(1, hi):
        temp = A[i]
        
        #j is the pointer between i and 0
        for j in range(i,0,-1):
            #swap if the value is smaller than temp
            if A[j-1] > temp:  
                A[j-1], A[j] =  A[j], A[j-1]
    return A    
          
A = [33,4,55,3,5,56,22,31]
print(insertionSort(A))


#Output
#[3, 4, 5, 22, 31, 33, 55, 56]