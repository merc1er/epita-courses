from AlgoPy import binTree

# to run tests
#from binaryTreesSerialization import *

#-------------------------------------------------------------

def degenerate0(T):
    if T == None :
        return True
    elif T.left != None  and T.right != None :
        return False 
    else :
        return degenerate0(T.left) and degenerate0(T.right)
        
        
def __degenerate(B):
    '''
    B not empty
    '''
    if B.left == None:
        if B.right == None:
            return True
        else:
            return __degenerate(B.right)
    else:
        if B.right == None:
            return __degenerate(B.left)
        else:
            return False
            
def degenerate(B):
    return B == None or __degenerate(B)


def __degenerate2(B):
    '''
    B not empty
    '''
    leftEmpty = (B.left == None)
    if B.right == None:
        return leftEmpty or __degenerate(B.left)
    else:
        return leftEmpty and __degenerate(B.right)
        
def degenerate2(B):
    return B == None or __degenerate(B)

    
# degenerate(buildTreeFromSerial2(LDegen))    
# degenerate2(buildTreeFromSerial2(LDegen)) 
    
#------------------------------------------------------------------------------        

def __perfect(B, h):
    '''
    B != None
    '''
    if B.left == None:
        if B.right == None:
            return h == 0
        else:
            return False
    else:
        if B.right == None:
            return False
        else:
            return __perfect(B.left, h-1) and __perfect(B.right, h-1)
        
def perfect(B):
    if B == None:
        return True
    else:
        h = 0
        T = B
        while T.left != None:
            h += 1
            T = T.left
        return __perfect(B, h)



def __perfect2(B, h):
    if B== None:
        return h == -1
    else:
        return __perfect2(B.left, h-1) and __perfect2(B.right, h-1)
    
def perfect2(B):
    h = -1
    T = B
    while T != None:
        T = T.left
        h += 1
    return __perfect2(B, h)    


def __perfect3(B, h):
    if B.left != None and B.right != None:
        return __perfect3(B.left, h-1) and __perfect3(B.right, h-1)
    else:
        return (B.left == None and B.right == None) and (h == 0)
    
def perfect3(B):
    h = -1
    T = B
    while T != None:
        T = T.left
        h += 1
    return B == None or __perfect3(B, h)
    
# perfect(buildTreeFromSerial(LPerfect)) 
# perfect(buildTreeFromSerial(LAlmost))

from AlgoPy import queue

def perfectWidth(B):
    if B == None:
        return True
    else:
        q = queue.Queue()
        q = queue.enqueue(B, q)
        q = queue.enqueue(None, q)
        (w, next_w) = (0, 1)
        perfect = True
        while not queue.isEmpty(q) and perfect:
            T = queue.dequeue(q)
            if T == None:
                if w != next_w:
                    perfect = False
                if not queue.isEmpty(q):
                    next_w = w * 2
                    w = 0
                    q = queue.enqueue(None, q)
            else:
                w = w + 1
                if T.left != None:
                    q = queue.enqueue(T.left, q)
                if T.right != None:
                    q = queue.enqueue(T.right, q)
        return perfect

# perfectWidth(buildTreeFromSerial(LPerfect)) 
# perfectWidth(buildTreeFromSerial(LAlmost))

#------------------------------------------------------------------

def completeWidth(B):
    q = queue.Queue()
    q = queue.enqueue(B, q)
    empty_child = False
    while not queue.isEmpty(q) and not empty_child:
        T = queue.dequeue(q)
        if T.left == None:
            empty_child = True
        else:
            q = queue.enqueue(T.left, q)
            if T.right != None:
                q = queue.enqueue(T.right, q)
            else:
                empty_child = True
    complete = True
    while not queue.isEmpty(q) and complete:
        T = queue.dequeue(q)
        complete = (T.left == None and T.right == None)
    return complete
    
# completeWidth(buildTreeFromSerial(LAlmost))
# completeWidth(buildTreeFromSerial(LComplete))
# completeWidth(buildTreeFromSerial(LPerfect))