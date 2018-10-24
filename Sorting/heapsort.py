#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:56:53 2018

@author: kdp
"""

def heap_sort(A, n):
    build_heap_bottem_up(A, n)
    
    while n > 1:
        max_value = A[1]
        A[1] = A[n]
        A[n] = max_value
        n = n-1
        restore_down(1, A, n)
        
def build_heap_bottem_up(A, n):
    i = n//2
    while i >=1:
        restore_down(i, A, n)
        i = i-1
            
def restore_down(i, A, n):
    
    k = A[i]
    lchild = 2 * i
    rchild = lchild + 1
    
    while rchild <= n:
        if k >= A[lchild] and k >= A[rchild]:
            A[i] = k
            return
        elif A[lchild] > A[rchild]:
            A[i] = A[lchild]
            i = lchild
        else:
            A[i] = A[rchild]
            i = rchild
            
        lchild = 2 * i
        rchild = lchild + 1
        
    #if number of nodes is even
    if lchild == n and k < A[lchild]:
        A[i] = A[lchild]
        i = lchild
    A[i] = k
    
A = [34, 22, 21, 24, 10, 9, 11, 39, 19, 28, 32, 8,3,1,0,23,13]
n = len(A)-1
heap_sort(A, n)

for i in range(1,n+1):
    print(A[i], end=",")
print()

#output 
#0,1,3,8,9,10,11,13,19,21,22,23,24,28,32,39,