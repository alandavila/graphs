# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:45:28 2016

@author: alan
"""

class Graph:
    '''
    Undirected Graph class. 
    '''
    
    def __init__(self):
        self.nodes = {}
        self.V = 0
        self.E = 0
    
    def add_edge(self, fromNode, toNode, weight = 0.):
        '''
        Adds fromNode to graph if it does not exits.
        Adds toNode to graph if it does not exist
        Adds edge to Graph with a given weight, 0. is default
        Edge goes both ways fromNode --> toNode and toNode --> fromNode
        
        Parameters:
        -----------
        fromNode: int
            First node form the edge to add to the graph
        toNode: int
            Second node from edge to add to the graph
        weight: float
            Weight of tthe edge
            
        Returns:
        ---------
            NA
        '''
        #no edges to self node allowed
        if fromNode == toNode:
            return
            
        if fromNode not in self.nodes:
            self.nodes[fromNode] = {}
            self.V +=1
        
        if toNode not in self.nodes:
            self.nodes[toNode] = {}
            self.V +=1

        overriddingEdge = False
        if fromNode in self.nodes:
            if toNode in self.nodes[fromNode]:
                overriddingEdge = True
        
        if not overriddingEdge:
            self.E +=1
        
        self.nodes[fromNode][toNode] = weight
        self.nodes[toNode][fromNode] = weight
        

if __name__ == '__main__':
    
    numNodes = 10

    graph = Graph()
    graph2 = Graph()
    for i in range(numNodes):
        for j in range(i, numNodes):
            graph.add_edge(i, j , i*j)
            
    for i in range(numNodes):
        for j in range(numNodes):
            graph2.add_edge(i, j , i*j)

    for i in range(graph.V):
        for edge in graph.nodes[i]:
            if graph.nodes[i][edge] != graph2.nodes[i][edge]:
                print('error in undirected graph')
                
    assert(numNodes == graph.V)
    assert(graph.V == graph2.V)
    assert((numNodes*(numNodes - 1)*0.5) == graph.E)
    assert(graph.E == graph2.E)