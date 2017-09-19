# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:05:18 2016

@author: Nathalie

search for a path from src to dst
return a list with vertices in the path found (empty if no path)
"""

from AlgoPy import graph
from AlgoPy import queue

# search for a path with a bfs
# uses the parent vector 

def __pathBFS(G, src, dst, p):
    q = queue.Queue()
    q = queue.enqueue(src, q)
    p[src] = -1
    while not queue.isEmpty(q):
        s = queue.dequeue(q)
        for adj in G.adjLists[s]:
            if p[adj] == None:       
                p[adj] = s
                if adj == dst:
                    return True
                q = queue.enqueue(adj, q)
            
    return False

def pathBFS(G, src, dst):
    p = [None] * G.order
    L = []
    if __pathBFS(G, src, dst, p):
        while dst != -1:
            L.insert(0, dst)
            dst = p[dst]
    return L
    
# search for a path with a dfs
# parent vector can also be used
# here, a list (used as a stack) is built when going up
    
def __pathDFS(G, s, dst, M, path):
    M[s] = True
    for adj in G.adjLists[s]:
        if not M[adj]:
            if adj == dst or __pathDFS(G, adj, dst, M, path):
                path.insert(0, adj)
                return True
    return False

def pathDFS(G, src, dst):
    M = [False] * G.order
    path = []
    if __pathDFS(G, src, dst, M, path):
        path.insert(0, src)
    return path


def testPaths(G):
    maxDiff = 0
    for i in range(G.order):
        for j in range(G.order):
            bfs = len(pathBFS(G, i, j))
            dfs = len(pathDFS(G, i, j))
            l = dfs-bfs
            if l > maxDiff:
                (src, dst) = (i, j)
                maxDiff = l
    return (src, dst)