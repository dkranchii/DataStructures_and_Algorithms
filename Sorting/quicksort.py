#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:02:09 2018

@author: kdp
"""

def quickSort(array):
    n = len(array)
    
    if n < 2:
        return array
    
    else:
        
        pivot = array[0]
        less = []
        greater=[]
        
        for i in range(1,n): 
            if array[i] < pivot:
                less.append(array[i])
            else:
                greater.append(array[i])
                
        return quickSort(less) + [pivot] + quickSort(greater)
	

#test    
list2= [5,39,2,3, 11, 9,8,12, 23, 355, 155]
list3=quickSort(list2)
print(list3)

