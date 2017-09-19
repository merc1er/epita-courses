# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:23:37 2016
@author: Nathalie
"""

from AlgoPy import queue
from AlgoPy import graph
#import nathDot

def buildSubGraph(G, s, n):
    '''
    build a subGraph from 
    S' = vertices reached by s with a path of longer at most n
    '''
    map = [None] * G.order
    dist = [-1] * G.order
    NG = graph.Graph(1)
    dist[s] = 0
    map[s] = 0
    q = queue.Queue()
    q = queue.enqueue(s, q)
    while not queue.isEmpty(q):
        s = queue.dequeue(q)
        for adj in G.adjLists[s]:
            if (dist[adj] == -1) and (dist[s] < n):       
                dist[adj] = dist[s] + 1
                map[adj] = NG.order
                NG.order += 1
                NG.adjLists.append([])
                q = queue.enqueue(adj, q)
            if dist[adj] != -1:
                NG.adjLists[map[s]].append(map[adj])
    return(NG, dist, map)
    
def test():
    G = graph.loadGRA("files/graphG6.gra")
    for i in range(G.order):
        G.adjLists[i].sort()
        
    (NG, dist, map) = buildSubGraph(G, 4, 2)
    print(dist)
    print(map)
#    nathDot.viewDot(graph.toDot(NG))