#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:29:11 2018

@author: kdp
"""

#Hash Table stores key values pairs. It is known by Map in Java and Dictionary in Python
#Hash Table array stores the address (reference) to instance of dictkeyvalue class. 
#This Hash Table stores the data using "open addressing" concept.
#Hash Table uses (key mod size) hash function to find position.
#When collision happens, find the next open slot using quadratic probing (2,4,8,16,32 etc)
#Clustering is the main problem with linear probing. 
#Resize the array to expand when the filled slots/table size is greater than load factor 0.75
#Resize the array to squeeze when filled slots are less than tablesize/4.

class dictKeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def get_key(self):
        return self.key
    
    def set_key(self, key):
        self.key = key
        
    def __str__(self):
        return str(self.key) + ":" + self.value
    
    
class Hash:    
    def __init__(self, size):
        self.tablesize = size
        self.hashtable = [None]*self.tablesize
        self.filled_slots = 0
        self.load_factor = 0.75
        
    
    def hash1(self, key):
        if type(key) == str:
                sum1 = self.SumofAsciiCode(key)
                hf = sum1 % self.tablesize
                return hf
        else:
            return key % self.tablesize
        
    def SumofAsciiCode(self, key):
        #only for inserting strings as key 
        #calculate the sum of 
        sum1 = 0
        n = len(key)
        for j in range(0, n):
            sum1 = sum1 + ord(key[j])  
        return sum1
        
    def insert(self, item):
         if self.filled_slots/self.tablesize >= self.load_factor:
             self.rehash(self.next_prime(2*self.tablesize))
             print()
             print("Grow Table - new tablesize is", self.tablesize)
         self.insert1(item)
    
    def insert1(self, newItem):
        
        key = newItem.get_key()
        h1 = self.hash1(key)
        
        #temp
        pos = h1
        print(newItem, "initial position:", pos)
        for i in range(1,self.tablesize):
            # if empty
            if self.hashtable[pos] is None or self.hashtable[pos].get_key() == -1:
                self.hashtable[pos] = newItem
                self.filled_slots +=1
                return True
            
            #if dups, skip
            if self.hashtable[pos].get_key() == key:
                return False
            
            #Collision, Find next spot using quadratic probing
            pos = (h1 + i*i) % self.tablesize  
        
        return False
    
    def delete(self, item):
        
        pos=self.search(item)
        
        if pos != None:
            self.hashtable[pos].set_key(-1)
            self.filled_slots -= 1
            
            #rehasing to squeeze the table
            if self.filled_slots > 0 and self.filled_slots <= self.tablesize/4:
                self.rehash(self.next_prime(self.tablesize//2))
                print("\nSqueeze Table - new Tablesize is ", self.tablesize)           
            return True
        
        return False
    
    def search(self, key):
        
        
        h = self.hash1(key)
        pos = h
        
        for i in range(1,self.tablesize):
            if self.hashtable[pos] is None:
               return None
           
            if self.hashtable[pos].get_key() == key:
               print(self.hashtable[pos], "is at pos", pos)
               return pos
            
            #Quadratic probing 
            pos = (h + i*i) % self.tablesize   
        
        return None    
    
    def display_table(self):     
        print()
        print("Show the whole Hash Table")
        for i in range(self.tablesize):
            print("[", i, "]", end=" ")
            if self.hashtable[i] is not None and self.hashtable[i].get_key() != -1 :
                print(self.hashtable[i])
            else:
                print("---")
                
        # print like python dict 
        print()
        print("Print key values like Python Dict")
        print("{")
        for item in self.hashtable:
            if item is not None and item.get_key() != -1:
                print(item, ",")
        print("}")
        print()
            
    
    def rehash(self, newsize):
        temp = Hash(newsize)   #create a temp hashtable
        
        #insert old values from existing table into temp
        for i in range(self.tablesize):
            if self.hashtable[i] != None and self.hashtable[i].get_key() != -1:
                temp.insert(self.hashtable[i])
                
        #copy the temp table to hastable
        self.hashtable = temp.hashtable
        #make new size
        self.tablesize = newsize
                 
    
    def next_prime(self, x):
        while self.is_prime(x) is not True:
            x = x+1
        return x
    
    def is_prime(self, x):
        for i in range(2,x):
            if x % i == 0:
                return False
        return True
    
#Test 
        
htable = Hash(11)

print("#--------Enter key Value pairs--------#")
anewItem =   dictKeyValue(1, "Los Angeles")
anewItem2 =  dictKeyValue(2, "San Francisco")
anewItem3 =  dictKeyValue('Aus', "Austin")
anewItem4 =  dictKeyValue('NYC', "New York City")
anewItem5=   dictKeyValue('Dal', "Dallas")
anewItem6 =  dictKeyValue('Bur', "Burbank")
anewItem7 =   dictKeyValue(5, "Denmark")
anewItem8 =  dictKeyValue(4, "Boston")
anewItem9 =  dictKeyValue(63, "Orlando")
anewItem10 =  dictKeyValue(65, "San Diego")

htable.insert(anewItem)
htable.insert(anewItem2)
htable.insert(anewItem3)
htable.insert(anewItem4)
htable.insert(anewItem5)
htable.insert(anewItem6)
htable.insert(anewItem7)
htable.insert(anewItem8)

htable.display_table()

htable.insert(anewItem9)
htable.insert(anewItem10)

htable.display_table()

print()
print("#------Search-----------#")
htable.search(anewItem3.get_key())
htable.search(anewItem2.get_key())
htable.search(anewItem8.get_key())


print()
print("#------Delete----------#")
htable.delete("Aus")
htable.delete(63)
htable.delete(5)
htable.delete(4)
htable.delete("NYC")
print()



htable.display_table()


"""
#-------------Output---------------#

