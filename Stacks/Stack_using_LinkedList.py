#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:13:21 2018

@author: kdp
"""

class Node:
    def  __init__(self, value):
        self.info = value
        self.link =  None
        
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False
        
    def push(self, data):  
        temp = Node(data)
        temp.link = self.top  #1st-none
        self.top = temp
        self.count +=1 
    
    def count(self):
        return self.count
        
    def size(self):
        if self.is_empty():
            return 0
        count = 0
        p = self.top
        while p is not None:
            p = p.link
            count+=1
        return count
    
    def peek(self):
        if self.is_empty():
            print("empty")
        else:
            return self.top.info
        
    def pop(self):
        if self.is_empty():
            print("nothing to pop")
        else:
            popped = self.top.info
            self.top = self.top.link
            self.count -= 1
            return popped
        

    def displayStack(self):
        if self.is_empty():
            print("empty")
        else:
            p = self.top
            print("[", end="")
            while p is not None:
                print(p.info, end=",")
                p = p.link
            print("]", end="")
                

    def popMiddle(self):
        if self.is_empty():
            print("empty")
        else:
            fast = self.top
            slow = self.top
            p = self.top
            
            while fast is not None:
                fast = fast.link   #move one+one
                
                if fast is None:   #in case of odd
                    popped = slow.info
                    p.link = slow.link
                    slow.link = None
                    return popped
                else: 
                    fast = fast.link
            
                p = slow              #save prev to p
                slow = slow.link  #move one step
            
            popped = slow.info    #save slow info
            p.link = slow.link    #mark prev node to next node
            slow.link = None      #slow link to none
            return popped         #return pop
    
        
#Test
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.displayStack()  #[3,2,1,]

print()
print("peek", s.peek())  #peek 3

print()
print("size", s.size())   #size 3

s.pop()
print()

s.displayStack()  #[2,1,]

s.push(3)
s.push(4)
s.push(5)
s.push(6)
print()
s.displayStack()  #[6,5,4,3,2,1,]

print()
print("popmiddle", s.popMiddle()) #popmiddle 3

print()
print("size", s.size())  #size 5

print()
s.displayStack() #[6,5,4,2,1,]
