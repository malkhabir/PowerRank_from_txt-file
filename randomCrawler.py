# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:58:45 2020

@author: Khabir
"""
import matplotlib.patches as mpatches
from NeededModulesP1 import transitionProbabilities
import numpy as np
import random
import matplotlib.pyplot as plt

#tiny
myfile = 'tiny.txt'
#myfile = input("Please enter the name of the file: ")

transitionMatrix = transitionProbabilities(myfile)[0]
N = int(transitionProbabilities(myfile)[1])


def modCrawler(numTrials):
    
    p = transitionMatrix
    hits = np.zeros(N) #count of hit on a  webpage by thercrawler
    page = 0 #Origin
    
    for i in range(numTrials):
        r = random.random() #Crawler makes one random move
        total = 0
        for j in range(0, N):
            total = total + p[page,j]
            if r < total:
                page = j
                break
        hits[page] = hits[page] + 1
    
    
    
    hits = hits / numTrials
    
    
    return hits
#Tiny
rank =  modCrawler(100000) #rank of the tiny.txt
values = np.arange(N)

#Medium
myfile = 'medium.txt'
transitionMatrix = transitionProbabilities(myfile)[0]
N = int(transitionProbabilities(myfile)[1])
rankM = modCrawler(100000)
valuesM = np.arange(N)


#CHecking
# print(rank)
# print(rankM)

rank_tiny = plt.bar(values,rank)
rank_medium = plt.bar(valuesM,rankM)
plt.xlabel('Node #')
plt.ylabel('Probabilities')
plt.title('Random Crawler Method with Multiple link effect')

or_patch = mpatches.Patch(color='orange', label='medium.txt')
bl_patch = mpatches.Patch(color='blue', label='tiny.txt')
plt.legend(handles=[or_patch],loc='upper right')
plt.legend(handles=[bl_patch],loc='lower right')

plt.show()
