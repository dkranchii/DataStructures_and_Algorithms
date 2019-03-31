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

def gcd(m, n):
    if m == 0:
        return n
    elif m > n:
        return gcd(n, m)
    else:
        return gcd(m, n-m)
    
print("gcd of 1200,232 is", gcd(1200, 232))
#gcd of 1200,232 is 8


def gcd_v1(a, b):
    if b == 0:
        return a
    else:
        return  gcd_v1(b, a%b)

print("gcd of 888,462 is", gcd_v1(888, 462))
#gcd of 1200,232 is 8


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

def max_item_in_list_DAC1(A):
    if len(A) == 1:
        return A[0]
    else:
        middle = len(A) // 2
        m1 = max_item_in_list_DAC1(A[0:middle])
        m2 = max_item_in_list_DAC1(A[middle:len(A)])
        return max(m1, m2)
    
A = [23, -1, 5, 56, 4, 2, 7]
print("max_list_length_DAC1", max_item_in_list_DAC1(A))
#max_list_length_DAC1 56


def max_item_in_list_DAC2(A, lower, upper):
    if lower == upper:
        return A[lower]
    else:
        middle = (upper + lower) // 2
        m1 = max_item_in_list_DAC2(A, lower, middle)
        m2 = max_item_in_list_DAC2(A, middle +1, upper)
        return max(m1, m2)
    
A = [23, -1, 5, 5, 4, 2, 7]
print("max_list_length_DAC2", max_item_in_list_DAC2(A, 0, len(A)-1))
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

