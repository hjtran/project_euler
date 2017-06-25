from time import time
start = time()

# Problem Code
from collections import namedtuple
from heapq import heappop, heappush
node_heap = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = -1      # placeholder for a removed task
#counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    #count = next(counter)
    entry = [priority, task]
    entry_finder[task] = entry
    heappush(node_heap, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while node_heap:
        priority, task = heappop(node_heap)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')


Edge = namedtuple('Edge', ['length','n1','n2'])

class Network:

    def __init__(self,num_nodes):

        self._net = [ [0 for _ in range(num_nodes)] for __ in range(num_nodes)]

    def get_children(self,node):

        return [ idx for idx in range(len(self._net)) if self._net[node][idx] != 0 ]

    def get_edge(self,node1,node2):

        return self._net[node1][node2]

    def set_edge(self,node1,node2,edge_length):

        self._net[node1][node2] = edge_length
        #self._net[node2][node1] = edge_length

    def remove_edge(self,node1,node2):

        self.set_edge(node1,node2,0)

    def export_edges(self):

        edges = []
        for n1 in range(len(self._net)):
            for n2 in range(n1,len(self._net)):
                if self._net[n1][n2] != 0:
                    edges.append(Edge(self._net[n1][n2],n1,n2))
        return edges


n = 80
net = Network(n**2+2)
mat = [ [ 0 for _ in range(n) ] for __ in range(n) ]
with open('inputs/p082.txt','r') as infile:
    for idx,line in enumerate(infile):
        mat[idx] = list(map(int,line.strip().split(',')))


for r in range(n):
    for c in range(n):
        if c == 0:
            net.set_edge(0,r*n+1,mat[r][c])
        else:
            net.set_edge(r*n+c,r*n+c+1,mat[r][c])
            if c == n-1:
                net.set_edge(r*n+c+1,n**2+1,0.00001)
        if r != 0:
            net.set_edge( (r-1)*n+c+1, r*n+c+1,mat[r][c])
        if r != n-1:
            net.set_edge( (r+1)*n+c+1, r*n+c+1,mat[r][c])



#
prev = [ None for _ in range(n**2+2) ]
dist = [ float('Inf') for _ in range(n**2+2) ]
dist[0] = 0
add_task(0,0)
for i in range(1,n**2+2):
    add_task(i,float('Inf'))

traversed = set()
while node_heap:
    try:
        node = pop_task()
    except KeyError:
        break
    if node not in traversed:
        traversed.add(node)
        for c in net.get_children(node):
            if dist[c] > dist[node]+net.get_edge(node,c):
                dist[c] = dist[node]+net.get_edge(node,c)
                prev[c] = node
                add_task(c,dist[c])


print(dist[n**2+1])


print('Time Elapsed: %.2fs' % (time()-start,))        
