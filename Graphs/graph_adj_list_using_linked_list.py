#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:15:20 2018

@author: kdp
"""
class Vertex_Node:
    #vertices will be associated with linked list of vertex
    #edges between vertices will be associated with linked list of edges
    def __init__(self, data):
        self.vertex_value = data
        self.next_vertex = None
        self.first_edge = None
        
        
class Edge_Node:
    #edges between vertices will be associated with linked list of edges
    def __init__(self, v):
        self.end_vertex = v
        self.next_edge = None
        
class Adj_List_Graph:
    
    def __init__(self):
        self.start = None
        self.vertex_count = 0
        self.edge_count = 0
        
    def insert_vertex(self, val):
        
        new_vertex_node = Vertex_Node(val)
        
        if self.start is None:
            self.start = new_vertex_node
        else:
            v = self.start
            while v.next_vertex is not None:
                if v.vertex_value == val:
                    print("vertex already exist")
                    return
                v = v.next_vertex
            if v.vertex_value == val:
                print("Vertex already exist")
                return
            v.next_vertex = new_vertex_node
        self.vertex_count += 1
                
    
    def insert_edge(self, val1, val2):
        
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
        
        new_edge = Edge_Node(v)
        
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
       
        v = self.start
        while v is not None:
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
                    
            v = v.next_vertex
    
    
    def delete_from_vertex_list(self, val):
        
        if self.start is None:
            print("No vertices to delete")
            return
        
        if self.start.vertex_value == val:
            q = self.start.first_edge
            while q is not None:
                self.edge_count -= 1
                self.start = self.start.next_vertex
                q = q.next_edge
                self.vertex_count -= 1
        else:
            v = self.start
            while v.next_vertex is not None:
                
                if v.next_vertex.vertex_value == val:
                    break
                v = v.next_vertex
                
            if v.next_vertex is None:
                print("vertex not found")
                return
            else:
                q = v.next_vertex.first_edge
                while q is not None:
                    
                    self.edge_count -= 1
                    q = q.next_edge
                v.next_vertex = v.next_vertex.next_vertex
                self.vertex_count -= 1
                
                
    def find_vertex(self, val):
        
        v = self.start
        while v is not None:
            if v.vertex_value == val:
                return v
            v = v.next_vertex
        return None
            
    
    def delete_edge(self, val1, val2):
        
        v = self.find_vertex(val1)
        
        if v is None:
            print("Start vertex not present")
            return
        
        if v.first_edge is None:
            print("Edge not present")
            return
        
        if v.first_edge.end_vertex.vertex_value == val2:
            v.first_edge = v.first_edge.next_edge
            self.edge_count -= 1
            return
        
        q = v.first_edge
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
         
       u = self.find_vertex(val)
       if u is None:
            raise Exception("Vertex not present")
       in_deg = 0
       v = self.start
       while v is not None:
           q = v.first_edge
           while q is not None:
               if q.end_vertex.vertex_value == val:
                   in_deg += 1
               q=q.next_edge
           v = v.next_vertex
       return in_deg

    def display_graph(self):
        
        v = self.start
        while v is not None:
            print("[", end="")
            print(v.vertex_value, end="")
            print("]-->", end="")
            q = v.first_edge
            while q is not None:
                print(q.end_vertex.vertex_value, end="->")
                q = q.next_edge
            print("None")
            v = v.next_vertex

#Test
         
G = Adj_List_Graph()

G.insert_vertex("abc")
G.insert_vertex("xyz")
G.insert_vertex("lmn")
G.insert_vertex("pqr")

G.insert_edge("xyz", "pqr")
G.insert_edge("xyz", "abc")
G.insert_edge("pqr", "abc")
G.insert_edge("lmn", "abc")
G.insert_edge("lmn", "xyz")
G.insert_edge("lmn", "pqr")

G.display_graph()
print()

print("Outdegree of vertex lmn is", G.outdegree_of_a_vertex("lmn"))
print("Indegree of vertex lmn is", G.indegree_of_a_vertex("lmn"))

print("Outdegree of vertex pqr is", G.outdegree_of_a_vertex("pqr"))
print("Indegree of vertex pqr ", G.indegree_of_a_vertex("pqr"))

print()

G.insert_vertex("tuv") 
G.insert_edge("abc", "tuv")
G.insert_edge("tuv", "pqr")

G.display_graph()

print()
G.delete_vertex("abc")
G.display_graph()

print()

G.delete_edge("xyz", "pqr")
G.display_graph()


"""
#----------Output--------------#

[abc]-->None
[xyz]-->pqr->abc->None
[lmn]-->abc->xyz->pqr->None
[pqr]-->abc->None

Outdegree of vertex lmn is 3
Indegree of vertex lmn is 0
Outdegree of vertex pqr is 1
Indegree of vertex pqr  2

[abc]-->tuv->None
[xyz]-->pqr->abc->None
[lmn]-->abc->xyz->pqr->None
[pqr]-->abc->None
[tuv]-->pqr->None

[xyz]-->pqr->None
[lmn]-->xyz->pqr->None
[pqr]-->None
[tuv]-->pqr->None

[xyz]-->None
[lmn]-->xyz->pqr->None
[pqr]-->None
[tuv]-->pqr->None

"""



    
        
    
        