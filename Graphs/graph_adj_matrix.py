#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:45:01 2018

@author: kdp
"""

class Vertex:
    
    def __init__(self, val):
        self.vertex_value = val
        self.state = None
        
    
class Adj_Matx_Graph:
    
    def __init__(self, size):
        self.graph_size = size
        self.graph = [[0] * self.graph_size for i in range(self.graph_size)]
        self.vertex_list = [None] * self.graph_size
        self.vertex_count = 0
        self.edge_count = 0
        
        self.INITIAL = 0
        self.WAITING = 1
        self.VISITED = 2
        
    #vertices are maintained in a list/array
    def insert_vertex(self, val):
        
        self.vertex_list[self.vertex_count] = Vertex(val)
        self.vertex_count += 1
    
        #i will represent the row/colum of the matrix matching the val
    #the edges are maintained in the matrix
    def get_index(self, val):
        
        for i in range(0, self.vertex_count):
            if self.vertex_list[i].vertex_value == val:
                return i
        else:
            raise Exception ( "Invalid Vertex")
            
    def edge_exists(self,val1, val2):
        return self.is_adjacent(self.get_index(val1), self.get_index(val2))
                                
    def is_adjacent(self, u, v):
        return self.graph[u][v]
    
    def insert_edge_directed_unweighted(self, val1, val2):
        
        u = self.get_index(val1)
        v = self.get_index(val2)
        if u == v:
            raise Exception ("Not a valid Edge")
        if self.graph[u][v] == 1:
            print("Edge already present")
        else:
            self.graph[u][v] = 1
            self.edge_count +=1 
            
    def insert_edge_directed_weighted(self, val1, val2, weight):
        
        u = self.get_index(val1)
        v = self.get_index(val2)
        if u == v:
            raise Exception ("Not a valid Edge")
        if self.graph[u][v] != 0:
            print("Edge already present")
        else:
            self.graph[u][v] = weight
            self.edge_count +=1         
    
    
    def insert_edge_undirected_unweighted(self, val1, val2):
        
        u = self.get_index(val1)
        v = self.get_index(val2)
        if u == v:
            raise Exception ("Not a valid Edge")
        if self.graph[u][v] == 1:
            print("Edge already present")
        else:
            self.graph[u][v] = 1
            self.graph[v][u] = 1
            self.edge_count +=1         
            
    def insert_edge_undirected_weighted(self, val1, val2, weight):
        
        u = self.get_index(val1)
        v = self.get_index(val2)
        if u == v:
            raise Exception ("Not a valid Edge")
        if self.graph[u][v] == 1:
            print("Edge already present")
        else:
            self.graph[u][v] = weight
            self.graph[v][u] = weight
            self.edge_count +=1     

            
    def delete_edge_directed(self, val1, val2):
        
        u = self.get_index(val1)
        v = self.get_index(val2)
        
        if self.graph[u][v] == 0:
            print("Edge not present in the graph")
        else:
            self.graph[u][v] = 0
            self.edge_count -= 1
            
        
    def out_degree(self, val1):
        
        u = self.get_index(val1)
        
        out = 0
        for v in range(self.graph_size):
            if self.graph[u][v]:
                out += 1
        return out
        
    def in_degree(self, val1):
        
        u = self.get_index(val1)
        
        in1 = 0
        for v in range(0, self.graph_size):
            if self.graph[v][u]:
                in1 += 1
        return in1
    
    def display(self):
        
        m = len(self.graph)
        n = len(self.graph)
        
        for i in self.vertex_list:
            print("{0:5s}".format(i.vertex_value), end="")
        print()
        for i in range(n):
            for j in range(m):
                print("{0:3d}".format(self.graph[i][j]), end="  ")
            print()
            
    def bfs_traversal(self, start_vertex):
        
        for v in range(0, self.graph_size):
            self.vertex_list[v].state = self.INITIAL
        
        print("\nBFS Traversal is ", end=" ")
        s = self.get_index(start_vertex)
        self._bfs(s)
        
        #this takes care of vertices that are not reachable from vertex[0]
        for v in range(0, len(self.vertex_list)): 
            if self.vertex_list[v].state == self.INITIAL:
                self._bfs(v)
                
        
    def _bfs(self, v):
        qu = []
        qu.append(v)
        self.vertex_list[v].state = self.WAITING
        
        while qu:
            v = qu.pop(0)           
            print(self.vertex_list[v].vertex_value, end= " ")
            self.vertex_list[v].state = self.VISITED
            
            for i in range(0, self.vertex_count):
                if self.is_adjacent(v,i) and self.vertex_list[i].state == self.INITIAL:
                    qu.append(i)
                    self.vertex_list[i].state = self.WAITING
    
#Test:

print("Graph - Adjacency Matrix")            
            
print("#---------------------------#")
print("Directed -- Unweighted")
print()
G = Adj_Matx_Graph(4)

G.insert_vertex("abc")
G.insert_vertex("xyz")
G.insert_vertex("lmn")
G.insert_vertex("pqr")

G.insert_edge_directed_unweighted("abc", "xyz")
G.insert_edge_directed_unweighted("xyz", "pqr")
G.insert_edge_directed_unweighted("abc", "pqr")
G.insert_edge_directed_unweighted("lmn", "xyz")

G.display()
print()
print("Total Vertices:",  G.vertex_count)
print("Total Edges:", G.edge_count)

print()
print("Outdegree of abc is :", G.out_degree("abc"))
print("Indgree of abc is :", G.in_degree("abc"))

#pass vertex value from where traversal should begin
G.bfs_traversal("lmn")

#Test 2
print()
print("#---------------------------#")
print("Directed -- Weighted")
print()
G1 = Adj_Matx_Graph(4)

G1.insert_vertex("LAX")
G1.insert_vertex("SFO")
G1.insert_vertex("PHX")
G1.insert_vertex("DEN")

G1.insert_edge_directed_weighted("LAX", "SFO", 300)
G1.insert_edge_directed_weighted("SFO", "PHX", 600)
G1.insert_edge_directed_weighted("PHX", "LAX", 200)
G1.insert_edge_directed_weighted("DEN", "LAX", 500)

G1.display()
print()
print("Total Vertices:",  G1.vertex_count)
print("Total Edges:", G1.edge_count)

print()
print("Outdegree of LAX is :", G1.out_degree("LAX"))
print("Indgree of LAX is :", G1.in_degree("LAX"))

G1.bfs_traversal("SFO")
print()

#Test 3

print("#---------------------------#")
print("Un-directed -- un-weighted")
print()
G2 = Adj_Matx_Graph(4)

G2.insert_vertex("LAX")
G2.insert_vertex("SFO")
G2.insert_vertex("PHX")
G2.insert_vertex("DEN")

G2.insert_edge_undirected_unweighted("LAX", "SFO")
G2.insert_edge_undirected_unweighted("SFO", "PHX")
G2.insert_edge_undirected_unweighted("PHX", "LAX")
G2.insert_edge_undirected_unweighted("DEN", "LAX")

G2.display()
print()
print("Total Vertices:",  G2.vertex_count)
print("Total Edges:", G2.edge_count)

print()
print("Outdegree of LAX is :", G2.out_degree("LAX"))
print("Indgree of LAX is :", G2.in_degree("LAX"))

G2.bfs_traversal("PHX")
print()
#Test 4

print("#---------------------------#")
print("Un-directed -- weighted")
print()
G3 = Adj_Matx_Graph(4)

G3.insert_vertex("LAX")
G3.insert_vertex("SFO")
G3.insert_vertex("PHX")
G3.insert_vertex("DEN")

G3.insert_edge_undirected_weighted("LAX", "SFO", 400)
G3.insert_edge_undirected_weighted("SFO", "PHX", 600)
G3.insert_edge_undirected_weighted("PHX", "LAX", 300)
G3.insert_edge_undirected_weighted("DEN", "LAX", 800)

G3.display()
print()
print("Total Vertices:",  G3.vertex_count)
print("Total Edges:", G3.edge_count)

print()
print("Outdegree of LAX is :", G3.out_degree("LAX"))
print("Indgree of LAX is :", G3.in_degree("LAX"))

G3.bfs_traversal("DEN")
print()

"""
#------Output---------#


