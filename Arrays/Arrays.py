# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def unsorted_linear_search(A, data):
    n = len(A)
    
    for i in range(0, n):
        if A[i] == data:
            return i
    
    return -1

A = [1,19,5,8,24,3, 12,14,4,2]
print(unsorted_linear_search(A, 3))
print(unsorted_linear_search(A, 6))

#O(N)
#output: 
#5
#-1

def sorted_search(A, data):
    n = len(A)
    
    for i in range(0,n):
        if A[i] == data:
            return i
        else:
            if A[i] > data:
                return -1
            
    return -1

A = [1,2,3,4,5,6,8,10,12,24,25]
print(sorted_search(A, 10))
print(sorted_search(A, 11))

#O(N)
#output
#7
#-1

#constraint - sorted
def Binary_search_iterative(A, data):
    lo = 0
    hi = len(A)-1
    
    while lo <= hi:
        mid =  lo+(hi-lo) // 2
        if A[mid] == data:
            return mid
        elif A[mid] > data:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

A = [1,2,3,4,5,6,8,10,12,24,25]
print(Binary_search_iterative(A, 2))
print(Binary_search_iterative(A, 25))

#O(logN)
#1, 10

#recursion. divide and conquer
def binary_search_recursive(A, lo, hi, data):

    if hi >= lo:
        mid = lo+ (hi-lo) // 2
        if A[mid] == data:
            return mid
        elif A[mid] < data:
            return binary_search_recursive(A, mid+1, hi, data)
        else:
            return binary_search_recursive(A, lo, mid-1, data)       
    else:
        return -1

A = [1,2,3,4,5,6,8,10,12,24,25]
print(binary_search_recursive(A, 0, len(A)-1, 3))
print(binary_search_recursive(A, 0, len(A)-1, 24))

#O(logN)
#2, 9
        

def check_duplicates_brute_force(A):
    n = len(A)
    for i in range(0, n):
        for j in range(1, n):
            if A[i] == A[j]:
                print("Dups exists")
                return
    print("No Dups")
    
A = [1,2,3,4,5,6,8,4,12,24,25]
check_duplicates_brute_force(A)
#output 
#Dups exists
#O(N2)

#sort the list. and then compare value with value next to it.
def check_dups_in_sorted(A):
    A.sort()
    n = len(A)
    for i in range(0, n-1):
        if A[i] == A[i+1]:
            print("Dups exists")
            return
            
    print("Dups do not exist")

A = [1,19,5,8,24,3, 12,2,4,2]
check_dups_in_sorted(A)
#output
#Dups exists
#O(NLogN) - NLogN due to sorting.


#read the array and move even numbers in front of the list
#and odd numbers in the back.
def even_odd(A):
    lo = 0
    hi =  len(A) -1
    
    while lo < hi:
        if A[lo] % 2 == 0:
            lo += 1
        else:
            A[lo], A[hi] = A[hi], A[lo]
            hi -= 1
        
A = [1,19,5,8,24,3, 12,2,4,2]
even_odd(A)
print(A)
#output
# [2,4,2,8,24.12,3,5,19,1]
        

def delete_dups_from_sorted_array(A):    
    if not A:
        return 0
    
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index-1] != A[i]:
            A[write_index] = A[i]
            write_index +=1
            
    return write_index

A = [1,2,2,4,5,6,8,12,12,24,25]
index = delete_dups_from_sorted_array(A)
#first 9 entries are good out of 11 
for i in range(0, 9):
    print(A[i], end=",")
#1,2,4,5,6,8,12,24,25
    

#max elem
def find_max_elem_in_array(A):
    n = len(A)
    
    max = A[0]
    for i in range(1, n):
        if A[i] > max:
            max = A[i]
    return max

A = [10,324,45, 90, 100]
max1 = find_max_elem_in_array(A)
print("\nLargest elem is", max1)


#function to find a given integer x appears more than n/2 times
#divide and conquer using binary search

#helper binary search function
def binary_search_alt(A, lo, hi, data):

    if hi >= lo:
        mid = lo + hi // 2
        
        #check if A[mid] is first occ of x.
        #A[mid] is first occ if one of the following is true
        #1 mid == 0 and A[mid] == x
        #2 A[mid-1] < x and A[mid] == x
        if (mid == 0 or x > A[mid-1]) and (A[mid] == data):
            return mid
        elif A[mid] < data:
            return binary_search_recursive(A, mid+1, hi, data)
        else:
            return binary_search_recursive(A, lo, mid-1, data)       
    else:
        return -1


