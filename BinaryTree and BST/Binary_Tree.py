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
        self.hd = 0  #bottom view
        
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
                    return
            else:
                if node.right != None:    
                    self.add(data, node.right) 
                else:
                    node.right = BinaryNode(data) 
                    return

    def add_iter(self, root, data):
        q = []
        newNode = BinaryNode(data)
        if newNode is None:
            print("System Memory Error")
            return
        if root is None:
            self.root = newNode
            return
        q.append(root)
        while q:
            temp = q.pop(0)
            if temp.left is not None:
                q.append(temp.left)
            else:
                temp.left = newNode
                return
            if temp.right is not None:
                q.append(temp.right)
            else:
                temp.right = newNode
                return
        del q
        return
    
     #recursively display binary tree
     #call right node with level +1. ]
    def display(self, p, level):
        if p is None:
            return
        self.display(p.right, level+1)
        print()
        
        for i in range(level):
            print(" ", end=" ")
        print(p.info)
        self.display(p.left, level+1)
        
    #recursively delete a node
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

    # recursively delete the tree.
    def delete_binary_tree_rec(self, root):
        if root is None:
            return
        
        if root.left is not None:
            self.delete_binary_tree_rec(root.left)
        if root.right is not None:
            self.delete_binary_tree_rec(root.right)
            
        self.root = None
        return self.root
        
    def _delete_binary_tree_iter(self, root):
        if root is None:
            return
        q = []
        q.append(root)
        while q:
            p = q.pop(0)
            if p.left is not None:
                q.append(p.left)
            if p.right is not None:
                q.append(p.right)
            p = None
        return p
    
    def delete_tree_iter(self, node_ref):
        node_ref = self._delete_binary_tree_iter(node_ref)
        return node_ref
    
    # TRAVERSAL METHODS-------------------------------------------------------
    
    #recursive - print root.info, call with left node. call with right node
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
     
    #recursive - call with left, print root.info, call with right         
    def in_order_rec(self, root):
        if root is None:
            return
        self.in_order_rec(root.left)
        print(root.info,  end=" ")
        self.in_order_rec(root.right)
        
    
    #p=root. definestack, 
    #while stack or p, if p is not None, append(p), p=p.left.  
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
                

     #p=root. definestack, 
    #while stack or p, if p is not None, append(p), p=p.left.  
    #else,p=pop(), if kth==k print return, else kth++ p=p.right
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

                
    #recursive - call with left, call with right, print root.info        
    def post_order_recur(self, root):
        if root is None:
            return
        self.post_order_recur(root.left)
        self.post_order_recur(root.right)
        print(root.info,  end=" ")
        
    #p=root. 
    #while stak or p. if p is not none, append p, p=p.left
    #else p=pop(). 
    #if p.right is not none and p.right not in visited. p = p.right
     #else add p to visited. print p.info. p = None
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

    #add root to queue. pop queue. print info. add left. add right.
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

    
     # two while loops. NodeCount=length(queue) 
     #Break from outer loop when nodeCount==0.
     #Inner while loop, node count is greater than 0. 
     #pop queue, print, add left, add right. decrement nodeCount
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
            
    #place all popped items from queue in stack. 
    #Print all items from stack for reverse
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
            
            
    def printAllAncestorsRecur(self, root,item):
        if root is None:
            return False
        if root.info == item:
            return True
        if self.printAllAncestorsRecur(root.left, item) or \
            self.printAllAncestorsRecur(root.right, item):
                print(root.info, end= ",")
                return True
            
        return False

    #AGGREGATED/SIZE METHODS--------------------------------------------------
    
    #call with left + call with right + 1
    def size_recursive(self, p):
        if p is None:
            return 0
        return self.size_recursive(p.left) + self.size_recursive(p.right) +1 
    
    
    #level order traversal
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
    
    #maxData = root.info.
    #call with left and store result in lres
    #call with right and store result in rres
    #maxData is max of lres, maxData, rres
    def max_rec(self, root):
        if root is None:
            return float("-inf")
        
        maxData = root.info
            
        lres = self.max_rec(root.left)
        rres = self.max_rec(root.right)
        
        maxData = max(max(lres, maxData), max(rres, maxData))
        return maxData
    
    #level order. pop, compare with max and update max.
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

    #max(call with left, call with right) +1
    def height_rec(self, root):
        if root is None:
            return 0
        return max(self.height_rec(root.left), self.height_rec(root.right)) + 1

    #queue. append root. append none.
    #while q pop. 
    #if pop is none. level++. if queue is not empty. append none
    #else: add left add right.
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
    
    #if root.info==date, found. else# call with left. else call with right
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
            
            
    def find_item_iter(self, root, k):
        if root is None:
            return "not found"
        if root.info == k:
            return "found"
        q = []
        q.append(root)
        while q:
            popped = q.pop(0)
            if popped.info == k:
                return "found"
            if popped.left is not None:
                q.append(popped.left)
            if popped.right is not None:
                q.append(popped.right)
    
    #root.info + call with left + call with right
    def sum_of_values_recur(self, root):
        if root is None:
            return 0
        return root.info + self.sum_of_values_recur(root.left) + self.sum_of_values_recur(root.right)    

    #level order. pop and sum all values
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
    
    #level order. Append root append None. 
    #if popped is none. print sum.
        #if queue, append None. level++
    #else sum+popped.  Add left to queue. Add Right to queue.
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
           
    
    #append root, append none
    #if popped is None, sum. if sum > max. set max.
        #if queue, apppend None. level+
    #else sum+popped. add left. add right.
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
    
    #vertical sum of the tree
    #call again with left, -1.
    #add column and value in hashtable.
    #call again with right, +1
    def vertical_sum(self, root, column, dict1):
       
        if root is None:
            return
        
        #call again with left with column -1
        self.vertical_sum(root.left, column-1, dict1)
        
        #add or update dictionary
        if column in dict1:
           dict1[column] += root.info
        else:
           dict1[column] = root.info
           
        #call again with right with column+1
        self.vertical_sum(root.right, column+1, dict1)
        
        
    def is_leaf_node(self, root):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True
        return False
        
    #sum of left nodes
    def sum_of_left_leaves_nodes_rec(self, root):
        res = 0
        if root is not None:
            if self.is_leaf_node(root.left):
                res += root.left.info
            else:
                res += self.sum_of_left_leaves_nodes_rec(root.left)
            res += self.sum_of_left_leaves_nodes_rec(root.right)
        return res
    
    #diameter of the tree
    #left height. right height. left diam, rightdiam. 
    #max of height vs diams
    def diameter_of_tree(self, root):
        if root is None:
            return 0
        lef = self.height_rec(root.left)
        rig = self.height_rec(root.right)
        
        leftdiam = self.diameter_of_tree(root.left)
        rightdiam = self.diameter_of_tree(root.right)
        
        return max(lef + rig+1, max(leftdiam, rightdiam))
    
    #NODE COUNT METHODS-------------------------------------------------------
    
    #level order. while q, pop. if node.left and node.right exist. count
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

    #recursive
    def num_of_full_nodes_rec(self, root):
         if root is None :
             return 0
         res  = 0
         if root.left is not None and root.right is not None:
             res +=1
         res += self.num_of_full_nodes_rec(root.left) + self.num_of_full_nodes_rec(root.right) 
         return res

    #level order. count half nodes 
    #left not none. right none, count++
    #right not none, left none, count++
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
    
    #recursive half nodes
    def num_of_half_nodes_rec(self, root):
         if root is None :
             return 0
         res  = 0
         if root.left is not None and root.right is None:
             res +=1
         if root.right is not None and root.left is None:
             res +=1
             
         res += self.num_of_half_nodes_rec(root.left) + self.num_of_half_nodes_rec(root.right) 
         return res
    
    #level order. while q. pop.
    #right and left are none. count++
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
    
    #recursive leaf node
    def num_of_leaf_nodes_rec(self, root):
         if root is None :
             return 0
         res  = 0
         if root.left is None and root.right is None:
             res +=1             
         res += self.num_of_leaf_nodes_rec(root.left) + self.num_of_leaf_nodes_rec(root.right) 
         return res    
    
    #q, append root. append none.
    #while q, pop. 
    #if popped is none. print count. set count=0. if q, append none. level++
    #else count++, add left, add right.    
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
              
            
    #two while loops. two queues.  
    def average_of_elemts_at_each_level(self, root):
        q = []
        q.append(root)
        
        while q:
            sum1 = count = level = 0
            temp = []
            
            while q:
                p = q.pop(0)
                sum1 += p.info
                count+=1
                level += 1
                
                if p.left is not None:
                    temp.append(p.left)
                if p.right is not None:
                    temp.append(p.right)
            q = temp
            print("Sum at each level : ", level, sum1)
            print("Average at level :", level, sum1 / count)

    def deepest_node(self, root):
        if root is None:
            return
        q = []
        q.append(root)
        while q:
            popped = q.pop(0)
            if popped.left is not None:
                q.append(popped.left)
            if popped.right is not None:
                q.append(popped.right)
        return popped.info


    # VIEWS-------------------------------------------------------------------

    #queue, add root. pop. dict[hd] = popped.info
    #if left, left.hd-1, append. #if right right.hd+1, append.
    def bottom_view(self, root):
        if root is None:
            return
        q = []
        ht = {}
        q.append(root)
        while q:
            popped = q.pop(0)
            hd = popped.hd
            ht[hd] = popped.info
            
            if popped.left is not None:
                popped.left.hd = hd -1
                q.append(popped.left)
                
            if popped.right is not None:
                popped.right.hd = hd + 1
                q.append(popped.right)
        
        print(ht)
        
        
    #q, append root. 
    #two while loops. update max_level with level. decrement count.
    def right_view(self, root):
        if root is None:
            return
        
        q = []
        q.append(root)
        level = 0
        max_level = 0
        print("Right View of the binary Tree is :")
        while q:
            count = len(q)
            level +=1 
            while count != 0:
                popped = q.pop(0)
                if level > max_level:
                    print(popped.info, end=" ")
                    max_level = level
                
                if popped.right is not None:
                    q.append(popped.right)
                if popped.left is not None:
                    q.append(popped.left)
                count -=1
            
            
    def left_view_rec(self, root):
        max_level = [0]
        self.left_view_util(root, 1, max_level)

    def left_view_util(self, root, level,max_level):
        if root is None:
            return
        if max_level[0] < level:
            print(root.info, end=" ")
            max_level[0] = level
        
        self.left_view_util(root.left, level+1, max_level)
        self.left_view_util(root.right, level+1, max_level)
        
    
    #queue, append root. dict. pop. if hd not in ht. add hd=info
    #if left, left.hd-1, append. #if right, right.hd+1, append.
    def top_view(self, root):
        if root is None:
            return
        q = []
        ht = {}
        q.append(root)
        
        while q:
            popped = q.pop(0)
            hd = popped.hd
            
            if hd not in ht:
                ht[hd] = popped.info
            
            if popped.left is not None:
                popped.left.hd = hd-1
                q.append(popped.left)
                
            if popped.right is not None:
                popped.right.hd = hd+1
                q.append(popped.right)
                
        print(ht)
        
    #CONSTRUCTION of other Trees-----------------------------------------------
    def sum_tree(self, root):
        if root is None:
            return 0
        
        old_val = root.info 
        root.info = self.sum_tree(root.left) + self.sum_tree(root.right)
        return root.info + old_val
    
    def convert_to_mirror_of_tree(self, root):
        if root is None:
            return
        if root:
            self.convert_to_mirror_of_tree(root.left)
            self.convert_to_mirror_of_tree(root.right)
            root.left, root.right = root.right,root.left
        return 
        
        
    #VALIDATIOON
    def are_structurally_same_tree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.info == root2.info:
            return True
        return self.are_structurally_same_tree(root1.left, root2.left) and self.are_structurally_same_tree(root1.right, root2.right)


    def are_mirror_of_each_other(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.info != root2.info :
            return False
        return self.are_mirror_of_each_other(root1.left, root2.right) and self.are_mirror_of_each_other(root1.right, root2.left)
#Test:
print("#---------Create Tree instance----------#")
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

print()
print()
print("Print all ancestors of a node")
BT.printAllAncestorsRecur(BT.root, 12)

#Aggregate Methods
print()
print("#----------Aggregated Methods--------------#")
print("Max elem in the BT (recur) is", BT.max_rec(BT.root))
print("Max elem in the BT(iter) is", BT.max_iter())

print()
print("Height of the BT(recur) is ", BT.height_rec(BT.root))
print("Height of the BT(iter) is ", BT.height_iter())

print()
print("Deepest node of the tree iter is", BT.deepest_node(BT.root))

print()
print("Search->Item {} {} in the tree".format(5, BT.find_item_rec(BT.root, 5)))
print("Search->Item {} {} in the tree Iter".format(10, BT.find_item_iter(BT.root, 10)))

print()
print("Sum of all elems (recur) is ", BT.sum_of_values_recur(BT.root))
print("Sum of all elems (iter) is ", BT.sum_of_values_iter())

print()
print("Sum of all left leaves (recur) is ", BT.sum_of_left_leaves_nodes_rec(BT.root))

print()
print("Diameter of the tree is ", BT.diameter_of_tree(BT.root))

print()
BT.sum_at_level()

print()
print("Level with max sum ", BT.level_with_max_sum())

print()
BT.average_of_elemts_at_each_level(BT.root)
print()



dict1 = {}
BT.vertical_sum(BT.root, 0, dict1)
print("Vertical sum for each column is : ")
print(dict1)

#Node Count Methods
print()
print("#----------Node Count Methods--------------#")
print("total nodes of the BT (recur) is", BT.size_recursive(BT.root))
print("total nodes of the BT (iter) is", BT.size_iter())

print()
print("Num of full nodes ", BT.num_of_full_nodes(BT.root))
print("Num of full nodes (recur): ", BT.num_of_full_nodes_rec(BT.root))

print()
print("Num of half nodes ", BT.num_of_half_nodes(BT.root))
print("Num of half nodes (recur): ", BT.num_of_half_nodes_rec(BT.root))
print()
print("Num of leaf nodes ", BT.num_of_leaf_nodes(BT.root))    
print("Num of leaf nodes (recur) ", BT.num_of_leaf_nodes_rec(BT.root))

print()
BT.node_count_at_each_level()



# VIEWS
print("#----------View Methods--------------#")
print("Bottom View of the tree is ")
BT.bottom_view(BT.root)
print()

print("Top View of the tree is ")
BT.top_view(BT.root)
print()

BT.right_view(BT.root)
print()

print()
print("Left View of the tree (recur) is:")
BT.left_view_rec(BT.root)
print()


print()
print("#---------Remove node 4 from the tree------#")
BT.deleteNode(BT.root, 4)
BT.display(BT.root,0)
print()

# CONSTRUCTION METHODS
print("#----------Construction Methods--------------#")
print()
#root = BT.sum_tree(BT.root)  --temporarily commented to test conversion to mirror tree
#BT.display(BT.root, 0)

print()
print("Convert BT tree to its mirror")
BT.convert_to_mirror_of_tree(BT.root)
BT.display(BT.root,0)
print()


print("#----------Create another Tree-------------#")
BT1 = BinaryTree()
BT1.add_iter(BT1.root, 10)
BT1.add_iter(BT1.root, 5)
BT1.add_iter(BT1.root, 15)
BT1.add_iter(BT1.root, 4)
BT1.add_iter(BT1.root, 6)
BT1.add_iter(BT1.root, 12)
BT1.add_iter(BT1.root, 16)

BT1.display(BT1.root,0)
BT1.deleteNode(BT1.root, 4)
print()
print("Node 4 removed. Display Tree again")
BT1.display(BT1.root,0)

print()
print("Are trees structurally the same: ",BT1.are_structurally_same_tree(BT.root, BT1.root))
print()

print()
print("Are trees mirror of each other: ",BT1.are_mirror_of_each_other(BT.root, BT1.root))
print()

#DELETE TREE
print("#----------Deletion Methods--------------#")
print()
root = BT.delete_tree_iter(BT.root)
print("BT Tree deleted")
print()

root = BT1.delete_binary_tree_rec(BT1.root)
print("BT1 Tree deleted")
print()

"""
Output
---------Create Tree instance----------#
#---------Add nodes to the tree----------#

    16

  15

    12

10

    6

  5

    4

#----------Traversal Methods----------------#
PreOrder Traversal (recur) -->10 5 4 6 15 12 16 
PreOrder Traversal (iter) -->10 5 4 6 15 12 16 

InOrder Traversal (recur) -->4 5 6 10 12 15 16 
InOrder Traversal (iter) -->4 5 6 10 12 15 16 
Kth node in InOrder Traversal (iter) -->4 

PostOrder Traversal (recur) -->4 6 5 12 16 15 10 
PostOrder Traversal (iter) -->4 6 5 12 16 15 10 

LevelOrder Traversal -->10 5 15 4 6 12 16 

LevelOrder Traversal line by line
10 
5 15 
4 6 12 16 

Reverse LevelOrder Traversal
16 12 6 4 15 5 10 

Print all ancestors of a node
15,10,
#----------Aggregated Methods--------------#
Max elem in the BT (recur) is 16
Max elem in the BT(iter) is 16

Height of the BT(recur) is  3
Height of the BT(iter) is  3

Deepest node of the tree iter is 16

Search->Item 5 found in the tree
Search->Item 10 found in the tree Iter

Sum of all elems (recur) is  68
Sum of all elems (iter) is  68

Sum of all left leaves (recur) is  16

Diameter of the tree is  5

Sum at level 1 is->10
Sum at level 2 is->20
Sum at level 3 is->38

Sum at  1 is->10
Sum at  2 is->20
Sum at  3 is->38
Level with max sum  3

Sum at each level :  1 10
Average at level : 1 10.0
Sum at each level :  2 20
Average at level : 2 10.0
Sum at each level :  4 38
Average at level : 4 9.5

Vertical sum for each column is : 
{-2: 4, -1: 5, 0: 28, 1: 15, 2: 16}

#----------Node Count Methods--------------#
total nodes of the BT (recur) is 7
total nodes of the BT (iter) is 7

Num of full nodes  3
Num of full nodes (recur):  3

Num of half nodes  0
Num of half nodes (recur):  0

Num of leaf nodes  4
Num of leaf nodes (recur)  4

Node Count at level  1 is->1
Node Count at level  2 is->2
Node Count at level  3 is->4
#----------View Methods--------------#
Bottom View of the tree is 
{0: 12, -1: 5, 1: 15, -2: 4, 2: 16}

Top View of the tree is 
{0: 10, -1: 5, 1: 15, -2: 4, 2: 16}

Right View of the binary Tree is :
10 15 16 

Left View of the tree (recur) is:
10 5 4 

#---------Remove node 4 from the tree------#

    16

  15

    12

10

    6

  5

#----------Construction Methods--------------#


Convert BT tree to its mirror

  5

    6

10

    12

  15

    16

#----------Create another Tree-------------#

    16

  15

    12

10

    6

  5

    4

Node 4 removed. Display Tree again

    16

  15

    12

10

    6

  5

Are trees structurally the same:  True


Are trees mirror of each other:  True

#----------Deletion Methods--------------#

BT Tree deleted

BT1 Tree deleted
"""