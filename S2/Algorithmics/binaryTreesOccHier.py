# -*- coding: utf-8 -*-
"""
November 2016
Binary trees: occurrences and hierarchical numbering
@author: Nathalie
"""

from AlgoPy import binTree
from AlgoPy.binTree import BinTree
from AlgoPy import queue

#------------------------------------------------------------------------------
# 4.1                           Occurrence list display

def treeToOccList(B):
    '''
    Builds the list of node occurrences
    '''
    q = queue.Queue()
    q = queue.enqueue((B,""))
    L = []
    while not queue.isEmpty(q):
        (T, occ) = queue.dequeue(q)
        L.append(occ)
        if T.left != None:
            q = queue.enqueue((T.left, occ+'0'), q)
        if T.right != None:
            q = queue.enqueue((T.right, occ+'1'), q)
    return L      

def printOccList(B):
    '''
    Prints the occurrence list representation of B
    '''
    if B != None:
        L = treeToOccList(B)
        s = '{' + chr(949)  # 'Îµ'
        for i in range(1, len(L)):
            s += ", " + L[i]
        s += '}'
    print(s)            
         
#------------------------------------------------------------------------------
# 4.2                         Prefix code

# tree from 4.2 q 3
        
codeTree = BinTree(None,
                   BinTree('a',None,None),
                   BinTree(None,
                          BinTree(None,BinTree('c',None,None),BinTree('b',None,None)),
                          BinTree(None,
                                 BinTree(None,BinTree('f',None,None),BinTree('e',None,None)),
                                 BinTree('d',None,None))))

occ = "{Îµ, 0, 1, 10, 11, 100, 101, 110, 111, 1100, 1101}"

# without optimization: traversal is done entirely

def printCode(B, c, s=""):
    if B.left == None:
        if B.key == c:
            print(s)
    else:
        printCode(B.left, c, s+'0')
        printCode(B.right, c, s+'1')


def callPrintCode(B, c):
    if B != None:
        printCode(B, c)


# the traversal stops when c is found

def printCodeOpti(B, c, s=""):
    if B.left == None:
        if B.key == c:
            print(s)
            return True
        else:
            return False
    else:
        if printCodeOpti(B.left, c, s+'0'):
            return True
        else:
            return printCodeOpti(B.right, c, s+'1')

def callPrintCodeOpti(B, c):
    if B == None or not printCodeOpti(B, c):
        print("No code found")


# another version: that builds the code going up
        
def findCode(B, c):
    if B.left == None:
        if B.key == c:
            return ""
        else:
            return None
    else:
        r = findCode(B.left, c)
        if r != None:
            return '0' + r
        else:
            r = findCode(B.right, c)
            if r != None:
                return '1' + r
            else:
                return None

def printCode2(B, c):
    code = None
    if B != None:
        code = findCode(B, c)
    if code != None:
        print(code)
    else:
        print("No code found")

             
#------------------------------------------------------------------------------
             
''' 
Trees as vector (list here) : 
using the hierarchical numbering
T[i] is the value at node number i (T[0] unused...)
'''

#------------------------------------------------------------------------------
#  6.1                       occurrence <-> hierarchical number

def fromOccToHier(occ):
    if occ == chr(949):
        return 1
    else:
        nb = 1
        for i in range(len(occ)):
            nb = 2*nb + int(occ[i])
        return nb

def fromHierToOcc(nb):
    if nb == 1:
        return chr(949)
    else:
        occ = ""
        while nb != 1:
            occ = str(nb % 2) + occ
            nb = nb // 2
        return occ
    
#------------------------------------------------------------------------------
#                             Examples

T_hier = [None]*30
for i in range(1, 9):
    T_hier[i] = i
(T_hier[11], T_hier[14], T_hier[29]) = (11, 14, 29)

B = BinTree(22, 
            BinTree(5, 
                    BinTree(3, BinTree(1, None, None), BinTree(4, None, None)), 
                    BinTree(12, None, BinTree(17, None, None))), 
            BinTree(29, BinTree(23, None, None), None))