def is_majority(A, n, x):
    
    #if i is found.
    i = binary_search_alt(A, 0, n-1, x)
    
    if i == -1:
        return False
    
    #check if the element is present more than n/2 times
    if ((i + n//2) <= (n-1)) and A[i + n//2] == x:
        return True
    else:
        return False
    

AB = [1,2,3,3,3,3,3,3, 10]
n=len(AB)
x = 3
print("does", x, "appear more than n/2 times in A?",is_majority(AB,n,x))
#output does 3 appear more than n/2 times in A? True

def last_duplicate_index_in_a_sorted_array(A):
    n = len(A)
        
    if (A is None or n <= 0):
        return
    
    for i in range(n-1, 0, -1): #reverse traversal
        if A[i] == A[i-1]:
            print("Last index is", i, "of the Last duplicate itm in A", A[i])
            return
    print("no dups")
    
A = [1,5,5,6,6,7,9]
last_duplicate_index_in_a_sorted_array(A)
#output: Last index is 4 of the Last duplicate itm in A 6


#buy the stock once and sell once. Buying has to happen before.
def buy_and_sell_stock_prices(prices):
    
    min_price_so_far = prices[0]
    max_profit  = 0.0
    
    for price in prices:    
        #today's profit - today's price minus min price.
        max_profit_sell_today = price - min_price_so_far
        
        #compare max profit until now and store the max
        max_profit = max(max_profit, max_profit_sell_today)
        
        #maintain minimum price so far.
        min_price_so_far = min(min_price_so_far, price)
        
    return max_profit

prices = [7,1,5,3,6,4]
print("max profit is", buy_and_sell_stock_prices(prices))


#arrange where B[0] <= B[1] >= B[3] <= B4 >= B5..
#computer alternation
#sorting is not needed. Median is not needed either
#iterating through the array and swapping A[i] A[i+1] when i is even
#and A[i] > A[i+1] or i is odd and A[i] < A[i+1] achieves it.
#O(N)
def rearrange(A):
    
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i : i+2], reverse = i % 2)
        
A = [1,19,5,8,24,3,12,2,4,2]
rearrange(A)
print("A[0] < A[1] > A2 < A3 > A4 < A5..")
print(A)
#output [1, 19, 5, 24, 3, 12, 2, 8, 2, 4]


#Given an array return a random subset of the given size of the array elemts
import random
def random_sampling(A, k):
    
    for i in range(k):
        r = random.randint(i, len(A)-1)
        A[i], A[r] = A[r], A[i]
        
A = [3,7,5,11]
k = 3
random_sampling(A, k)
print(A[0:k])


#find first elem larger than k in a sorted list
#divide and conquer 
#log(N)
def find_next_higher(A, k):
    
    lo = 0
    hi = len(A)-1
    
    result = float("inf")
    while lo <= hi:
        mid = (lo + hi) // 2
        
        if A[mid] > k:
            result = A[mid] #upfate result
            hi = mid - 1
        else:
            lo = mid + 1
            
    return result

A = [1,2,3,4,5,6,8,10,12,24,25]
k = 6
print("next higher than k {} is".format(k), find_next_higher(A, k))


def get_missing_num(A):
    n = len(A)
    total = (n+1) * (n+2) / 2
    sum_of_A = sum(A)
    return total - sum_of_A

A = [1,2,4,5,6]
print("missing number is ", get_missing_num(A))

#output 3

#find two elems whose sum is closes to 0
# sort all elem of input array
# use lo and high to traverse from left to right.
# sum = a[lo] + a[hi].  
#keep track of abs min. Repeat 
def two_elements_whose_sum_is_closest_to_zero(A):
    
    lo = 0
    hi = len(A)-1
    
    #variables to keep track of pairs
    min_lo = lo
    min_hi = hi
    if hi < 2:
        print("mininum two elements needed")
        return
    
    #sort
    A.sort()
    min_sum = float("inf")
    sum1 = float("inf")
    while lo < hi:
        
        sum1 = A[lo] + A[hi]
        
        #if sum1 is less than minsum. 
        #store sum1 in minsum. and update min_lo, min_hi
        if abs(sum1) <= abs(min_sum):
            min_sum = sum1
            min_lo = lo 
            min_hi = hi
            
        #sum1 is -ve traverse right(lo++). 
        #if sum is +ve, traverse left(hi--)
        if sum1 < 0:
            lo += 1
        else:
            hi -= 1
            
    #print the A[min_lo] and A[min_hi]
    print("The two elements whose sum is min are ", A[min_lo], A[min_hi])


A = [1,60, -20, 22, -98, 86, 21]
two_elements_whose_sum_is_closest_to_zero(A)
        

#assume no duplicates in an array
#divide and conquer.
def search_in_rotated_array(A, data):
    lo = 0
    hi = len(A)-1
    
    while lo < hi:
        mid = lo + (hi-lo)//2
        
        if A[mid] == data:
            return mid
        
        if A[lo] <= A[mid]:
            if data < A[mid] and data >= A[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
                
        if A[mid] <= A[hi]:
            if data > A[mid] and data <= A[hi]:
                lo = mid + 1
            else:
                hi = hi - 1
                
    return -1 

A = [3,4,5,6,1,2]
k  = 1 
print("Item found at index ", search_in_rotated_array(A, k))


#pring the max sum of contiguous data elements.
def contiguous_max_sub_array(A):
    
    dp = []
    #copy first number to new list.
    dp.insert(0, A[0])
    
    #make the first element as max sum
    max_sum = dp[0]
    
    #traverse from elem 1. 
    #Compare with last elem in new list. 
    #Add new list element-1 with A[i] if its greater than 0 else only add A[i]
    for i in range(1, len(A)-1):
        dp.append(A[i] + (dp[i-1] if dp[i-1] > 0 else 0))
        max_sum = max(dp[i], max_sum)
    
    
    return max_sum
   

A = [-2, 1,-3, 4, -1, 2, 1, -5, 4]
print(contiguous_max_sub_array(A))
    
