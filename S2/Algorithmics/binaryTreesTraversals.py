# -*- coding: utf-8 -*-
"""
Binary Trees
February 2016
@author: Nathalie
"""

from AlgoPy import binTree
from AlgoPy.binTree import BinTree

# Some Binary Trees
B_ex = BinTree(1, 
          BinTree(2, 
                BinTree(4, BinTree(8,None,None), None), 
                BinTree(5,None,BinTree(11,None,None))),
          BinTree(3, 
                BinTree(6,None,None), 
                BinTree(7, BinTree(14,None,BinTree(29,None,None)),None)))
         
B_tuto = BinTree('V', 
            BinTree('D', 
               BinTree('I', 
                  BinTree('Q', None,BinTree('U', None,None)),
                  None),
               BinTree('S', 
                  BinTree('E', None,None),
                  BinTree('T', None,None))),
            BinTree('I', 
               BinTree('E', 
                  None,
                  BinTree('R', None,None)),
              BinTree('A', 
                  BinTree('T', None,None),
                  BinTree('S', None,None))))         


def printTree(B, s=""):
    '''
    display from GolluM/Nath
    '''
    if B == None:
        print(s, '- ')
    elif B.left == None and B.right == None:
        print(s, '- ', B.key)
    else:
        print(s, '- ', B.key)
        printTree(B.left, s + "  |")
        printTree(B.right, s + "   ")
        
#------------------------------------------------------------------------------
"""    
1 - Measures
"""
            
def size(B):
    if B == None:
        return 0
    else:
        return 1 + size(B.left) + size(B.right)

def height(B):
    if B == None:
        return -1
    else:
        return 1 + max(height(B.left), height(B.right))


def epl(B, h = 0):
    '''
    Binary Tree External Path Length (LCE)
    Returns: (EPL, Leaf count)
    '''
    if B == None:
        return (0, 0)
    elif B.left == None and B.right == None:
        return (h, 1)
    else:
        (a, n1) = epl(B.left, h+1)
        (b, n2) = epl(B.right, h+1)
        return (a + b, n1 + n2)

def ead(B):
    '''
    Binary Tree External Average Depth (PME)
    '''
    if B == None:
        raise Exception("Empty tree")
    else:
        (p, n) = epl(B)
        return p / n


#------------------------------------------------------------------------------
"""    
2.1 - Depth-First Traversals (DFS)
"""

def dfsPrefix(B):
    '''
    Depth-first traversal
    Prints keys in preorder
    '''
    if B != None:
        print(B.key, end=' ')
        dfsPrefix(B.left)
        dfsPrefix(B.right)
        
def dfsInfix(B):
    '''
    Depth-first traversal
    Prints keys in inorder
    '''
    if B != None:
        dfsInfix(B.left)
        print(B.key, end=' ')
        dfsInfix(B.right)

def dfsSuffix(B):
    '''
    Depth-first traversal
    Prints keys in postorder
    '''
    if B != None:
        dfsInfix(B.left)
        dfsInfix(B.right)
        print(B.key, end=' ')


def tree2Abstract(B):
    '''
    Prints the "abstract" form of the tree
    '''
    if B == None:
        print('_', end='')
    else:
        print('<', end='')
        tree2Abstract(B.left)
        print(B.key, end='')
        tree2Abstract(B.right)
        print('>', end='')

def tree2AbstractStr(B):
    '''
    Returns the "abstract" form of the tree as a string
    '''
    if B == None:
        return '_'
    else:
        s = '<' + str(B.key) + ','
        s = s + tree2AbstractStr(B.left) + ','
        s = s + tree2AbstractStr(B.right)
        s = s + '>'
        return s

def tree2AbstractStr2(B):
    if B == None:
        return '_'
    else:
        return '<' + str(B.key) + ',' \
        + tree2AbstractStr2(B.left) + ',' \
        + tree2AbstractStr2(B.right) + '>'

"""    
2.2 - Breadth-First Traversals (bfs)
"""

from AlgoPy import queue

def bfs(B):
    '''
    Prints keys in breadth-first traversal order
    '''
    if B != None:
        q = queue.Queue()
        q = queue.enqueue(B, q)
        while not queue.isEmpty(q):
            T = queue.dequeue(q)
            print(T.key, end=' ')
            if T.left != None:
                q = queue.enqueue(T.left, q)
            if T.right != None:
                q = queue.enqueue(T.right, q)

# computes the width with a "change-level mark"
def width(B):
    if B == None:
        return 0
    else:
        q = queue.Queue()
        q = queue.enqueue(B, q)
        q = queue.enqueue(None, q)  #change-level mark
        w = 0
        max_w = 0
        while not queue.isEmpty(q):
            T = queue.dequeue(q)
            if T == None:
                max_w = max(max_w, w)
                w = 0
                if not queue.isEmpty(q):
                    q = queue.enqueue(None, q)
            else:
                w = w + 1
                if T.left != None:
                    q = queue.enqueue(T.left, q)
                if T.right != None:
                    q = queue.enqueue(T.right, q)
        return max_w

# version with two queues

def width2(B):
    if B == None:
        return 0
    else:
        q = queue.Queue()
        q = queue.enqueue(B, q)
        q2 = queue.Queue()
        w = 0
        max_w = 0
        while not queue.isEmpty(q):
            T = queue.dequeue(q)
            w = w + 1
            if T.left != None:
                q2 = queue.enqueue(T.left, q2)
            if T.right != None:
                q2 = queue.enqueue(T.right, q2)
            if queue.isEmpty(q):    # level change
                max_w = max(max_w, w)
                w = 0
                q = q2
                q2 = queue.Queue()
        return max_w

#----------------------------------------------------------------------

# tests
def testBinTree(B):
    printTree(B)
    print("Depth-First Traversals:")
    print("----------------------")
    print("- Preorder:", end = ' ')
    dfsPrefix(B)
    print()
    print("- Inorder:", end = ' ')
    dfsInfix(B)
    print()
    print("- Postorder:", end = ' ')
    dfsSuffix(B)
    print()
    print(tree2AbstractStr(B))
    print()
    print("Breadth-First Traversal:")
    print("-----------------------")
    bfs(B)
    print('\n')
    print("size =", size(B), "- height =", height(B), \
        "- external average depth =", ead(B), "- width =", width(B), width2(B))