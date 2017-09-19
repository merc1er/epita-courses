# -*- coding: utf-8 -*-
"""
AVL tutorial
April 2017
@author: Nathalie
"""

from AlgoPy import avl

def printAVL(B, s=""):
    '''
    from Gollum's display
    '''
    if B != None:
        print(s, '- ', B.key, ' (', B.bal, ')', sep='')
        printAVL(B.left, s + "  |")
        printAVL(B.right, s + "   ")

#------------------------------------------------------------------------------
# height-balanced test

def __isBalanced(B):
    '''
    returns (height, boolean = balanced?)
    '''
    
    if B == None:
        return (-1, True)
    else:
        (hl, test) = __isBalanced(B.left) 
        if not test:
            return (0, False)
        else:
            (hr, test) = __isBalanced(B.right)
            return (1 + max(hl, hr), test and abs(hl-hr) < 2)
                
                
def isBalanced(B):
    (h, result) = __isBalanced(B)
    return result
    
#------------------------------------------------------------------------------    
# rotations: works only in "usefull" cases

def lr(A):
    aux = A.right
    A.right = aux.left
    aux.left = A
    A = aux
    
    A.left.bal = -1 - A.bal
    A.bal = 1 + A.bal
    return A
    
    
def rr(A):
    aux = A.left
    A.left = aux.right
    aux.right = A
    A = aux
    
    A.right.bal = 1 - A.bal
    A.bal = -1 + A.bal
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

    if A.bal == -1:
        (A.left.bal, A.right.bal) = (1, 0)
    elif A.bal == 1:
        (A.left.bal, A.right.bal) = (0, -1)
    else:
        (A.left.bal, A.right.bal) = (0, 0)
    A.bal = 0
    
    return A
    
def rlr(A):
    
    aux = A.right.left
    A.right.left = aux.right
    aux.right = A.right
    
    A.right = aux.left
    aux.left = A
    A = aux
    
    if A.bal == -1:
        (A.left.bal, A.right.bal) = (1, 0)
    elif A.bal == 1:
        (A.left.bal, A.right.bal) = (0, -1)
    else:
        (A.left.bal, A.right.bal) = (0, 0)
    A.bal = 0
    
    return A

#------------------------------------------------------------------------------
# insertion

def __insertAVL(x, A):
    if A == None:
        return (avl.AVL(x, None, None, 0), True)
    elif x == A.key:
        return (A, False)
    elif x < A.key:
        (A.left, dh) = __insertAVL(x, A.left)
        if not dh:
            return (A, False)
        else:
            A.bal += 1
            if A.bal == 2:
                if A.left.bal == 1:
                    A = rr(A)
                else:
                    A = lrr(A)
            return (A, A.bal == 1)
    else:   # x > A.key
        (A.right, dh) = __insertAVL(x, A.right)
        if not dh:
            return (A, False)
        else:
            A.bal -= 1
            if A.bal == -2:
                if A.right.bal == -1:
                    A = lr(A)
                else:
                    A = rlr(A)
            return (A, A.bal == -1)

def insertAVL(x, A):
    (A, dh) = __insertAVL(x, A)
    return A
    
def buildAVL(L):
    A = None
    for e in L:
        A = insertAVL(e, A)
    return A

L1 = [13, 20, 5, 1, 15, 10, 18, 25, 4, 21, 27, 7, 12]
L2 = [21, 7, 33, 5, 17, 26, 47, 1, 9, 20, 31, 42, 53, 4, 15]
L3 = [-15, -2, 0, 5, 8, 25, 32, 42, 51, 66]


#------------------------------------------------------------------------------
# deletion

# non optimized

def maxBST(B):
    while B.right != None:
        B = B.right
    return B.key
    
def __deleteAVL(x, A):
    if A == None:
        return (None, False)
    elif x == A.key:
        if A.left != None and A.right != None:
            A.key = maxBST(A.left)
            x = A.key
        else:
            if A.left == None:
                return(A.right, True)
            else:
                return(A.left, True)
    if x <= A.key:          # oui j'utilise le pouvoir dÃ©branchant du return !
        (A.left, dh) = __deleteAVL(x, A.left)
        if not dh:
            return (A, False)
        else:
            A.bal -= 1
            if A.bal == -2:
                if A.right.bal == 1:
                    A = rlr(A)
                else:
                    A = lr(A)
            return (A, A.bal == 0)
    else:   # x > A.key
        (A.right, dh) = __deleteAVL(x, A.right)
        if not dh:
            return (A, False)
        else:
            A.bal += 1
            if A.bal == 2:
                if A.left.bal == -1:
                    A = lrr(A)
                else:
                    A = rr(A)
            return (A, A.bal == 0)

def deleteAVL(x, A):
    (A, dh) = __deleteAVL(x, A)
    return A