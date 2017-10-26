# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 19:36:20 2016

@author: Nathalie
"""

from AlgoPy import graph

def dfsSuff(G, s, M, L):
    M[s] = True
    for adj in G.adjLists[s]:
        if not M[adj]:
            dfsSuff(G, adj, M, L)
    L.insert(0, s)

def topologicalOrder(G):
    M = [False] * G.order
    L = []
    for s in range(G.order):
        if not M[s]:
            dfsSuff(G, s, M, L)
    return L
    
def testTopologicalOrder(G, L):
    M = [False]*G.order
    while L != []:
        s = L.pop()
        for adj in G.adjLists[s]:
            if not M[adj]:
                return False
        M[s] = True
    return True