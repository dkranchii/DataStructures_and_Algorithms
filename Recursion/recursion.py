#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 21:14:47 2019

@author: kdp
"""
"""
Template for designing recursive alg"
1. Determine size of the prob
2. Define base cases
3. Decompose computational problem with self-similar sub 
   of smaller size and possibly additional diff probs
4. Define recurse cases by relying on induction and diagrams
    (induction - key idea is that programmers must assume the recursive
     code works for simpler and smaller problems even if they have not written
     of code. Referred as recursive leap of faith)
5. Test the code
"""

def fib_recur(n):
    if n <= 2 :
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)
    
print("fibonacci", fib_recur(9))
#outuput for 9: 34
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55

def fact_recur(n):
    if n == 1:
        return 1
    else:
        return n * fact_recur(n-1)
    
print("factorial", fact_recur(5))
#5*4*3*2*1 = 120

def sum_recur(n):
    if n == 1:
        return 1
    else:
        return n + sum_recur(n-1)   
    
print("sum_recur", sum_recur(5))
#5+4+3+2+1 = 15

def sum_of_first_naturals_2(n):
    if n==1:
        return 1
    if n == 2:
        return 3
    elif n % 2:
        return (3 * sum_of_first_naturals_2((n-1)/2) 
                + sum_of_first_naturals_2((n+1)/2))
    else:
        return (3 * sum_of_first_naturals_2((n)/2) + 
                 sum_of_first_naturals_2((n)/2-1))
        
print("sum_of_first_naturals_2", sum_of_first_naturals_2(10))
#10+9+8+7+6+5+4+3+2+1 == 55

def sum_of_list_recur(A):
    if len(A)==0:
        return 0
    else:
        return A[0] + sum_of_list_recur(A[1:])
    
A=[1,2,3,41,5]
print("sum_of_list_recur", sum_of_list_recur(A))
#sum_of_list_recur 52

def sum_list_len_alt2(A):
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return A[0]
    else:
        middle = len(A) // 2
        return (sum_list_len_alt2(A[0:middle])
                + sum_list_len_alt2(A[middle:len(A)]))
    
B = [5,3,4,2,3]
print("sum_list_len_alt2", sum_list_len_alt2(B))
#sum_list_len_alt2 17

def sum_list_limits_1(A, lower, upper):
    if lower > upper:
        return 0
    else:
        return A[upper] + sum_list_limits_1(A, lower, upper-1)
    
A1 = [4,2,3,1,5]
print("sum_list_limits_1", sum_list_limits_1(A1,0, len(A1)-1))
#sum_list_limits_1 15


def sum_list_limits_2(A, lower, upper):
    if lower > upper:
        return 0
    else:
        return A[lower] + sum_list_limits_2(A, lower+1, upper)
    
A2 = [4,2,3,1,6]
print("sum_list_limits_2", sum_list_limits_2(A2, 0, len(A2)-1))
#sum_list_limits_2 16

def sum_list_limits_3(A, lower, upper):
    if lower > upper:
        return 0
    elif lower == upper:
        return A[lower]
    else:
        middle = (upper + lower) // 2
        return (sum_list_limits_3(A, lower, middle)
                + sum_list_limits_3(A, middle, upper))
        
A3 = [4,2,3,1,7]
print("sum_list_limits_3", sum_list_limits_2(A3, 0, len(A2)-1))
#sum_list_limits_3 17

def print_n_numbers(n):
    if n == 0: 
        return 0
    else:
        print(n, end= ",")
        print_n_numbers(n-1)
        
print(print_n_numbers(10))
#10,9,8,7,6,5,4,3,2,1,None

def print_n_numbers_reverse(n):
    if n == 0: 
        return 0
    else:
        print_n_numbers_reverse(n-1)
        print(n, end= ",")
        
print(print_n_numbers_reverse(10))
#1,2,3,4,5,6,7,8,9,10,None

def add_digits(n):
    if n < 10:
        return n
    else:
        return add_digits(n // 10) + (n % 10)

print("add digits", add_digits(326))
#11

def print_digits_reversed_vert(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        print_digits_reversed_vert(n // 10)
        
        
print(print_digits_reversed_vert(1234))
#4
#3
#2
#1

def max_list_length_DAC1(A):
    if len(A) == 1:
        return A[0]
    else:
        middle = len(A) // 2
        m1 = max_list_length_DAC1(A[0:middle])
        m2 = max_list_length_DAC1(A[middle:len(A)])
        return max(m1, m2)
    
A = [23, -1, 5, 56, 4, 2, 7]
print("max_list_length_DAC1", max_list_length_DAC1(A))
#max_list_length_DAC1 56


def max_list_length_DAC2(A, lower, upper):
    if lower == upper:
        return A[lower]
    else:
        middle = (upper + lower) // 2
        m1 = max_list_length_DAC2(A, lower, middle)
        m2 = max_list_length_DAC2(A, middle +1, upper)
        return max(m1, m2)
    
A = [23, -1, 5, 5, 4, 2, 7]
print("max_list_length_DAC2", max_list_length_DAC2(A, 0, len(A)-1))
#max_list_length_DAC2 23

def is_even(n):
    if n==0:
        return True
    elif n == 1:
        return False
    else:
        return is_even(n-2)
    
print("is 4 even", is_even(4))
print("is 3 even", is_even(3))
#is 4 even True
#is 3 even False

#non-negative exponents
def power_is(b, n):
    if n==0:
        return 1
    else:
        return b * power_is(b, n-1)
    
print("power is", power_is(2, 3))
#power is 8


def decimal_to_binary(n):
    if n < 2:
        return n
    else:
        return 10 * decimal_to_binary(n//2) + (n % 2)
    
print("Decimal to binary", decimal_to_binary(8))
#Decimal to binary 1000


def decimal_to_base(n, b):
    if n < b:
        return n
    else:
        return 10 * decimal_to_base(n // b, b) + (n % b)
    
print("decimal to base", decimal_to_base(1024,2))
#decimal to base 10000000000


#Strings
def reverse_string(s):
    if len(s) == 1:
        return s[0]
    else:
        return reverse_string(s[1:]) + s[0]
                                
print("reversing a string",  reverse_string("jimmie"))    
#reversing a string eimmij

def is_palindrome(s):
    n = len(s)
    if n <=1:
        return True
    else:
        return s[0] == s[n-1] and is_palindrome(s[1:n-1])

print("is palindrome nayan", is_palindrome("nayan"))
print("is palindrome kasam", is_palindrome("kasam"))
#is palindrome nayan True
#is palindrome kasam False


def occurrences_in_list(A, x):
    if A == []:
        return 0
    else:
        return int(A[0] == x) + occurrences_in_list(A[1:],x)
    
A=[1,34,5,2,-1,23,2]
print("occurrences_in_list", occurrences_in_list(A, 2))
#occurrences_in_list 2



