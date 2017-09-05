from AlgoPy import binTree




# 1.1 BST -> list

def __BSTtoList(B, L):
    if B != None:
        __BSTtoList(B.left, L)
        L.append(B.key)
        __BSTtoList(B.right, L)
 
def BSTtoList(B):
    L = []
    __BSTtoList(B, L)
    return L       

        
# 1.1 list -> BST

def dicho(L, left, right):
    # L[left, right[ -> BST

    if left >= right:
        return None
    else:
        mid = (left + right) // 2   # left + (right-left) // 2
        B = binTree.BinTree(L[mid], dicho(L, left, mid), dicho(L, mid + 1, right))
        return B

def sortedList2BST(L):
    return dicho(L, 0, len(L))


Lsorted = [-15, -2, 0, 5, 8, 25, 32, 42, 51, 66]

#----------------------------------------------------------------------------
# 1.2 test

infty = float('inf')

def testBST(B, inf, sup):
    if B == None:
        return True
    else:
        return (inf < B.key and B.key <= sup) \
                and testBST(B.left, inf, B.key) \
                and testBST(B.right, B.key, sup)
def isBST(B):
    return testBST(B, -infty, infty)
    
#----------------------------------------------------------------------------
# 2.1 searches

# q1: minimum and maximum (tree is not empty)

def minBST(B):
    while B.left != None:
        B = B.left
    return B.key

def minBST_rec(B):
    if B.left == None:
        return B.key
    else:
        return minBST_rec(B.left)
    
def maxBST(B):
    while B.right != None:
        B = B.right
    return B.key
    
def maxBST_rec(B):
    if B.right == None:
        return B.key
    else:
        return maxBST_rec(B.right)

# q2: search for x in B
    
def searchBST(x, B):
    if B == None or B.key == x:
        return B
    else:
        if x < B.key:
            return searchBST(x, B.left)
        else:
            return searchBST(x, B.right)

def searchBST_iter(x, B):
    while B != None and B.key != x:
        if x < B.key:
            B = B.left
        else:
            B = B.right
    return B
            
#----------------------------------------------------------------------------
# 2.2 insert at leaf

def addBST(x, B):
    if B == None:
        return binTree.BinTree(x, None, None)
    else:
        if x <= B.key:
            B.left = addBST(x, B.left)
        else:
            B.right = addBST(x, B.right)
        return B


def list2BST(L):
    T = None
    for e in L:
        T = addBST(e, T)
    return T

L = [13, 20, 5, 1, 15, 10, 18, 25, 4, 21, 27, 7, 12]
B_tuto = list2BST(L)

def addBST_iter(x, B):
    T = B
    while T != None:
        dad = T
        if x <= T.key:
            T = T.left
        else:
            T = T.right
    new = binTree.BinTree(x, None, None)
    if B == None:
        B = new
    else:
        if x <= dad.key:
            dad.left = new
        else:
            dad.right = new
    return B

def list2BST_iter(L):
    T = None
    for e in L:
        T = addBST_iter(e, T)
    return T
    
#----------------------------------------------------------------------------
# 2.3 delete


def delBST_(x, B):
    if B == None:
        return None
    else:
        if x == B.key:
            if B.left != None and B.right != None:
                B.key = maxBST(B.left)
                B.left = delBST_(B.key, B.left)     # not optimized
            else:
                if B.left == None:
                    B = B.right
                else:
                    B = B.left
        else:
            if x < B.key:
                B.left = delBST_(x, B.left)
            else:
                B.right = delBST_(x, B.right)
        return B
        
# optimization: using delMax instead of maxBST
        
def delMax(B):        
    if B.right == None:
        return (B.key, B.left)
    else:
        (x, B.right) = delMax(B.right)
        return (x, B)
        
def delBST(x, B):
    if B == None:
        return None
    else:
        if x == B.key:
            if B.left != None and B.right != None:
                (B.key, B.left) = delMax(B.left)
            else:
                if B.left == None:
                    B = B.right
                else:
                    B = B.left
        else:
            if x < B.key:
                B.left = delBST(x, B.left)
            else:
                B.right = delBST(x, B.right)
        return B
        
#----------------------------------------------------------------------------
# 2.4 insert as new root

def cut(B, x):
    if B == None:
        return (None, None)
    else:
        if B.key <= x:
            G = B
            (G.right, D) = cut(B.right, x)
        else:
            D = B
            (G, D.left) = cut(B.left, x)
    return (G, D)

def addRoot(x, B):
    R = binTree.BinTree(x, None, None)
    (R.left, R.right) = cut(B, x)
    return R
    
    
def list2BST_root(L):
    T = None
    for e in L:
        T = addRoot(e, T)
    return T







        