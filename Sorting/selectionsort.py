#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:52:43 2018

@author: kdp
"""

def selection_sort(A):
    
    for i in range(len(A)-1):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        if i != min_index:
            A[i], A[min_index] = A[min_index], A[i]
                
    
#test:
list1 = [22,34,21,29,8,8, 2, 3, 1, 0, 28, 27, 11,19, 18]
selection_sort(list1)
print(list1)                


#output
#[0, 1, 2, 3, 8, 8, 11, 18, 19, 21, 22, 27, 28, 29, 34]