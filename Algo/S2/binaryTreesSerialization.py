# -*- coding: utf-8 -*-
"""
Binary Tree Serialization
February 2017
@author: Nathalie
"""

from AlgoPy import binTree

# examples

L_tuto = ['V', 'D', 'I', 'Q', '#', 'U', '#', '#', '#', 'S', 'E', '#', '#',
          'T', '#', '#', 'I', 'E', '#', 'R', '#', '#', 'A', 'T', '#',
          '#', 'S', '#', '#']


Lperfect = [1,5,7,21, '#', '#', 33, '#', '#', 26, 17, '#', '#', 47, '#', '#',
     42, 20, 9, '#', '#', 31, '#', '#', 4, 53, '#', '#', 15, '#', '#']    

# not perfect (leaves not at same height)

LnotPerfect1 = [26, 5, 7, 21, '#', '#', 33, '#', '#', 17, '#', '#', 
      42, 20, 1, 47, '#', '#', 9, '#', '#', 31, '#', '#', 4, 53, '#', '#', 
      15, '#', '#']

#not perfect (a single internal node)

LnotPerfect2 = [1,5,7,'#', 33, '#', '#', 26, 17, '#', '#', 47, '#', '#',
     42, 20, 9, '#', '#', 31, '#', '#', 4, 53, '#', '#', 15, '#', '#']    


LDegen = [66, '#', 24, '#', 35, 35, 84, '#', 15, 33, '#', '#', '#','#', '#']

LFull = [11, 65, 95, 27, '#', '#', 58, '#', '#', 16, '#', '#', 67, '#', '#']

LPerfect = [75, 84, 93, 72, '#', '#', 83, '#', '#', 86, 56, '#', '#', 
 57, '#', '#', 65, 59, 44, '#', '#', 81, '#', '#', 22, 17, '#', '#', 26, '#', '#']
    
LAlmost = [75, 84, 93, 72, '#', '#', 83, '#', '#', 86, 56, '#', '#', 
 '#', 65, 59, 44, '#', '#', 81, '#', '#', 22, 17, '#', '#', 26, '#', '#']

LAlmost2 = [75, 84, 93, 72, '#', '#', 83, '#', '#', 86, '#', 
 '#', 65, 59, 44, '#', '#', 81, '#', '#', 22, 17, '#', '#', 26, '#', '#']
 
LComplete = [75, 84, 93, 72, '#', '#', 83, '#', '#', 86, 56, '#', '#', 
 '#', 65, 59, '#', '#', 22, '#', '#']
 

"""
3.4 - Serialization
"""

def serialize(B, L):
    if B == None:
        L.append('#')
    else:
        L.append(B.key)
        serialize(B.left, L)
        serialize(B.right, L)

def serializeBinTree(B):
    L = []
    serialize(B, L)
    return L


#---------------------------------------------------
# from serialized form to tree

# the function returns the index
    
def __buildTree(L, i=0):
    if i >= len(L) or L[i] == '#':
        return (None, i+1)
    else:
        B = binTree.BinTree(L[i], None, None)
        i = i + 1
        (B.left, i) = __buildTree(L, i)        
        (B.right, i) = __buildTree(L, i)
        return (B, i)

def buildTreeFromSerial(L):
    (B, i) = __buildTree(L)
    return B
    
# last version: reverses the list, then use L.pop() => WARNING: list is lost
    
def __buildTreeS(L):
    if L == []:
        return None
    else:
        e = L.pop()
        if e == '#':
            return None
        else:
            B = binTree.BinTree(e, None, None)
            B.left = __buildTreeS(L)    
            B.right = __buildTreeS(L)
            return B

def reverse(L):
    n = len(L)
    for i in range(n//2):
        (L[i], L[n-i-1]) = (L[n-i-1], L[i])
    return L

def buildTreeFromSerial2(L):
    return __buildTreeS(reverse(L))

