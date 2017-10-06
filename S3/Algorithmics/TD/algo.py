import tree
import treeasbin

import queue
from queue import Queue

class Tree :
    def __init__(self, key , children = []):
        self.key = key
        self.children = children

    @property
    def nbchildren(self):
        return len(self.children)

    @property
    def size(self):
        return reduce(lambda accu , elt : accu + elt.size, self.children, 1)



#######################################
#                                     #
#             1 Measures              #
#                                     #
#######################################

# Exercise 1.1 : Size
def size(t):
    s = 1
    for child in t.children:
        s += size(child)
    return s

def size_bin(t): # iterative version
    s = 1
    child = t.child
    while child:
        s+= size_bin(child)
        child = child.sibling
    return s


#Exercise 1.2 : Height
def height (t):
    maxi = -1
    for child in t.children:
        maxi = max(maxi ,height(child))
    return maxi + 1

def height_bin(t): # iterative version
    h = -1
    child = t.child
    while child:
        h = max(h , height_bin(child))
        child =  child.sibling
    return h + 1

def height_bin2(t): #recursive version
    if not t :
        return -1
    return max(1+ height_bin2(t.child), height_bin2((t.sibling)))




#Exercise 1.3 : External path lenght

def external_path_lenght(t , d = 0):
    if not t.children :
        return d
    r = 0
    for child in t.children :
        r += external_path_lenght(child , d + 1)
    return r

def epl_bin(t, d=0):
    if not t.child :
        return d
    r = 0
    child = t.child
    while child :
        r += epl_bin(child, d+1)
        child = child.sibling
    return r

def epl_bin2(t, d=0):
    r = 0
    if not t.child:
        r = d
    else :
        r = epl_bin2(t.child, d+1)
    if t.sibling :
        r += epl_bin2(t.sibling, d)
    return r


###################################
#                                 #
#          2 TRAVERSALS           #
#                                 #
###################################

#Exercise 2.1 : Depth first traversal

# 2. Prefix order : 15 , 3 , -6 , 10 , 8 , 11 , 0 , 4 , 2 , 5 , 9
#    Suffix order : -6 , 10 , 3 , 0 , 4 , 11 , 2 , 5 , 8 , 9 , 15

#3. Goal of these functions : print the keys of the tree with a pip between the siblings:

def dfs (t):
    #preorder#
    print (t.key, end= ' ')
    if not t.children:
        #leaf case#
        return
    dfs(t.children[0])
    for child in t.child[1:]:
        print('|', end= ' ')
        #inorder#
        dfs(child)
    #postorder##
        print(t.key, end = ' ')

def dfs_bin (t):
    #preorder#
    print(t.key, end= " ")
    if t.child:
        dfs_bin(t.child)
        print(t.key, end = ' ')
    if t.sibling:
        print('|', end= ' ')
        dfs_bin(t.sibling)



#Exercise 2.2 : Breath first traversal

# 2. you push a level marker each time you meet one.

def width(t):
    q = Queue()
    maxw = 0
    count = 0
    q.enqueue(t)
    q.enqueue(None)
    while(not(q.emptyqueue())):
       node = q.dequeue()
       if  node == None :
           maxw = max(maxw, count)
           count = 0
       else:
          count += 1
          for child in node.children :
            q.enqueue(child)
    return maxw

def width_bin(t):
    w, wcur = 0,0
    q = Queue()
    q.enqueue(t)
    q.enqueue(None)
    while not q.emptyqueue():
        cur = q.dequeue()
        if not cur:
            w= max(w,wcur)
            wcur = 0
            if not q.isempty():
                q.enqueue(None)
        else:
            wcur += 1
            child = cur.child
            while child:
                q.enqueue(child)
                child = child.sibling
    return w


##################################
#                                #
#       3 APPLICATIONS           #
#                                #
##################################

#Exercise 3.1 : Equality

def same (T, B):
    if T.key == B.key:
        bc = B.child
        for tc in T.children:
            if not bc or not same (tc,bc) :
                return False
            bc = bc.sibling
        return bc == None
    return False

#Exercise 3.2 : Average Arity
def _average_arity(t):
    nc , ni = t.nbchildren, (t.nbchildren > 0)
    for child in t.children :
        c,i = _average_arity(child)
        nc, ni = nc + c, ni + i
    return nc , ni

def avg_arity(t):
    children, internal = _average_arity(t)
    return children / internal if internal else 0

def _avg_arity_bin(t):
    nc, ni = 0, (t.child != None)
    child = t.child
    while child :
        c,i = _avg_arity_bin(child)
        nc , ni = 1 + nc + c , ni + i
        child = child.sibling
    return nc, ni

def _double_rec_avg_arity_bin (t):
    if not t:
        return 0,0
    a, b = _double_rec_avg_arity_bin(t.child)
    c, d = _double_rec_avg_arity_bin(t.sibling)
    return a + c + 1, b + d + (t.child != None)

def double_rec_avg_arity_bin(t):
    size, internal = _double_rec_avg_arity_bin(t)
    return (size - 1) / internal if internal else 0

# Exercise 3.3 : Serialization

#1. [2 , 2  ,10 , 6, 2, 10, 7, 8 , 10, 2, -1, 6]


#2.
def _serialization(t,parents):
        for child in t.children :
            parents[child.key]= t.key
            _serialization(child, parents)



def serialization(t, size):
    parents =[-1] * size
    _serialization(t, parents)
    return parents

def _serialization_bin(t,parents):
    if t.child:
        parents[t.child.key]= t.key
        _serialization_bin(t.child,parents)
    if t.sibling:
        parents[t.sibling.key] = parents[t.key]
        _serialization_bin()


def serialisation_bin(t, size):
    parents = [-1] * size
    _serialization_bin(t , parents)
    return parents


#Exercise 3.4 : Tuples <=> left child- right sibling

#1.
def sibling_to_tuples(b):
  t = tree.Tree(b.key)
  child = b.child
  while child :
      t.children.append(sibling_to_tuples(child))
      child = child.sibling
  return t











































