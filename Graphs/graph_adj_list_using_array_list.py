#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:15:20 2018

@author: kdp
"""

#References to the vertices are stored in a graph array with an initil capacity of 16
#When the filled slots in the array are greater than the load factor, a new temp graph array is created. 
#Vertices and Edges are copied from original to temp. Temp is made as the primary graph

class Vertex_Node:
    #vertices will be associated with linked list of vertex
    #edges between vertices will be associated with linked list of edges
    def __init__(self, data):
        self.vertex_value = data
        self.first_edge = None
        
class Edge_Node:
    #edges between vertices will be associated with linked list of edges
    def __init__(self, v, w):
        self.end_vertex = v
        self.next_edge = None
        self.weight  = w
        
class Adj_List_Graph:
    
    def __init__(self, size=16):
        self.graph_size =  size
        self.graph = [None] * self.graph_size
        self.vertex_count = 0
        self.edge_count = 0
        self.load_factor = 0.75
        
    def insert_vertex(self, val):
        
        if self.vertex_count/self.graph_size >= self.load_factor:
            self.resize_graph(self.next_prime(2*self.graph_size))
            
        self._insert_vertex(self.vertex_count+1, val)
        
        
    def _insert_vertex(self, next_loctation, val):
        
        new_vertex_node = Vertex_Node(val)
        
        #store the new vertex as the next location (which is vertex_count+1)
        for v in range(next_loctation, self.graph_size):
            if self.graph[v] is None:
                self.graph[v] = new_vertex_node
                self.vertex_count += 1
                return
            else:
                if self.graph[v].vertex_value == val:
                    print("vertex already exist")
                    return
    
    def insert_edge(self, val1, val2, weight):
        
        if val1 == val2:
            print("Start and End Vertex are same")
            return
        
        u = self.find_vertex(val1)
        v = self.find_vertex(val2)
        
        if u is None:
            print("Start vertex not present")
            return
        if v is None:
            print("End vertex not present")
            return
        
        new_edge = Edge_Node(v, weight)
        
        if u.first_edge is None:
            u.first_edge = new_edge
            self.edge_count += 1
        else:
            e = u.first_edge
            while e.next_edge is not None:
                if e.end_vertex.vertex_value == val2:
                    print("Edge already present")
                    return
                e = e.next_edge
            if e.end_vertex.vertex_value == val2:
                print("Edge already present")
                return
            e.next_edge = new_edge
            self.edge_count += 1
                
        
    def delete_vertex(self, val):
        self.delete_from_edge_list(val)
        self.delete_from_vertex_list(val)
    
    def delete_from_edge_list(self, val):
               
        for i in range(0, self.graph_size):
            v = self.graph[i]
            if v is not None:
                if v.first_edge is None:
                    continue
            
                if v.first_edge.end_vertex.vertex_value == val:
                    v.first_edge = v.first_edge.next_edge
                    self.edge_count -=1
                else:
                    q = v.first_edge
                    while q.next_edge is not None:
                        if q.next_edge.end_vertex.vertex_value == val:
                            q.next_edge = q.next_edge.next_edge
                            self.edge_count -=1
                            break
                        q = q.next_edge
                    
    def delete_from_vertex_list(self, val):
        
        for v in range(0, self.graph_size):
            if self.graph[v] is not None:
                if self.graph[v].vertex_value == val:
                    q = self.graph[v].first_edge
                    while q is not None:
                        self.edge_count -= 1
                        self.graph[v] = None
                        q = q.next_edge
                        self.vertex_count -= 1
                        return
        
    def find_vertex(self, val):
        
        for v in range(0, self.graph_size):
            if self.graph[v] is not None:
                if self.graph[v].vertex_value == val:
                    return self.graph[v]  #address of vertex node
        return None
            
    
    def delete_edge(self, val1, val2):
        
        v = self.find_vertex(val1)
        
        if v is None:
            print("Start vertex not present")
            return
        
        if v.first_edge is None:
            print("Edge not present")
            return
        
        #first edge
        if v.first_edge.end_vertex.vertex_value == val2:
            v.first_edge = v.first_edge.next_edge
            self.edge_count -= 1
            return
        
        q = v.first_edge  #address of the first edge node
        while q.next_edge is not None:
            if q.next_edge.end_vertex.vertex_value == val2:
                q.next_edge = q.next_edge.next_edge
                self.edge_count -= 1
                return
            q = q.next_edge
        print("Edge not present")
        
    # number of edges going out from a vertex
    def outdegree_of_a_vertex(self, val):
        
        v = self.find_vertex(val)
        if v is None:
            raise Exception("Vertex not present")
            
        out = 0
        q = v.first_edge
        while q is not None:
            q = q.next_edge
            out += 1
        return out
    
    
    def indegree_of_a_vertex(self, val):
               
       in_deg = 0       
       for v in range(0, self.graph_size):
           if self.graph[v] is not None:
               q = self.graph[v].first_edge
               while q is not None:
                   if q.end_vertex.vertex_value == val:
                       in_deg += 1
                   q=q.next_edge
       return in_deg

    def display_graph(self):
        
        for v in range(0, self.graph_size):
            if self.graph[v] is not None:
                print("[", end="")
                print(self.graph[v].vertex_value, end="")
                print("]-->", end="")
                q = self.graph[v].first_edge
                while q is not None:
                    print(str(q.end_vertex.vertex_value) + "(" + str(q.weight) + ")", end="-->")
                    q = q.next_edge
                print("None")
            
        print()
        print("Total Vertices :", self.vertex_count)
        print("Total Edges :", self.edge_count)
        print("#-------------------------------------------#")


    def resize_graph(self, new_size):
        temp = Adj_List_Graph(new_size) #new instance of a class
              
        for i in range(0, self.graph_size): #copy from orig to temp
            if self.graph[i] is not None:
                temp._insert_vertex(i, self.graph[i].vertex_value)
                
        for i in range(0, self.graph_size): #copy from orig to temp
            if self.graph[i] is not None:
                if self.graph[i].first_edge is not None:
                    q = self.graph[i].first_edge
                    while q is not None:
                        temp.insert_edge(self.graph[i].vertex_value, q.end_vertex.vertex_value, q.weight)
                        q = q.next_edge
         
   
        self.graph = temp.graph     #make temp graph as orig
        self.graph_size = temp.graph_size  #set new size to graph_size
        
    def next_prime(self, x):    #gives the next prime num of x. x is 2*heap_size
        while self.is_prime(x) is not True:
            x = x+1
        return x
    
    def is_prime(self, x):
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True   

#Test         
G = Adj_List_Graph()

# INSERT VERTICES METHODS
G.insert_vertex("abc")      #shown
G.insert_vertex("xyz")      #shown
G.insert_vertex("lmn")     #shown
G.insert_vertex("pqr")      #shown

# INSERT EDGE with weights 
G.insert_edge("xyz", "pqr", 5)    #not shown
G.insert_edge("xyz", "abc", 4)    #shown
G.insert_edge("pqr", "abc", 4)   #shown
G.insert_edge("lmn", "abc", 3)   #shown
G.insert_edge("lmn", "xyz", 1)   #shown
G.insert_edge("lmn", "pqr", 0)   #not shown

G.display_graph()

print()
print("Outdegree of vertex lmn is", G.outdegree_of_a_vertex("lmn"))
print("Indegree of vertex lmn is", G.indegree_of_a_vertex("lmn"))

print("Outdegree of vertex pqr is", G.outdegree_of_a_vertex("pqr"))
print("Indegree of vertex pqr ", G.indegree_of_a_vertex("pqr"))
print("#---------------------------------------------#")

print()

# INSERT METHODS 
print("Insert additional new vertex and add edges")
G.insert_vertex("tuv") 

G.insert_edge("abc", "tuv", 2)   #not shown
G.insert_edge("tuv", "pqr", -1)  #showb

G.display_graph()

G.insert_vertex("acb") #shown
G.insert_vertex("bca") #shown

G.display_graph()

G.insert_vertex(123)  #shown
G.insert_vertex(456)  #shown

G.insert_edge(123, "tuv", 2)   #shown
G.insert_edge("acb", 123, -1)  #shown
G.insert_edge(123, 456, 2)     #shown
G.insert_edge("acb", "bca", -1)  #shown


G.insert_vertex("xxx")   #shown
G.insert_vertex("yyy")   #shown
G.insert_vertex("zzz")   #shown
G.insert_vertex("ket")   #shown
G.insert_vertex("efr")   #shown
G.insert_vertex("dul")   #shown

G.insert_edge("xxx", "tuv", 2)  #shown
G.insert_edge("efr", "dul", -1) #shown


G.display_graph()
print()

#DELETE VERTEX METHOD
print("Delete Vertex test")
G.delete_vertex("abc")
G.display_graph()
print()

# DELETE EDGE METHOD
print("Delete Edge test")
G.delete_edge("xyz", "pqr")
G.display_graph()


"""
[abc]-->None
[xyz]-->pqr(5)-->abc(4)-->None
[lmn]-->abc(3)-->xyz(1)-->pqr(0)-->None
[pqr]-->abc(4)-->None

