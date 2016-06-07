class EdgeNotFoundException(Exception):
    pass

class NodeNotFoundException(Exception):
    pass


class Graph:

    class Node:
        
        def __init__(self,label):
            self._label = label
        
        def getLabel(self):

            return _label

    class Edge:

        def __init__(self,n1,n2,wt=1):
            self._n1 = n1
            self._n2 = n2
            self._wt = wt

        def getWeight(self):

            return self._wt

        def getStartNode(self):
            
            return self._n1

        def getEndNode(self):

            return self._n2


    def __init__(self):
        nodes = []
        edges = {}

    def addNode(self,label):
        newNode = Node(label)
        nodes.append(newNode)
        edges[newNode] = {}
        return newNode

    def removeNode(self,node):
        if node not in nodes:
            raise NodeNotFoundException()
        
        for e in edges[node]:
            removeEdge(e)
        del edges[node]
        nodes.remove(node)

    def addEdge(self,n1,n2,wt=1):
        
        if n1 is not in nodes or n2 is not in nodes:
            raise NodeNotFoundException()
        newEdge = Edge(n1,n2,wt)
        edges[n1][n2] = newEdge
        edges[n2][n1] = newEdge

    def removeEdge(self,edge):
        del edges[edge.getStartNode][edge.getEndNode]
        del edges[edge.getEndNode][edge.getStartNode]

    def __len__(self):
        return len(nodes)

    def numNodes(self):
        return __len__
    
    def numEdges(self):
        pass

    def inEdges(self,n):
        ret = []
        for node in nodes:
            if node is not n:
                if n in edges[node]:
                    ret.extend(edges[node][n].values())
        return ret

    def outEdges(self,n):
        return edges[n].values()



