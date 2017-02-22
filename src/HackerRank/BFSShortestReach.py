
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.last = None
		self.next = next
	def set_data(self, data):
		self.data = data
	def get_data(self):
		return self.data
	def set_next(self, next):
		self.next = next
	def get_next(self):
		return self.next
	def setLast(self, last):
		self.last = last
	def getLast(self):
		return self.last	
	def has_next(self):
		return self.next != None


class Queue(object):
	def __init__(self, data=None):
		self.front = None
		self.rear = None
		self.size = 0

	def enQueue(self, data):
		self.lastNode = self.front
		self.front = Node(data, self.front)
		if self.lastNode:
			self.lastNode.setLast(self.front)
		if self.rear is None:
			self.rear = self.front
		self.size += 1

	def queueRear(self):
		if self.rear is None:
			print ("Sorry, the queue is empty!")
			raise IndexError
		return self.rear.get_data()

	def queueFront(self):
		if self.front is None:
			print ("Sorry, the queue is empty!")
			raise IndexError
		return self.front.get_data()

	def deQueue(self):
		if self.rear is None:
			print ("Sorry, the queue is empty!")
			raise IndexError
		result = self.rear.get_data()
		self.rear = self.rear.last
		self.size -= 1
		return result

	def size(self):
		return self.size
	
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = -1
        self.visited = False
        self.color = 'white'  	
        self.previous = None

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getConnections(self):
        return self.adjacent.keys()  

    def getVertexID(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance
	
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color	

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertDictionary.values())

    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]
        else:
            return None

    def addEdge(self, frm, to, cost=0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)

        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)
	# For directed graph do not add this
        self.vertDictionary[to].addNeighbor(self.vertDictionary[frm], cost)

    def getVertices(self):
        return self.vertDictionary.keys()

    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous
	
    def getEdges(self):
        edges = []
        for v in G:
            for w in v.getConnections():
                vid = v.getVertexID()
                wid = w.getVertexID()
                edges.append((vid, wid, v.getWeight(w)))
        return edges
 
def BFSTraversal(G, s):  
	start = G.getVertex(s)
	start.setDistance(0)
	start.setPrevious(None)
	vertQueue = Queue()
	vertQueue.enQueue(start)

	while (vertQueue.size > 0):
		currentVert = vertQueue.deQueue()
		for nbr in currentVert.getConnections():
			if (nbr.getColor() == 'white'):
				nbr.setColor('gray')
				nbr.setDistance(currentVert.getDistance() + 6)
				nbr.setPrevious(currentVert)
				vertQueue.enQueue(nbr)
			currentVert.setColor('black')
    
            
if __name__ == '__main__':
    
    q = int(input())
    for i in range(0,q):
        n,m = [int(i) for i in input().strip().split(' ')]
        G = Graph()
        for i in range(0,n):
            G.addVertex(i+1) 
        for i in range(0,m):
            fromV,toV = [int(i) for i in input().strip().split(' ')]
            G.addEdge(fromV, toV , 6)  
        
        s = int(input())
        BFSTraversal(G,s)
        
        for i in range(1,n+1):
            if i != s:
                print(G.vertDictionary[i].getDistance(), end = ' ')
        print()
