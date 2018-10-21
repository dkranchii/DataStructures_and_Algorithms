#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 12:03:32 2018

@author: kdp
"""

class BinaryNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data, node):  
        if self.root is None:
            self.root = BinaryNode(data) 
        else: 
            if data < node.info:                            
                if node.left != None:  
                    self.add(data, node.left)             
                else:
                    node.left = BinaryNode(data) 
            else:
                if node.right != None:    
                    self.add(data, node.right) 
                else:
                    node.right = BinaryNode(data) 

    def display(self, p, level):
        if p is None:
            return
        self.display(p.right, level+1)
        print()
        
        for i in range(level):
            print(" ", end=" ")
        print(p.info)
        self.display(p.left, level+1)
        

    def deleteNode(self, p, key):
        
        if p == None:
            return self.root
        
        if key < p.info: 
            p.left = self.deleteNode(p.left, key)
        elif key > p.info:   
            p.right = self.deleteNode(p.right, key)
        else:  #if equal to root.
            
            if p.left == None:    
                temp = p.right  
                p = None
                return temp       #return temp
            elif p.right == None:
                temp = p.left  
                p = None        #set root to None
                return temp        #retutn temp
            
            if temp != None:
                p.info = temp.info
        
            # if either child of root are not null, 
            # then make right child as root
            p.right = self.deleteNode(p.right, p.info)        
        return p



    # TRAVERSAL METHODS
    
    def pre_order_rec(self, root):
        if root is None:
            return
        print(root.info,  end = " ")
        self.pre_order_rec(root.left)
        self.pre_order_rec(root.right)
    
    #stack, add root, while stack (pop, print p.info, 
    #if right, append right, if left, append left)        
    def pre_order_iter(self):
        if self.root is None:
            return
        stack = [self.root]

        print("PreOrder Traversal (iter) ", end="-->")
        while stack:
            node = stack.pop()
            print(node.info, end = " " )
            
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
                
    def in_order_rec(self, root):
        if root is None:
            return
        self.in_order_rec(root.left)
        print(root.info,  end=" ")
        self.in_order_rec(root.right)
        
    
    #stack, while stack or p, if p is not None, append(p),  p=p.left.  
    #else,p=pop(), print, p=p.right

    def in_order_iter(self):
        if self.root is None:
            return
        p = self.root
        stack = []
        print("InOrder Traversal (iter) ", end="-->")

        while stack or p:
            if p is not None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                print(p.info,  end=" ")
                p = p.right
                

        #Divide and Counquer method available. Add later
    def kth_node_in_order(self, k):
        if self.root is None:
            return
        p = self.root
        stack = []
        print("Kth node in InOrder Traversal (iter) ", end="-->")
        kth = 0
        while stack or p:
            if p is not None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                if kth == k:
                    print(p.info,  end=" ")
                    return
                else:
                    kth +=1
                p = p.right

                
                
    def post_order_recur(self, root):
        if root is None:
            return
        self.post_order_recur(root.left)
        self.post_order_recur(root.right)
        print(root.info,  end=" ")
        
    def postOrderIter(self):
        if self.root is None:
            return
        stack = []
        p = self.root
        visited = set()
        
        print("PostOrder Traversal (iter) ", end="-->")
        while stack or p:
            if p is not None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                if p.right != None and p.right not in visited:
                    stack.append(p)
                    p = p.right
                else:
                    visited.add(p)
                    print(p.info, end=" ")
                    p = None                

    
    def level_order_traversal(self):
        queue_list = []
        queue_list.append(self.root)
        
        while queue_list:
            popped = queue_list.pop(0)
            print(popped.info, end=" ")
            
            if popped.left is not None:
                queue_list.append(popped.left)
                
            if popped.right is not None:
                queue_list.append(popped.right)


    def level_order_line_by_line(self):
        queue_list = []
        queue_list.append(self.root)
        
        while 1:
            nodeCount = len(queue_list)
            if nodeCount == 0:
                break
            
            while nodeCount > 0:
                popped = queue_list.pop(0)
                print(popped.info, end=" ")
            
                if popped.left is not None:
                    queue_list.append(popped.left)
                
                if popped.right is not None:
                    queue_list.append(popped.right) 
                
                nodeCount -=1
            print()
            
    def reverse_level_order(self):
        queue_list = []
        queue_list.append(self.root)
        stack = []
        while queue_list:
            popped = queue_list.pop(0)
            stack.append(popped)
            
            if popped.left is not None:
                queue_list.append(popped.left)
                
            if popped.right is not None:
                queue_list.append(popped.right)

        while stack:
            popp = stack.pop()
            print(popp.info, end=" ")
            

    #AGGREGATED/SIZE METHODS

    def size_recursive(self, p):
        if p is None:
            return 0
        return self.size_recursive(p.left) + self.size_recursive(p.right) +1 
    
    
    def size_iter(self):
        queue_list = [self.root]
        size = 0
        while queue_list:
            popped = queue_list.pop(0)
            if popped is not None:
                size += 1
            
            if popped.left is not None:
                queue_list.append(popped.left)
                
            if popped.right is not None:
                queue_list.append(popped.right)
            
        #test
        return size
    
    
    def max_rec(self, root):
        if root is None:
            return float("-inf")
        
        maxData = root.info
            
        lres = self.max_rec(root.left)
        rres = self.max_rec(root.right)
        
        maxData = max(max(lres, maxData), max(rres, maxData))
        return maxData
    
    
    def max_iter(self):
        if self.root is None: 
            return
        queue_list = [self.root]
        max1 = float("-inf")
        while queue_list:
            popped = queue_list.pop(0)
            if popped.info > max1:
                max1 = popped.info
            
            if popped.left is not None:
                queue_list.append(popped.left)
                
            if popped.right is not None:
                queue_list.append(popped.right)
            
        return max1

    def height_rec(self, root):
        if root is None:
            return 0
        return max(self.height_rec(root.left), self.height_rec(root.right)) + 1

    def height_iter(self):
        level=0
        if self.root is None:
            return
        queue_list = [self.root]
        queue_list.append(None)
        
        while queue_list:
            popped = queue_list.pop(0)

            if popped is None:
                if queue_list:
                    queue_list.append(None)
                level+=1

            else:
                if popped.left is not None:
                    queue_list.append(popped.left)
                if popped.right is not None:
                    queue_list.append(popped.right)
        
        return level
    
    def find_item_rec(self, root, data):
        if root is None:
            return "not found"
        if root.info == data:
            return "found"
        else:
            temp = self.find_item_rec(root.left, data)
            if temp == "found":
                return temp
            else:
                return self.find_item_rec(root.right, data)     
    
    def sum_of_values_recur(self, root):
        if root is None:
            return 0
        return root.info + self.sum_of_values_recur(root.left) + self.sum_of_values_recur(root.right)    


    def sum_of_values_iter(self):
        queue_list = [self.root]
        sum1 = 0
        while queue_list:
            popped = queue_list.pop(0)
            sum1 += popped.info 
            
            if popped.left is not None:
                queue_list.append(popped.left)
                
            if popped.right is not None:
                queue_list.append(popped.right)
            
        return sum1
    
    def sum_at_level(self):
        level=1
        if self.root is None:
            return

        queue_list = [self.root]
        queue_list.append(None)
        sum1 = 0

        while queue_list:
            popped = queue_list.pop(0)
            
            if popped is None:
                print("Sum at level",level, "is", end="->")
                print(sum1)
                sum1=0

                if queue_list:
                    queue_list.append(None)
                level+=1

            else:
                sum1+=popped.info

                if popped.left is not None:
                    queue_list.append(popped.left)
                if popped.right is not None:
                    queue_list.append(popped.right)
           

    def level_with_max_sum(self):
        level=1
        if self.root is None:
            return
        queue_list = [self.root]
        queue_list.append(None)
        sum1 = 0
        maxSum = float("-inf")
        maxLevel = 0
        while queue_list:
            popped = queue_list.pop(0)
            
            if popped is None:
                print("Sum at ",level, "is", end="->")
                print(sum1)
                if sum1 > maxSum:
                    maxSum = sum1
                    maxLevel = level
                sum1=0
                if queue_list:
                    queue_list.append(None)
                level+=1
            else:
                sum1+=popped.info
                if popped.left is not None:
                    queue_list.append(popped.left)
                if popped.right is not None:
                    queue_list.append(popped.right)
            
        return maxLevel
    
    #NODE COUNT METHODS
    
    def num_of_full_nodes(self, root):
        if root is None:
            return 0
        q = []
        q.append(root)
        count = 0
        while q:
            node = q.pop(0)
            if node.left is not None and node.right is not None:
                count +=1
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return count


    def num_of_half_nodes(self, root):
        if root is None:
            return 0
        q = []
        q.append(root)
        count = 0
        while q:
            p = q.pop(0)
            if p.left is not None and p.right is None:
                count +=1
            if p.right is not None and p.left is None:
                count +=1
                
            if p.left is not None:
                q.append(p.left)
            if p.right is not None:
                q.append(p.right)
        return count
    
    def num_of_leaf_nodes(self, root):
        if root is None:
            return 0
        q = []
        q.append(root)
        count = 0
        while q:
            node = q.pop(0)
            if node.left is None and node.right is None:
                count +=1
            else:
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return count
    
    def node_count_at_each_level(self):
        level=1
        if self.root is None:
            return
        queue_list = [self.root]
        queue_list.append(None)
        count1 = 0

        while queue_list:
            popped = queue_list.pop(0)

            if popped is None:
                print("Node Count at level ",level, "is", end="->")
                print(count1)
                count1=0

                if queue_list:
                    queue_list.append(None)
                level+=1

            else:
                count1+=1
                if popped.left is not None:
                    queue_list.append(popped.left)
                if popped.right is not None:
                    queue_list.append(popped.right)


#Test:
BT = BinaryTree()

print("#---------Add nodes to the tree----------#")
BT.add(10, BT.root)
BT.add(5, BT.root)
BT.add(15, BT.root)
BT.add(4, BT.root)
BT.add(6, BT.root)
BT.add(12, BT.root)
BT.add(16, BT.root)

BT.display(BT.root,0)

print()
print("#---------Remove nodes from the tree------#")
BT.deleteNode(BT.root, 4)
BT.display(BT.root,0)
print()

#Traversal Methods
print()
print("#----------Traversal Methods----------------#")
print("PreOrder Traversal (recur) -->", end="")
BT.pre_order_rec(BT.root)
print()
BT.pre_order_iter()

print()
print()
print("InOrder Traversal (recur) -->", end="")
BT.in_order_rec(BT.root)
print()
BT.in_order_iter()

print()
BT.kth_node_in_order(0)

print()
print()
print("PostOrder Traversal (recur) -->", end="")
BT.post_order_recur(BT.root)
print()
BT.postOrderIter()


print()
print()
print("LevelOrder Traversal -->", end="")
BT.level_order_traversal()


print()
print()
print("LevelOrder Traversal line by line")
BT.level_order_line_by_line()

print()
print("Reverse LevelOrder Traversal")
BT.reverse_level_order()

#Aggregate Methods
print()
print("#----------Aggregated Methods--------------#")
print("Max elem in the BT (recur) is", BT.max_rec(BT.root))
print("Max elem in the BT(iter) is", BT.max_iter())

print("Height of the BT(recur) is ", BT.height_rec(BT.root))
print("Height of the BT(iter) is ", BT.height_iter())

print("Item {} {} in the tree".format(5, BT.find_item_rec(BT.root, 5)))

print("Sum of the elem (recur) is ", BT.sum_of_values_recur(BT.root))
print("Sum of the elem (iter) is ", BT.sum_of_values_iter())

print()
BT.sum_at_level()

print()
print("Level with max sum ", BT.level_with_max_sum())

#Node Count Methods
print()
print("#----------Node Count Methods--------------#")
print("total nodes of the BT (recur) is", BT.size_recursive(BT.root))
print("total nodes of the BT (iter) is", BT.size_iter())
print("Num of full nodes ", BT.num_of_full_nodes(BT.root))
print("Num of half nodes ", BT.num_of_half_nodes(BT.root))
print("Num of leaf nodes ", BT.num_of_leaf_nodes(BT.root))    
BT.node_count_at_each_level()


"""
#---Output---#

