# -*- coding: utf-8 -*-
"""
Created on Nov. 2016
@author: Nathalie
"""

from AlgoPy import graph
from AlgoPy import queue

# 3.1 bipartite: can be done with both traversals


def __bipartite(G, s, Set):
    for adj in G.adjLists[s]:
        if Set[adj] == 0:
            Set[adj] = -Set[s]
            if not __bipartite(G, adj, Set):
                return False
        else:
            if Set[adj] == Set[s]:
                return False
    return True

# just to show: studentsdon't have to do it

def __bipartiteBFS(G, s, Set):
    q = queue.Queue()
    q = queue.enqueue(s, q)
    Set[s] = 1  # can also be done here!
    while not queue.isEmpty(q):
        s = queue.dequeue(q)
        for adj in G.adjLists[s]:
            if Set[adj] == 0:       
                Set[adj] = -Set[s]
                q = queue.enqueue(adj, q)
            else:
                if Set[adj] == Set[s]:
                    return False                
    return True
    
def bipartite(G):
    Set = [0] * G.order
    for s in range(G.order):
        if Set[s] == 0:
            Set[s] = 1  # here if DFS
            if not __bipartite(G, s, Set):
                return False
    return True