def power_alt(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return power_alt(x, y//2) * power_alt(x, y//2)
    else:
        return (x * power_alt(x, y//2)) * power_alt(x, y//2)
    
x = 2
y = 3
print("power alt is ", power_alt(x,y))
# power alt is  8


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

def longest_palindromic_substring(s):
    n = len(s)
    if is_palindrome(s):
        return s
    else:
        aux1 = longest_palindromic_substring(s[1:n])
        aux2 = longest_palindromic_substring(s[0:n-1])
        if len(aux1) > len(aux2):
            return aux1
        else:
            return aux2

print("longest palindromic substring is", longest_palindromic_substring("nayanic"))
#longest palindromic substring is nayan

def equal_strings(s,t):
    if len(s) != len(t):
        return False
    elif s == '':
        return True
    else:
        return s[0] == t[0] and equal_strings(s[1:], t[1:])
    
print("strings joe and joe are equal", equal_strings( "joe", "joe"))
print("strings smith and joe are equal", equal_strings( "smith", "joe"))
#strings joe and joe are equal True
#strings smith and joe are equal False

def equal_strings_tail(s, t):
    if len(s) != len(t):
        return False
    elif s == '':
        return True
    elif s[0] != t[0]:
        return False
    else:
        return equal_strings_tail(s[1:], t[1:])
    

print("strings mary and mary are equal", equal_strings_tail( "mary", "mary"))
print("strings mary and joe are equal", equal_strings_tail( "mary", "joe"))
#strings mary and mary are equal True
#strings mary and joe are equal False

def occurrences_in_list(A, x):
    if A == []:
        return 0
    else:
        return int(A[0] == x) + occurrences_in_list(A[1:],x)
    
A=[1,34,5,2,3,23,2]
print("occurrences_in_list", occurrences_in_list(A,3))
#occurrences_in_list 2

def linear_search_list_tail(A, x):
    n = len(A)
    if A==[]:
        return -1
    elif A[n-1] == x:
        return n-1
    else:
        return linear_search_list_tail(A[:n-1])
    
    
A=[1,34,5,12,4,23,2]
print("linear search in list", linear_search_list_tail(A,2))
#linear search in list 6
    
def linear_search_linear(A, x, n):
    if A == []:
        return -n-1
    elif A[0] == x:
        return 0
    else:
        return 1 + linear_search_linear(A[1:], x, n)
    
    
A=[1,34,5,12,5,23,2]
n = len(A)
print("linear search in list", linear_search_linear(A, 12, n))
#linear search in list 3
print("linear search in list", linear_search_linear(A, 15, n))
#linear search in list -1

def linear_search_tail_2(A, x, n):
    if A == []:
        return -1
    elif A[0] == x:
        return n
    else:
        return 1 + linear_search_tail_2(A[1:], x, n+1)
    
    
A=[1,34,5,12,4,23,2]
n = len(A)
print("linear search in list", linear_search_linear(A, 23, n))
#linear search in list 5
print("linear search in list", linear_search_linear(A, 11, n))
#linear search in list -1

def binary_search(A, x, lower, upper):
    if lower > upper:
        return -1
    else:
        middle = (lower + upper) // 2
        if x== A[middle]:
            return middle
        elif x < A[middle]:
            return binary_search(A, x, lower, middle-1)
        else:
            return binary_search(A, x, middle+1, upper)

bb=[1, 3, 7, 22, 33, 44, 55, 56, 78]
print("binary search in a list" , binary_search(bb, 56, 0, len(bb)-1))
#binary search in a list 7

def get_smaller_than_or_equal_to(A, x):
    if A == []:
        return []
    elif A[0] <= x:
        return [A[0]] + get_smaller_than_or_equal_to(A[1:], x)
    else:
        return get_smaller_than_or_equal_to(A[1:],x)
    
AA = [9,6,1,7,4,5]
print("get smaller than 5", get_smaller_than_or_equal_to(AA, 5))
#get smaller than 5 [1, 4, 5]

def get_greater_than(A, x):
    if A == []:
        return []
    elif A[0] > x:
        return [A[0]] + get_greater_than(A[1:],x)
    else:
        return get_greater_than(A[1:],x)
    
AB = [9,6,1,7,4,5]
print("get greater than 5", get_greater_than(AB, 4))
#get greater than 5 [9, 6, 7, 5] 


def is_list_sorted(A):
    n = len(A)
    if n <= 1:
        return True
    else:
        return (is_list_sorted(A[0:n//2])
                and A[n // 2-1] <= A[n//2]
                and is_list_sorted(A[n // 2:n]))
    
AZ = [1,3,5,6,79, 110]
print("is list sorted", is_list_sorted(AZ))
#is list sorted True

def select_sort_rec(a):
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        m = min(b)
        b.remove(m)
        
        return [m] + select_sort_rec(b)
    
A = [7,5,23,3,8,4]
print(select_sort_rec(A))


def select_sort_rec_1(a):
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        min_indx = b.index(min(b))
        aux = b[min_indx]
        b[min_indx] = b[0]
        b[0] = aux
        
        return [aux] + select_sort_rec_1(b[1:])
    
A = [7,5,23,3,8,4]
print(select_sort_rec_1(A))

def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    else:
        m1 = merge_sort(A[0:n//2])
        m2 = merge_sort(A[n // 2: n])
        return merge(m1, m2)
    
def merge(a, b):
    if a == []:
        return b
    if b == []:
        return a
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:],b)
        else:
            return [b[0]] + merge(a, b[1:])
                  
AX = [7,3,4,5,6,33,3,6]
print("merge sort list is ", merge_sort(AX))
#merge sort list is  [3, 3, 4, 5, 6, 6, 7, 33]

def pascal(n):
    if n==0:
        return [1]
    else:
        row = [1]
        previous_row = pascal(n-1)
        for i in range(len(previous_row)-1):
            row.append(previous_row[i] + previous_row[i+1])
        row.append(1)
    return row

print(pascal(8))
#[1, 8, 28, 56, 70, 56, 28, 8, 1]


 
#ABC -->0/0 --> call rec ABC 
    #-->1/1 -->call ABC  2/2 call ABC [l==r match, print (ABC)]
    #ABC
    #-->2/1 -->call ACB  2/2 call ACB [l==r match print (ACB) ]
#ABC --> ABC
    
#ABC -->1/0 --> call rec  BAC 
     #-->1/1 -->call BAC  2/2 Call BAC [l==r match print (ABC)]
     #BAC
     #-->2/1 -->call ACB  2/2 Call BCA [l==r matchprint (BCA)]
#BCA --> ABC

#ABC -->2/0 --> call rec CBA 
    #-->1/1 -->call CBA  2/2 Call CBA [l==r match print (CBA)]
    #CBA
    #-->2/1 -->call CAB  2/2 Call CAB [l==r match print (CAB)]
#CBA --> ABC 

def perm_of_list(A, l, r):
    if l==r:
        print(A)
    else:
        for i in range(l, r+1):
            A[l], A[i] = A[i], A[l]
            perm_of_list(A, l+1, r)
            A[l], A[i] = A[i], A[l]
            

B="ABC"
n = len(B)
A = list(B)
perm_of_list(A, 0, n-1)


#Catalan numbers

def catalan(n):
    if n <= 1:
        return 1
    
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-i-1)
        
    return res

print("catalan numbers: ", end= "")
for i in range(10):
    print(catalan(i), end= " ")
    
#output: 1 1 2 4 14 42 132 429 1430 4862
print()

#Binomial Coefficient
#gives number of ways, disregarding order,
#that k object can be chosen from among n objects. 
#formally k element subset of n element set
def binomialCoeff(n, k):
    
    if k == 0 or k == n:
        return 1
    
    return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)

n = 5 
k = 2
print("binomial Coeff of n=5, k=2 is", binomialCoeff(n, k))


#coin change problem
# N = 4, s = {1,2,3} there are four solutions: {1,1,1,1}, {1,1,2}, {2,2}, {1,3}
#output should be 4. 
def count(S, m, n):
    
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    if m <= 0 and n >= 1:
        return 0
    
    return count(S, m-1, n) + count(S, m, n-S[m-1])

arr=[1,2,3]
m = len(arr)
print(count(arr, m, 4))

#output 4:
"""
                  C(1,2,3),5
 
                /            \ 
              /                \
            
        C{1,2,3},2)              C{1,2}, 5)
        /       \               /          \ 
       /        \              /            \
C{1,2,3}, -1)    C{1,2},2)  C{1,2},3)       C{1}, 5)
                /  \            /    \            /    \
               /    \          /      \          /     \
       C(1,2), 0)  C{1},2)  C{1,2},1) C{1},3)  C{1},3)  C{},4)
                                               /   \
                                              /     \
"""


#Subset of sum problem
# Given a set of non-negative integers and a value sum,
# determine if there is a subset of a given set with sum equal to sum

def isSubsetSum(set, n, sum):
    
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    
    if set[n-1] > sum:
        return isSubsetSum(set, n-1, sum)
    
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])

set = [3,34,4,12, 5,2 ]
sum = 9
n = len(set)
if isSubsetSum(set, n, sum) == True:
    print("Found a subset with given sum")
else:
    print("No subset with given sum")
    
#output Found a subset with given sum
"""   
                            ISS(set, n, sum)
                        /                    \
                       /                         \
       ISS(set, n-1, sum)                         ISS(set, n-1, sum-set[n-1])
       /            \                                      /                 \
      /              \                                     /                 \
ISS(set, n-2, sum) ISS(set, n-2, sum-set[n-2])  ISS(set, n-2, sum-set[n-1])  ISS(n-2, sum-set[n-1]-set[n-2])     
"""


#Longest common subsequence

def lcs(X, Y, m, n):
    
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
    
X = 'AXYT'
Y = 'AYZX'
print("Length of LCS is ", lcs(X, Y, len(X), len(Y)))

#output of LCS is 2  (AY)


#Cutting rod

def cutRod(price, n):
    if n <= 0:
        return 0
    max_val = float("-inf")
    
    for i in range(0,n):
        max_val = max(max_val, price[i] + cutRod(price, n-i-1)
                      )
    return max_val

arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Max obtainable value is ", cutRod(arr, size))

#Max obtainable value is 22


#Friends Pairing:
#Given n friends, each one can remain single or can be paired up with some other 
#friend. Each friend can be paired only once. 
# Find out the total number of ways in which friends can remain single or paired up
#{1}, {2}, {3} -- all single
#{1}, {2,3} : 2 and 3 paird but 1 is single
#{1,2}, {3} : 1 and 2 are paired but 3 is single
#{1,3}, {2} : 1 and 3 are paired but 2 is single
#{1,2} and {2,1} are same.
def countFriendsPairings(n):
    
    if n <= 1:
        return 1
    return countFriendsPairings(n-1) + ((n-1)  * countFriendsPairings(n-2))

n = 3
print(countFriendsPairings(n))

# output 4.  for n = 4, output 10, for n = 5, output is 26

#find a peak element - use binary search

def findpeak(A, low, high, n):
    
    mid = low + (high-low)/2
    mid = int(mid)
    
    if mid == 0 or A[mid-1] <= A[mid] and \
        (mid == n-1  or A[mid+1] <= A[mid]):
            return mid
    
    elif mid > 0 and A[mid-1] > A[mid]:
        return findpeak(arr, low, mid-1, n)
   
    else:
        return findpeak(arr, mid+1, high, n)
    
A = [1,3,20,4,1,0]
print("index of a peak point is", findpeak(A, 0, n-1, n))
#index of a peak point is 2

