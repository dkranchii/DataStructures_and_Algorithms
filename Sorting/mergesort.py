#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:10:33 2018

@author: kdp
"""

def mergesort(A):
    if len(A) > 1:
        mid = len(A) // 2
        lefthalf = A[:mid]
        righthalf = A[mid:]
        mergesort(lefthalf)  #split left half until it contains only 1 item
        mergesort(righthalf) #split left half until it contains only 1 item
        
        #merge the two arrays
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            
            if lefthalf[i] < righthalf[j]:
                A[k] = lefthalf[i]
                i +=1
            else:
                A[k] = righthalf[j]
                j += 1
            k += 1
            
        while i < len(lefthalf):
            A[k] = lefthalf[i]
            i += 1
            k += 1
            
        while j < len(righthalf):
            A[k] = righthalf[j]
            j += 1
            k += 1

    return A


x = mergesort([5, 6, 1, 7, 8, 9, 2, 10, 4, 3])

print(x)