#---------Add nodes to the tree----------#

    16

  15

    12

10

    6

  5

    4

#---------Remove nodes from the tree------#

    16

  15

    12

10

    6

  5


#----------Traversal Methods----------------#
PreOrder Traversal (recur) -->10 5 6 15 12 16 
PreOrder Traversal (iter) -->10 5 6 15 12 16 

InOrder Traversal (recur) -->5 6 10 12 15 16 
InOrder Traversal (iter) -->5 6 10 12 15 16 

PostOrder Traversal (recur) -->6 5 12 16 15 10 
PostOrder Traversal (iter) -->6 5 12 16 15 10 

LevelOrder Traversal -->10 5 15 6 12 16 

LevelOrder Traversal line by line
10 
5 15 
6 12 16 

Reverse LevelOrder Traversal
16 12 6 15 5 10 
#----------Aggregated Methods--------------#
Max elem in the BT (recur) is 16
Max elem in the BT(iter) is 16
Height of the BT(recur) is  3
Height of the BT(iter) is  3
Item 5 found in the tree
Sum of the elem (recur) is  64
Sum of the elem (iter) is  64

Sum at level 1 is->10
Sum at level 2 is->20
Sum at level 3 is->34

Sum at  1 is->10
Sum at  2 is->20
Sum at  3 is->34
Level with max sum  3

#----------Node Count Methods--------------#
total nodes of the BT (recur) is 6
total nodes of the BT (iter) is 6
Num of full nodes  2
Num of half nodes  1
Num of leaf nodes  3
Node Count at level  1 is->1
Node Count at level  2 is->2
Node Count at level  3 is->3

"""