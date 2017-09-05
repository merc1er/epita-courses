# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 20:25:48 2017

@author: Nathalie
"""

from AlgoPy import binTree

"""
ex 3.1
"""

# q1

def search(x, B):
    if B == None:
        return None
    else:
        if x == B.key:
            return B
        else:
            res = search(x, B.left)
            if res == None:
                res = search(x, B.right)
            return res

# q2
# the path is th occurrence of the node

def __searchOcc(x, B, occ=""):
    if B == None:
        return ""
    else:
        if x == B.key:
            return occ
        else:
            res = __searchOcc(x, B.left, occ + '0')
            if res == "":
                res = __searchOcc(x, B.right, occ + '1')
            return res

def searchOcc(x, B):
    if B != None and x == B.key:
        return chr(949)  # 'Îµ'
    else:
        return __searchOcc(x, B)
            
# the path is a stack of 'l' for left and 'r' for right

from AlgoPy import stack

def __path(x, B, path):
    if B == None:
        return None
    else:
        if x == B.key:
            return B
        else:
            res = __path(x, B.left, path)
            if res != None:
                stack.push('l', path)
            else:
                res = __path(x, B.right, path)
                if res != None:
                    stack.push('r', path) 
        return res

def searchPath(x, B):
    path = stack.Stack()
    return (__path(x, B, path), path)
    
def followPath(B, path):
    while not stack.isEmpty(path):
        side = stack.pop(path)
        if side == 'l':
            B = B.left
        else:
            B = B.right
    print(B.key)
    

#------------------------------------------------------------------------------
#  ex 3.2   new implementation: with a link to parent in each nodes

class BinTreeParent:
    def __init__(self, key, parent, left, right):
        """
        Init Tree
        """
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

# first version: parent is pass as parameter

def __copy(B, p):
    if B == None:
        return None
    else:
        C = BinTreeParent(B.key, p, None, None)
        C.left = __copy(B.left, C)
        C.right = __copy(B.right, C)
        return C
        
def copyWithParent(B):
    return __copy(B, None)


# second version: parent is set going up

def __copy2(B):
    '''
    B is not None
    '''
    C = BinTreeParent(B.key, None, None, None)
    if B.left != None:
        C.left = __copy2(B.left)
        C.left.parent = C
    if B.right != None:
        C.right = __copy2(B.right)
        C.right.parent = C
    return C

def copyWithParent2(B):
    if B == None:
        return None
    else:
        return __copy2(B)
        