# [None, 22, 5, 29, 3, 12, 23, None, 1, 4, None, 17, None, None, None, None, None, None, None, None, None, None, None, None]

#------------------------------------------------------------------------------
#  6.2                       Classics

def size_h(T, i = 1):
    if (i >= len(T)) or (T[i] == None):
        return 0
    else:
        return 1 + size_h(T, 2*i) + size_h(T, 2*i+1)
        
def depth_pref_h(T, i = 1):
    if (i < len(T)) and (T[i] != None):
        print(T[i], end=' ')
        depth_pref_h(T, 2*i)
        depth_pref_h(T, 2*i+1)

def breadth(T):
    if T[1] != None:
        l = len(T)
        q = queue.Queue()
        q = queue.enqueue(1)
        while not queue.isEmpty(q):
            no = queue.dequeue(q)
            print(T[no])
            no = 2 * no
            if no < l and T[no] != None:   # left child
                q = queue.enqueue(no, q)
            no = no + 1
            if no < l and T[no] != None:   # right child
                q = queue.enqueue(no, q)
                

#------------------------------------------------------------------------------           
#  6.3                     Tests

def testBinTrees(B, T, i = 1):
    if B == None or i >= len(T) or T[i] == None:
        return B == None and (i >= len(T) or T[i] == None)
    elif B.key != T[i]:
        return False
    else:
        return testBinTrees(B.left, T, 2*i) and testBinTrees(B.right, T, 2*i+1)

#------------------------------------------------------------------------------           
#  6.4                     object implementation <-> hierarchical (list)

# q1: object -> list

# version1: the size is given (maxi)

def __hierFromTree(B, T, maxi, i = 1):
    if i >= maxi:
        raise Exception("array is too short")
    if B == None:
        T[i] = None
    else:
        T[i] = B.key
        __hierFromTree(B.left, T, maxi, 2*i)
        __hierFromTree(B.right, T, maxi, 2*i+1)

def hierFromTree(B, maxi):
    T = [None]*maxi  
    __hierFromTree(B, T, maxi)
    return T


# version 1bis : maxi is the hierarchical number of the last empty child (can be done with the last node)

def last(T, i=1):
    if T != None:
        return max(i, last(T.left, 2*i), last(T.right, 2*i+1))
    else:
        return i

def hierFromTree1(B):
    maxi = last(B) + 1
    T = [None]*maxi
    __hierFromTree(B, T, maxi)
    return T
    
# version2: the list grows when needed (thanks to GolluM)

def hierSet(T, i, val):
    l = len(T)
    for k in range(i-l+1):
        T.append(None)
    T[i] = val

def __hierFromTree2(B, T, i = 1):
    if B == None:
        hierSet(T, i, None)
    else:
        hierSet(T, i, B.key)
        __hierFromTree2(B.left, T, 2*i)
        __hierFromTree2(B.right, T, 2*i+1)

def hierFromTree2(B):
    T = []
    __hierFromTree2(B, T)
    return T

# without calls on "empty" children: result is the shorter!


def __hierFromTree3(B, T, i = 1):
    hierSet(T, i, B.key)
    if B.left!= None:       
        __hierFromTree3(B.left, T, 2*i)
    if B.right != None:
        __hierFromTree3(B.right, T, 2*i+1)


def hierFromTree3(B):
    T = []
    if B == None:
        T[1] = None
    else:
        __hierFromTree3(B, T)
    return T
    
# version 2 vs version 3: testing i during traversal can be omitted with version 2 result...
    
# q2: list -> object

def treeFromHier(T, i = 1):
    if i >= len(T) or T[i] == None:
        return None
    else:
        B = BinTree(B.key, None, None)
        B.left = treeFromHier(T, 2*i)
        B.right = treeFromHier(T, 2*i+1)
        return B

def treeFromHier2(T, i = 1):
    if i >= len(T) or T[i] == None:
        return None
    else:
        return BinTree(T[i], treeFromHier2(T, 2*i), treeFromHier2(T, 2*i+1))
        