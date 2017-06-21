from collections import namedtuple

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
        self._net[node2][node1] = edge_length

    def remove_edge(self,node1,node2):

        self.remove_edge(node1,node2,0)

    def export_edges(self):

        edges = []
        for n1 in range(len(self._net)):
            for n2 in range(n1,len(self._net)):
                if self._net[n1][n2] != 0:
                    edges.append(Edge(self._net[n1][n2],n1,n2))
        return edges



net = Network(40)
with open('inputs/p107.txt','r') as infile:
    for n1,line in enumerate(infile):
        for n2,edge_length in enumerate(line.strip().split(',')):
            if edge_length != '-' and n2 >= n1:
                net.set_edge(n1,n2,int(edge_length))

edges = net.export_edges()
edges.sort()
edges = edges[::-1]

mst = Network(40)
cloud = list(range(40))
def reassign_cloud(cloud,node,new_cloud):
    cloud[node] = new_cloud
    for child in mst.get_children(node):
        if cloud[child] != new_cloud:
            reassign_cloud(cloud,child,new_cloud)
    
savings = 0
while len(edges) > 0:
    e_len,n1,n2 = edges.pop()
    if cloud[n1] != cloud[n2]:
        reassign_cloud(cloud,n1,cloud[n2])
        mst.set_edge(n1,n2,e_len)
    else:
        savings += e_len
print(savings)
