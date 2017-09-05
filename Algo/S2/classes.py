

class BinTree:
    def __init__(self, key, left, right):
        """
        Init Tree
        """
        self.key = key
        self.left = left
        self.right = right


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



class Stack:
    def __init__(self):
        self.elements = deque()

def push(e, s):
    s.elements.append(e)
    return s

def top(s):
    return s.elements[len(s.elements)-1]
    
def pop(s):
    return s.elements.pop()

def isEmpty(s): # empty ?
    return len(s.elements) == 0



class AVL:
    def __init__(self, key, left, right, bal):
        self.key = key
        self.left = left
        self.right = right
        self.bal = bal