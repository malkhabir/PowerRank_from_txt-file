# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:51:40 2020

@author: Khabir
"""

import numpy as np 



def adjMatrixFromFile(myfile):
    
    t = []
    
    with open(eval('myfile'), 'r') as f:
        N = f.readline()
        for l in f:
            l = list(map(int, l.split()))
            for i in range(0, len(l)-1, 2):
                t.append([l[i], l[i+1]])
    
    #Getting the size 
    size = max(max(t)) + 1
     
    # make an empty adjacency list  
    adjacency = [[0]*size for j in range(size)]
    
    # populating the list for each edge
    for m, n in t:
        adjacency[m][n] = 1
    adjacencyMatrix = np.array(adjacency)
    
    return adjacencyMatrix, N



def outDegree(myfile):
    adj = adjMatrixFromFile(myfile)
    outDegrees = np.sum(adj[0], axis = 1, keepdims= True)
    
    return outDegrees





def transitionProbabilities(myfile):
    adja = adjMatrixFromFile(myfile)
    adjacencyMatrix = adja[0]
    N = adja[1]
    outDegrees = outDegree(myfile)
    # transitionMatrix = np.zeros_like(adjacencyMatrix)
    
    transitionMatrix = 0.90 * ((adjacencyMatrix)/outDegrees) + (0.1 / float(N))
    
    return transitionMatrix,N



if __name__ == "randomCrawler":
    imp = __import__("NeededModulesP3")
    print ("Function cheks out with no problem")
        