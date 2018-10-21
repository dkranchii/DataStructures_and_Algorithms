#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:32:54 2018

@author: kdp
"""

class Node:
    def __init__(self, data):
          self.data =  data 
          self.next = None

class Queue:
     def __init__(self):
           self.front  = None
           self.rear = None 
           self.size = 0
           
     def display(self):
         if self.front is None:
             return None
         else:
             p = self.front
             while p is not None:
                 print(p.data, end=" ")
                 p = p.next
    
     def is_Empty(self):
         if self.size == 0:
             print("Queue is Empty")
             return True
         else:
             return False 
         
     def enqueue(self,  data):
         temp = Node(data)
         if self.front is None:
             self.front = temp
             self.rear = temp
             self.size +=1
         else:
            self.rear.next = temp
            self.rear = temp
            self.size +=1
            
     def dequeue(self):
         if self.front is None:
             return
         else:
             dequeued = self.front.data
             self.front = self.front.next
             self.size -=1
         return dequeued
     
     def reverse(self):
         if self.front is None:
             return

         stack = []
         while self.front:
             dequeued = self.dequeue()
             stack.append(dequeued)
             #s: 11, 12, 13, 14, 15, 16, 17, 18
             #q:  empty

         while stack:
             popped = stack.pop()
             self.enqueue(popped)
            #q:  18, 17, 16, 15, 14, 13, 12, 11
            
              
     def reverseK(self, k):
         if self.front is None and k < self.size:
             return

         stack = []
         i = 0
         # add to stack elements up to k

         while self.front and i < k:
             dequeued = self.dequeue()
             stack.append(dequeued)
             i+=1
          
         #pop from stack and add to queue (rear)
         while stack:
             popped = stack.pop()
             self.enqueue(popped)
         
         #pop remaining items of the queue
         #and add them at the end again 
         #in the queue
         i = 0
         qs = self.size
         while i < qs-k:
             dequeued = self.dequeue()
             self.enqueue(dequeued)
             i+=1

     
     def interLeaveQueue(self):
          if self.size % 2 != 0:
              print("Enter even numbers of items")
              return
             
          stack = []
          halfsize = self.size //2
          
          #push first half from queue into stack
          for i in range(0, halfsize):
              dequeued = self.dequeue()
              stack.append(dequeued)
          # q: 15, 16, 17, 18
          # s: 11, 12, 13, 14
          
          stack.reverse()
          # s: 14, 13, 12, 11
          # q: 15 16, 17, 18
          
          #first pop&push from stack
          #second pop&push from queue    
          while stack:
             self.enqueue(stack.pop())      
             self.enqueue(self.dequeue())
          #q: 11, 15, 12, 16, 13, 17, 14,18

                 
#Test:
    
Q = Queue()
Q.enqueue(11)
Q.enqueue(12)
Q.enqueue(13)
Q.enqueue(14)
Q.enqueue(15)
Q.enqueue(16)
Q.enqueue(17)
Q.enqueue(18)
print("queue contains:", end="")
Q.display()


print()
print("Interleave:", end="")
Q.interLeaveQueue()
Q.display()

print()
print("Dequeued:", Q.dequeue())

print()
print("Reverse:", end="")
Q.reverse()
Q.display()

print()
print("Reverse first k items:", end="")
Q.reverseK(3)
Q.display()
print()
print()

print()
print("Size is ", Q.size)




