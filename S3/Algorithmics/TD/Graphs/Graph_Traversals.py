# -*- coding: utf-8 -*-
"""
Graphs: traversals - tutorial part 2
Nov 2016
@author: Nathalie
"""

#from AlgoPy import graph
#from AlgoPy import graphMat


#------------------------------------------------------------------------------
# Ex 2.1 q.4
"""
 Breadth First Search (Traversal): 
same algorithm whether the graph is directed or not
"""

from AlgoPy import queue

# with adjacency lists
def __bfs(G, s, p):
    q = queue.Queue()
    q = queue.enqueue(s, q)
    p[s] = -1    # M[s] = True
    while not queue.isEmpty(q):
        s = queue.dequeue(q)
        print(s, end = ' ')
        for adj in G.adjLists[s]:
            if p[adj] is None: # not M[adj]       
                p[adj] = s
                q = queue.enqueue(adj, q)
#                print(s, "->",  adj)
                
# with adjacency matrix
def __bfsMat(G, s, p):
    q = queue.Queue()
    q = queue.enqueue(s, q)
    p[s] = -1    # M[s] = True
    while not queue.isEmpty(q):
        s = queue.dequeue(q)
        print(s, end = ' ')
        for adj in range(G.order):
            if G.adj[s][adj]:   #adj is a successor
                if p[adj] is None: # not M[adj]       
                    p[adj] = s
                    q = queue.enqueue(adj, q)
#                   print(s, "->",  adj)

# call      
def bfs(G):
    p = [None] * G.order   # M = [False] * G.order
    for s in range(G.order):
        if p[s] is None:       # not M[s]
            __bfs(G, s, p)
    # p represents the spanning forest
    return p

#------------------------------------------------------------------------------
# ex 2.2 q2.4

"""
Depth first traversal (DFS)
"""

# simple DFS with adjacency lists
def __dfs(G, s, M):
    M[s] = True    # usually vertices are marked here
    print(s, end=' ')
    for adj in G.adjLists[s]:
        if not M[adj]: 
            __dfs(G, adj, M)
                
def dfs(G):
    M = [False] * G.order
    for s in range(G.order):
        if not M[s]:
            __dfs(G, s, M)
            
# q.3(c) graph depth-first traversal with back edge detection (with adjacency matric)
def __dfsForest(G, s, p):
    for adj in range(G.order):
        if G.adj[s][adj]:
            if p[adj] == None:  # tree edge
                p[adj] = s      # vertices has to be marked here
                print(s, "->", adj)
                __dfsForest(G, adj, p)
            else:
                if adj != p[s]:
                    print(s, '->', adj, "back edge")    #unless adj -> s is a back edge!
                
def dfsForest(G):
    p = [None] * G.order
    for s in range(G.order):
        if p[s] == None:
            p[s] = -1
            __dfsForest(G, s, p)
    return p


# q.4(c) digraph depth-first traversal -> prefix and suffix numbering with a single counter
# to detect edge types (with adjacency lists)

def __depthPrefSuff(G, s, pref, suff, cpt):
    cpt += 1
    pref[s] = cpt
    for adj in G.adjLists[s]:
        if pref[adj] == 0:
           print (s, "->",  adj)
           cpt = __depthPrefSuff(G, adj, pref, suff, cpt)
        else:
            if pref[s] < pref[adj]:
                print (s, "->",  adj, "forward")
            else:
                if suff[adj] == 0:
                    print (s, "->",  adj, "back")
                else:
                    print (s, "->",  adj, "cross")
    cpt += 1
    suff[s] = cpt
    return cpt

def depthPrefSuff(G):
    pref = [0] * G.order
    suff = [0] * G.order 
    cpt = 0
    for s in range(G.order):
        if pref[s] == 0:
            cpt = __depthPrefSuff(G, s, pref, suff, cpt)
    return(pref, suff)