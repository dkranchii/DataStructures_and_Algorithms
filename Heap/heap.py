#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 09:17:32 2018

@author: kdp
"""

#Heap is an array but acts like a tree.
#Heap uses Complete Binary Tree concept. 
#In a complete Binary Tree, nodes are added from left to right
#Root node is at position 1
#Fix up when you insert to bring larger values up
#Fix down when you delete to bring larger values up
class Heap:
    
    def __init__(self, heap_size):
        self.heap_size = heap_size
        self.heap = [0] * heap_size
        self.node_count = 0
        self.heap[0] = float("inf")
        self.load_factor  = 0.75
        
    def parent(self, index):
        return index//2
    
    def left_child(self, index):
        return 2 * index
    
    def right_child(self, index):
        return 2 * index + 1

    def insert(self, item):
        if self.node_count/self.heap_size >= self.load_factor:
            self.resize_heap(self.next_prime(2*self.heap_size))
        self._insert(item)

    #insert the new value at the last
    #and then fix_up if the last value is greater than its parent
    def _insert(self, item):
                    
        self.node_count +=1 
        self.heap[self.node_count] = item
        self.fix_up(self.node_count)
        
    def fix_up(self, index):
        
        #get the value of the new node
        new_node_value = self.heap[index]
        
        #get parent position of the new node
        iparent = self.parent(index)
        
        # keep checking the parent until root. 
        #if item greater, move up
        while self.heap[iparent] < new_node_value and iparent > 0:
            self.heap[index] = self.heap[iparent] # move parent down
            index = iparent  #store parent index as index
            iparent = self.parent(index) #get the next parent
        #once right position is found, store the new value there      
        self.heap[index] = new_node_value
        
    #peek max value    
    def get_max_value(self):
        if self.node_count == 0:
            return -1
        
        return self.heap[1]
    
    # Only operation supported by standard heap. 
    #After deleting the root. Copy the value of last node into root.
    #And then run fix_down method to find the next bigger value
    def remove_max(self):
        if self.node_count == 0:
            raise Exception("Heap is Empty")
        
        max_value = self.heap[1]
        self.heap[1] = self.heap[self.node_count] #move last item to root
        self.node_count -=1
        self.fix_down(1)  #pass 1 as the last value is at position 1 of the array
        
        return max_value
    
    
    # 
    def fix_down(self, index):
        
        #get the value of the index (in this case 1(root))
        root_node_value = self.heap[index] 
        
        lchild = self.left_child(index)
        rchild = self.right_child(index)   #3
        
        while rchild <= self.node_count:   #eg, 3 <= 9
            
            #if root is bigger that both right and left child.
            #assign root_node_value to index position
            if root_node_value >= self.heap[lchild] and root_node_value >= self.heap[rchild]:
                self.heap[index] = root_node_value
                return
            else:
                #root node value is not greater. 
                #check left node
                #if left value is greater than right value
                #move left child to parent
                if self.heap[lchild] > self.heap[rchild]:
                    self.heap[index] = self.heap[lchild]
                    index = lchild
                else:
                #root not value is not greater
                #check right node
                #if right value is greater than left value
                #move right child to parent
                    self.heap[index] = self.heap[rchild]
                    index = rchild
                    
             # get new left and right value of the new child
            lchild = self.left_child(index)
            rchild = self.right_child(index)  
            
            
        #if number of node is even
        if lchild == self.node_count and root_node_value < self.heap[lchild]:
            self.heap[index] = self.heap[lchild]
            index = lchild
        self.heap[index] = root_node_value
        
    #RESIZE Methods
    
    def resize_heap(self, new_size):
        temp = Heap(new_size) #new instance of a class
              
        for i in range(1, self.heap_size):
            if self.heap[i] != 0:
                temp.insert(self.heap[i])
                
        self.heap = temp.heap
        self.heap_size = new_size
        
    def next_prime(self, x):
        while self.is_prime(x) is not True:
            x = x+1
        return x
    
    def is_prime(self, x):
        for i in range(2,x):
            if x % i == 0:
                return False
        return True   
    
    
    def display_heap(self):
        
        print("Heap size is ", self.heap_size)
        print("Heap contains", end=" ")
        
        for i in range(0, self.heap_size):
            #if self.heap[i] != 0:
            print(self.heap[i], end=" ")
        print()
            
                

H = Heap(10)
H.display_heap()

#----Test insert----#
H.insert(11)
H.insert(14)
H.insert(23)
H.insert(9)
H.insert(12)
H.insert(45)
H.insert(66)
H.insert(77)
H.insert(4)

H.display_heap()

#test resize
H.insert(43)
H.insert(63)
H.insert(62)
H.insert(9)
H.insert(99)
H.insert(1200)
H.insert(132)
H.insert(142)

print("Max Value in the heap is", H.get_max_value())

#Display values of heap
H.display_heap()

##-----Remove Max Values----#

h = H.node_count
print()
print("Remove Max Values")
while h >= 1:
    print(H.remove_max())
    h-=1

"""
#------Output--------#

Heap size is  10
Heap contains inf 0 0 0 0 0 0 0 0 0 
Heap size is  23
Heap contains inf 77 66 45 12 11 14 23 9 4 0 0 0 0 0 0 0 0 0 0 0 0 0 
Max Value in the heap is 1200
Heap size is  23
Heap contains inf 1200 142 99 132 63 45 77 66 4 11 43 14 9 23 62 9 12 0 0 0 0 0 

Remove Max Values
1200
142
132
99
77
66
63
62
45
43
23
14
12
11
9
9
4

"""


        
    
    
    
        
        
        
        
        
        
    