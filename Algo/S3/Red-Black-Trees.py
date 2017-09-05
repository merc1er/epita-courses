# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:27:12 2016

@author: Nathalie
"""

from AlgoPy import bTree
from AlgoPy.bTree import BTree
bTree.BTree.degree = 2
 
from AlgoPy import redBlackTree
from AlgoPy.redBlackTree import RedBlackTree


import BtreeToDot
import redBlackTreeToDot
#import IPython

RBT_ex = RedBlackTree(13, False,
                      RedBlackTree(8, True, 
                                   RedBlackTree(1, False, None, RedBlackTree(6, True)),
                                   RedBlackTree(11, False)),
                      RedBlackTree(17, True, 
                                   RedBlackTree(15, False), 
                                    RedBlackTree(25, False, RedBlackTree(22, True), RedBlackTree(27, True))
                                    )
                    )

# ex 1.4 q2, degree = 2
s1 = "(<13,32,44>(<3>)(<18,25>)(<35,40>)(<46,49,50>))"
B1 = bTree.fromList(s1, 2)


# second in tutorial, ex 1.4 q1 degree = 2
s2 = "(<22>(<15>(<8,12>)(<18,19,20>))(<27,41>(<24,25>)(<30,35,38>)(<45,48>)))"
B2 = bTree.fromList(s2, 2)

#----------------------------- Conversions ------------------------------------                    

def redBlackFrom24tree(T):
    if T == None:
        return None
    if T.children == []:
        children = [None]*(T.nbKeys+1)
    else:
        children = T.children
    B = RedBlackTree(T.keys[0], T.nbKeys > 1, 
                     redBlackFrom24tree(children[0]), 
                    redBlackFrom24tree(children[1]))
    if T.nbKeys > 1:
        B = RedBlackTree(T.keys[1], False, B, None)
        if T.nbKeys == 2:
            B.right = redBlackFrom24tree(children[2])
        else:
            B.right = RedBlackTree(T.keys[2], True, 
                                   redBlackFrom24tree(children[2]),
                                   redBlackFrom24tree(children[3]))
    return B
    

def redBlackTo24tree(B):
    if B == None:
        return None
    else:
        N = BTree()

        if B.left and B.left.red:
            N.keys.append(B.left.key)
            N.children.append(redBlackTo24tree(B.left.left))
            N.children.append(redBlackTo24tree(B.left.right))
        else:
            N.children.append(redBlackTo24tree(B.left))
        
        N.keys.append(B.key)
    
        if B.right and B.right.red:
            N.keys.append(B.right.key)
            N.children.append(redBlackTo24tree(B.right.left))
            N.children.append(redBlackTo24tree(B.right.right))
        else:
            N.children.append(redBlackTo24tree(B.right)) 
        
        if N.children[0] == None:
            N.children = []
        return N
        
#---------------------------- insertion ---------------------------------------

def splitRBT(B):
    '''
    B exists and has two children
    its root is black, its two children are red
    '''     
    B.red = True
    B.left.red = False
    B.right.red = False

# rotations

def lr(A):
    aux = A.right
    A.right = aux.left
    aux.left = A
    A = aux
    A.red = False
    A.left.red = True
    return A
    
    
def rr(A):
    aux = A.left
    A.left = aux.right
    aux.right = A
    A = aux
    A.red = False
    A.right.red = True
    return A


def lrr(A):
# left rotation on left child
    aux = A.left.right
    A.left.right = aux.left
    aux.left = A.left
# right rotation
    A.left = aux.right
    aux.right = A
    A = aux

    A.red = False
    A.right.red = True
    return A
    
def rlr(A):
    
    aux = A.right.left
    A.right.left = aux.right
    aux.right = A.right
    
    A.right = aux.left
    aux.left = A
    A = aux
    
    A.red = False
    A.left.red = True
    
    return A
    
# insertion

def _insertRBT(B, x):
    if B == None:
        return (RedBlackTree(x, True, None, None), 1)
    elif x == B.key:
        return (B, 0)
    else:
        if x < B.key:
            (B.left, red) = _insertRBT(B.left, x)
            if B.red:
                return (B, red+1)
            else:
                if abs(red) == 2:
                    if B.right and B.right.red:
                        splitRBT(B)
                        return(B, 1)
                    elif red > 0:   # red == 2
                        B = rr(B)
                    else:           # red == -2
                        B = lrr(B)
            return (B, 0)
        else:   # x > B.key
            (B.right, red) = _insertRBT(B.right, x)
            if B.red:
                return (B, 1-3*red)
            else:
                if abs(red) == 2:
                    if B.left and B.left.red:
                        splitRBT(B)
                        return(B, 1)
                    elif red < 0:   # red == -2
                        B = lr(B)
                    else:           # red == 2
                        B = rlr(B)
            return (B, 0)

def insertRBT(B, x):
    (B, _) = _insertRBT(B, x)
    B.red = False
    return B
    
def test():
    # ex from Red Black Trees tuto
    s = "(<20>(<15>(<3,8,10>)(<18>))(<25,40>(<22, 23>)(<38>)(<42,45>)))"
    T = bTree.fromList(s, 2)
    BtreeToDot.viewBTree(T)
    B = redBlackFrom24tree(T)
    redBlackTreeToDot.viewTree(B)
    for x in (17, 48, 5, 52, 16, 62):
        B = insertRBT(B, x)
        redBlackTreeToDot.viewTree(B)
        input()