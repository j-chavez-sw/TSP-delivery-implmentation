# Julian A. Chavez
#I.D. #: 000966293


#this class represents package locations
#each object created from this class is an address from the provided materials
#inspiration from Holczer Balazs Udemy course - https://www.udemy.com/course/algorithms-and-data-structures-in-python/
class Vertex:

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
        self.visited = False
        self.adjacencyList = []
        self.startPoint = False
        self.midPoint = False
        self.endPoint = False
            

    def __str__(self):
        string = self.id
        return string

    def addEdge(self, edge):
        if edge not in self.adjacencyList:
            self.adjacencyList.append(edge)
        else:
            print("edge already exists...")

    def getVectorDistance(self, otherVertex):

        for edge in self.adjacencyList:
            if edge.targetVertex.getID() == otherVertex.getID():
                return edge.getWeight()

        return None

    def getADJList(self):
        return self.adjacencyList

    def getID(self):
        return int(self.id)

    def printADJ(self):

        print("ADJ LIST: ",self.id, *self.adjacencyList, sep=", ")
        
    def isSwappable(self):
        if(self.startPoint):
            return False
        elif(self.midPoint):
            return False
        elif(self.endPoint):
            return False
        else:
            return True
        
    def setStart(self,bool):
        self.startPoint = bool
        
    def setMid(self,bool):
        self.midPoint = bool
        
    def setEnd(self,bool):
        self.endPoint = bool

    def getAddress(self):
        return self.address
        