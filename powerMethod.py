# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 18:59:36 2020

@author: Khabir
"""

import matplotlib.patches as mpatches
from NeededModulesP1 import transitionProbabilities
import numpy as np
import matplotlib.pyplot as plt

numTrials = 100000

#Using the medium.txt file
myfile = 'medium.txt'
#myfile = input("Please enter the name of the file: ")
transitionMatrix = transitionProbabilities(myfile)[0]
N = int(transitionProbabilities(myfile)[1])
ranks = np.zeros(N)
ranks[0] = 1 
transitionMatrixTransposed = transitionMatrix.transpose()
for i in range(numTrials):
    ranks_prime = np.zeros(N)
    for j in range(N):
        for w in range(N):
            ranks_prime[j] = ranks_prime[j] + ranks[w] * transitionMatrix[w,j]
    mranks = ranks_prime            
valuesm = np.arange(N)




rank_medium = plt.bar(valuesm,mranks)
plt.xlabel('Nodes')
plt.ylabel('Probabilities')
plt.title('Power Method With Multiple link effect')

plt.show()