#--------Enter key Value pairs--------#
1:Los Angeles initial position: 1
2:San Francisco initial position: 2
Aus:Austin initial position: 0
NYC:New York City initial position: 3
Dal:Dallas initial position: 9
Bur:Burbank initial position: 0
5:Denmark initial position: 5
4:Boston initial position: 4

Show the whole Hash Table
[ 0 ] Aus:Austin
[ 1 ] 1:Los Angeles
[ 2 ] 2:San Francisco
[ 3 ] NYC:New York City
[ 4 ] Bur:Burbank
[ 5 ] 5:Denmark
[ 6 ] ---
[ 7 ] ---
[ 8 ] 4:Boston
[ 9 ] Dal:Dallas
[ 10 ] ---

Print key values like Python Dict
{
Aus:Austin ,
1:Los Angeles ,
2:San Francisco ,
NYC:New York City ,
Bur:Burbank ,
5:Denmark ,
4:Boston ,
Dal:Dallas ,
}

63:Orlando initial position: 8
Aus:Austin initial position: 21
1:Los Angeles initial position: 1
2:San Francisco initial position: 2
NYC:New York City initial position: 4
Bur:Burbank initial position: 21
5:Denmark initial position: 5
63:Orlando initial position: 17
4:Boston initial position: 4
Dal:Dallas initial position: 20

Grow Table - new tablesize is 23
65:San Diego initial position: 19

Show the whole Hash Table
[ 0 ] ---
[ 1 ] 1:Los Angeles
[ 2 ] 2:San Francisco
[ 3 ] ---
[ 4 ] NYC:New York City
[ 5 ] 5:Denmark
[ 6 ] ---
[ 7 ] ---
[ 8 ] 4:Boston
[ 9 ] ---
[ 10 ] ---
[ 11 ] ---
[ 12 ] ---
[ 13 ] ---
[ 14 ] ---
[ 15 ] ---
[ 16 ] ---
[ 17 ] 63:Orlando
[ 18 ] ---
[ 19 ] 65:San Diego
[ 20 ] Dal:Dallas
[ 21 ] Aus:Austin
[ 22 ] Bur:Burbank

Print key values like Python Dict
{
1:Los Angeles ,
2:San Francisco ,
NYC:New York City ,
5:Denmark ,
4:Boston ,
63:Orlando ,
65:San Diego ,
Dal:Dallas ,
Aus:Austin ,
Bur:Burbank ,
}


#------Search-----------#
Aus:Austin is at pos 21
2:San Francisco is at pos 2
4:Boston is at pos 8

#------Delete----------#
Aus:Austin is at pos 21
63:Orlando is at pos 17
5:Denmark is at pos 5
4:Boston is at pos 8
NYC:New York City is at pos 4
1:Los Angeles initial position: 1
2:San Francisco initial position: 2
65:San Diego initial position: 10
Dal:Dallas initial position: 9
Bur:Burbank initial position: 0

Squeeze Table - new Tablesize is  11


Show the whole Hash Table
[ 0 ] Bur:Burbank
[ 1 ] 1:Los Angeles
[ 2 ] 2:San Francisco
[ 3 ] ---
[ 4 ] ---
[ 5 ] ---
[ 6 ] ---
[ 7 ] ---
[ 8 ] ---
[ 9 ] Dal:Dallas
[ 10 ] 65:San Diego

Print key values like Python Dict
{
Bur:Burbank ,
1:Los Angeles ,
2:San Francisco ,
Dal:Dallas ,
65:San Diego ,
}
"""