Graph - Adjacency Matrix
#---------------------------#
Directed -- Unweighted

abc  xyz  lmn  pqr  
  0    1    0    1  
  0    0    0    1  
  0    1    0    0  
  0    0    0    0  

Total Vertices: 4
Total Edges: 4

Outdegree of abc is : 2
Indgree of abc is : 0

BFS Traversal is  lmn xyz pqr abc 
#---------------------------#
Directed -- Weighted

LAX  SFO  PHX  DEN  
  0  300    0    0  
  0    0  600    0  
200    0    0    0  
500    0    0    0  

Total Vertices: 4
Total Edges: 4

Outdegree of LAX is : 1
Indgree of LAX is : 2

BFS Traversal is  SFO PHX LAX DEN 
#---------------------------#
Un-directed -- un-weighted

LAX  SFO  PHX  DEN  
  0    1    1    1  
  1    0    1    0  
  1    1    0    0  
  1    0    0    0  

Total Vertices: 4
Total Edges: 4

Outdegree of LAX is : 3
Indgree of LAX is : 3

BFS Traversal is  PHX LAX SFO DEN 
#---------------------------#
Un-directed -- weighted

LAX  SFO  PHX  DEN  
  0  400  300  800  
400    0  600    0  
300  600    0    0  
800    0    0    0  

Total Vertices: 4
Total Edges: 4

Outdegree of LAX is : 3
Indgree of LAX is : 3

BFS Traversal is  DEN LAX SFO PHX 
"""
