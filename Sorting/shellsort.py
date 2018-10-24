#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:45:18 2018

@author: kdp
"""

#Worst case: time O(N square)
#Best case: O(N)
#Even though shell sort is faster than other n square algorithms,
#it is significantly slower than merge, heap and quick sorts.
#good choice for smaller list

def shell_sort(A):
    
    #enter 3 to test
    h = int(input("Enter max increment odd value: "))
    
    while h >= 1:
        for i in range(h, len(A)):
            temp = A[i]
            j = i-h
            while j >= 0 and A[j] > temp:
                A[j+h] = A[j]
                j = j - h
                A[j+h] = temp
        h = h-2
    return A  
    
#test
list1 = [45,23, 24,21, 5, 2, 6, 245, 3, 1, 55, 9, 8,7,19]
shell_sort(list1)
print(list1)

#output
#[1, 2, 3, 5, 6, 7, 8, 9, 19, 21, 23, 24, 45, 55, 245]