Total Vertices : 4
Total Edges : 6
#-------------------------------------------#

Outdegree of vertex lmn is 3
Indegree of vertex lmn is 0
Outdegree of vertex pqr is 1
Indegree of vertex pqr  2
#---------------------------------------------#

Insert additional new vertex and add edges
[abc]-->tuv(2)-->None
[xyz]-->pqr(5)-->abc(4)-->None
[lmn]-->abc(3)-->xyz(1)-->pqr(0)-->None
[pqr]-->abc(4)-->None
[tuv]-->pqr(-1)-->None

Total Vertices : 5
Total Edges : 8
#-------------------------------------------#
[abc]-->tuv(2)-->None
[xyz]-->pqr(5)-->abc(4)-->None
[lmn]-->abc(3)-->xyz(1)-->pqr(0)-->None
[pqr]-->abc(4)-->None
[tuv]-->pqr(-1)-->None
[acb]-->None
[bca]-->None

Total Vertices : 7
Total Edges : 8
#-------------------------------------------#
[abc]-->tuv(2)-->None
[xyz]-->pqr(5)-->abc(4)-->None
[lmn]-->abc(3)-->xyz(1)-->pqr(0)-->None
[pqr]-->abc(4)-->None
[tuv]-->pqr(-1)-->None
[acb]-->123(-1)-->bca(-1)-->None
[bca]-->None
[123]-->tuv(2)-->456(2)-->None
[456]-->None
[xxx]-->tuv(2)-->None
[yyy]-->None
[zzz]-->None
[ket]-->None
[efr]-->dul(-1)-->None
[dul]-->None

Total Vertices : 15
Total Edges : 14
#-------------------------------------------#

Delete Vertex test
[xyz]-->pqr(5)-->None
[lmn]-->xyz(1)-->pqr(0)-->None
[pqr]-->None
[tuv]-->pqr(-1)-->None
[acb]-->123(-1)-->bca(-1)-->None
[bca]-->None
[123]-->tuv(2)-->456(2)-->None
[456]-->None
[xxx]-->tuv(2)-->None
[yyy]-->None
[zzz]-->None
[ket]-->None
[efr]-->dul(-1)-->None
[dul]-->None

Total Vertices : 14
Total Edges : 10
#-------------------------------------------#

Delete Edge test
[xyz]-->None
[lmn]-->xyz(1)-->pqr(0)-->None
[pqr]-->None
[tuv]-->pqr(-1)-->None
[acb]-->123(-1)-->bca(-1)-->None
[bca]-->None
[123]-->tuv(2)-->456(2)-->None
[456]-->None
[xxx]-->tuv(2)-->None
[yyy]-->None
[zzz]-->None
[ket]-->None
[efr]-->dul(-1)-->None
[dul]-->None

Total Vertices : 14
Total Edges : 9
#-------------------------------------------#

"""



    
        
    
        