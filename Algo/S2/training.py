class BinTree:
    def __init__(self, key, left, right):
        """
        Init Tree
        """
        self.key = key
        self.left = left
        self.right = right

from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()

def enqueue(e, q):
    q.elements.append(e)
    return q

def dequeue(q):
    return q.elements.popleft()

def isEmpty(q): # empty ?
    return len(q.elements) == 0



def size (T):
	if (T != None):
		return (1 + size(T.left) + size(T.right))
	return 0

def height (T):
	if (T != None):
		return (max((height(T.left)+1), (height(T.right)+1)))
	return -1
	
def LDCExterne (T, s=0, h=0):
	if (T != None):
		if (T.left == None and T.right == None):
			return s + h 
		s = LDCExterne(T.left, s, h+1)
		h-1
		s = LDCExterne(T.right, s, h+1)
	return s

def DFTPreorder (T):
	if (T != None):
		print(T.key)
		DFTPreorder(T.left)
		DFTPreorder(T.right)
	else:
		print('_')
		
def BST (T):
	q = Queue()
	q = enqueue(T, q)
	while (not isEmpty(q)):
		r = dequeue(q)
		if (r != None):
			print(r.key)
			q = enqueue(r.left, q)
			q = enqueue(r.right, q)

def width(B):
    if B == None:
        return 0
    else:
        q = Queue()
        q = enqueue(B, q)
        q = enqueue(None, q)  #change-level mark
        w = 0
        max_w = 0
        while not isEmpty(q):
            T = dequeue(q)
            if T == None:
                max_w = max(max_w, w)
                w = 0
                if not isEmpty(q):
                    q = enqueue(None, q)
            else:
                w = w + 1
                if T.left != None:
                    q = enqueue(T.left, q)
                if T.right != None:
                    q = enqueue(T.right, q)
        return max_w
		
def search (T, x):
	if (T != None):
		if (T.key == x):
			return T
		A = search(T.left, x)
		if (A != None):
			return A
		A = search(T.right,x)
		if (A != None):
			return A
	else:
		return None
		
def isDegenerated (T):
	if (T != None):
		if (T.left != None and T.right != None):
			return False
		return (isDegenerated(T.left) and isDegenerated(T.right))
	return True

def isPerfect (T):
	if (T != None):
		if (not(T.right != None and T.left != None) and T.right != T.left):
			print (T.key)
			return False
		return (isPerfect(T.left) and isPerfect(T.right))
	return (True)
	
def isComplete (T):
	q = Queue()
	q = enqueue(T, q)
	firstNone = False 
	while (not isEmpty(q)):
		r = dequeue(q)
		if (r != None):
			q = enqueue(r.left, q)
			q = enqueue(r.right, q)
		else:
			firstNone = True
			

M = BinTree('M',None,None)
B = BinTree('B', None, None)
C = BinTree('C', None, M)
A = BinTree('A', B, C)

D = BinTree('D', None, None)
X = BinTree('X', None, None)
E = BinTree('E', D, X)

T = BinTree('T', A, E)

print (isPerfect(T))
print(height(T))
print(size(T))


'''
print(size(T))
print(height(T))
print(LDCExterne(T))
DFTPreorder(T)
print(width(T))
print()
BST(T)
print(search (T, 'L'))
print(isDegenerated(B))
'''
