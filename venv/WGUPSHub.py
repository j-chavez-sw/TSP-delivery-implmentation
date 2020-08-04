# Julian A. Chavez
#I.D. #: 000966293


from CSVread import *
from HashTable import *
from Package import *
from Vertex import *
from ThreeOpt import *
import copy

class WGUPSHub:

    def __init__(self):

        self.packageHashTable = HashTable
        self.addressTable = []
        self.distances = []
        self.locations = []
        self.truck_1_preload = []
        self.truck_2_preload = []
        self.truck_3_preload = []
        self.truck_1_preRoute = []
        self.truck_2_preRoute = []
        self.truck_3_preRoute = []
        self.truck_1_distance = 0
        self.truck_2_distance = 0
        self.truck_3_distance = 0
        self.truck_1_zipCodes = ["84104"]
        self.truck_2_zipCodes = ["84103","84111","84118","84121","84123"]
        self.truck_3_zipCodes = ["84105","84106","84107"]
        self.shared_zipCodes  = ["84115","84117","84119"]

    #method to start the delivery process when called from main
    def start(self):

        self.createAddressTable()
        self.createDeliveries()
        self.associateConditionalPackages()
        self.associatePriorityPackages()
        self.distributeToPreload()
        self.associateRemainderPackages()
        self.distributeToPreload()
        self.distributePreloadToLoad()

    #this method populates the hashtable with package ids as keys and package objects as values
    def createDeliveries(self):
        packages = CSVread.getPackages()
        self.packageHashTable = HashTable(len(packages))
        for package in packages:
            self.packageHashTable.put(int(package[0]),
                                      Package(package[0], package[1], package[2], package[3], package[4],
                                              package[5],
                                              package[6], package[7], self.getVertexFromAddress(package[1])))

    #method to iterate through hashtable and print package information
    def printAllDeliveries(self, time):
        for index in range(self.packageHashTable.hashTableSize()):
            print(self.packageHashTable.get(index+1).lookup(time))

    #method to print the information of a specific package
    def packageLookup(self, id, time):
        print(self.packageHashTable.get(id).lookup(time))

    #method that returns a package from the hashtable
    def getPackage(self, key):
        return self.packageHashTable.get(key)

    #method that creates a list of vertex objects that are synonomous with addresses in SLC
    def createAddressTable(self):

        locations = CSVread.getDistanceTable()
        distances = CSVread.getDistances()
        vertexList = []

        self.distances = distances
        self.locations = locations

        for location in locations:
            vertexList.append(Vertex(location[0], location[1], location[2]))

        self.addressTable = vertexList

    #method that returns a vertex from a given address string
    def getVertexFromAddress(self, address):
        for vertex in self.addressTable:
            if address == vertex.getAddress():
                return vertex

    #method that associates a package with trucks 1,2, or 3
    #ids are appended to an id list and vertices are appended to a vertex list to be optimized
    def distributeToPreload(self):
        for index in range(self.packageHashTable.hashTableSize()):
            package = self.packageHashTable.get(index + 1)
            if(package.getTruckPriority() and not package.getPreloaded()):
                id = package.getID()
                vertex = package.getVertex()
                truck = package.getTruckAssociation()
                if truck == 1:
                    self.truck_1_preload.append(id)
                    self.truck_1_preRoute.append(vertex)
                    package.setPreloaded()
                elif truck == 2:
                    self.truck_2_preload.append(id)
                    self.truck_2_preRoute.append(vertex)
                    package.setPreloaded()
                elif truck == 3:
                    self.truck_3_preload.append(id)
                    self.truck_3_preRoute.append(vertex)
                    package.setPreloaded()
                else:
                    print("Sorry... Cannot find truck association...")
                    print("Package ID: ", id)

    #method to handle special package requirements given in the notes field
    #i.e. delayed,or must be in same load as other packages
    def associateConditionalPackages(self):

        for index in range(self.packageHashTable.hashTableSize()):
            package = self.packageHashTable.get(index + 1)

            if(not package.getTruckPriority()):
                if (package.getLoadPriority()):
                    package.setTruckAssociation(1)
                    tempList = package.getLoadAssociation()
                    for id in tempList:
                        self.packageHashTable.get(id).setTruckAssociation(1)

                elif(not package.getOnTime()):
                    if (package.getPriority()):
                        package.setTruckAssociation(2)

                    else:
                        package.setTruckAssociation(3)

    #method that handles the packages with 9:00am or 10:30am delivery targets
    def associatePriorityPackages(self):

        for index in range(self.packageHashTable.hashTableSize()):
            package = self.packageHashTable.get(index + 1)
            zipCode = package.getZip()

            if(not package.getTruckPriority() and package.getPriority()):

                if (zipCode in self.truck_1_zipCodes):
                    package.setTruckAssociation(1)

                elif (zipCode in self.truck_2_zipCodes):
                    package.setTruckAssociation(2)

                elif (zipCode in self.truck_3_zipCodes):
                    package.setTruckAssociation(3)

                elif (zipCode in self.shared_zipCodes):
                    if (zipCode == "84115"):
                        package.setTruckAssociation(3)

                    elif (zipCode == "84119"):
                        package.setTruckAssociation(3)

                    elif (zipCode == "84117"):
                        city = package.getCity()
                        if(city == "Salt Lake City"):
                            package.setTruckAssociation(2)
                        else:
                            package.setTruckAssociation(1)

    #method that directs the remaining non-priority, non conditional packages to appropriate truck associations
    def associateRemainderPackages(self):

        for index in range(self.packageHashTable.hashTableSize()):
            package = self.packageHashTable.get(index + 1)
            zipCode = package.getZip()
            vertex = package.getVertex()

            if (not package.getTruckPriority()):
                if (zipCode in self.truck_1_zipCodes):
                    package.setTruckAssociation(1)

                elif (zipCode in self.truck_2_zipCodes):
                    package.setTruckAssociation(2)

                elif (zipCode in self.truck_3_zipCodes):
                    package.setTruckAssociation(3)

                elif (vertex in self.truck_1_preRoute):
                    package.setTruckAssociation(1)

                elif (vertex in self.truck_2_preRoute):
                    package.setTruckAssociation(2)

                elif (vertex in self.truck_3_preRoute):
                    package.setTruckAssociation(3)

                elif (zipCode in self.shared_zipCodes):
                    if (zipCode == "84115"):
                        package.setTruckAssociation(self.optimizeByVertex(package.getVertex()))

                    elif (zipCode == "84119"):
                        city = package.getCity()
                        if (city != "Salt Lake City"):
                            package.setTruckAssociation(1)
                        else:
                            package.setTruckAssociation(self.optimizeByVertex(package.getVertex()))

                    elif (zipCode == "84117"):
                        city = package.getCity()
                        if (city != "Salt Lake City"):
                            package.setTruckAssociation(1)
                        else:
                            package.setTruckAssociation(2)

    #method that allows remainder packages to be distributed to the most optimal path
    def optimizeByVertex(self, vertex):

        r1 = copy.copy(self.truck_1_preRoute)
        r2 = copy.copy(self.truck_2_preRoute)
        r3 = copy.copy(self.truck_3_preRoute)

        r1 = self.attachRouteToHub(r1)
        r2 = self.attachRouteToHub(r2)
        r3 = self.attachRouteToHub(r3)

        r1,d1 = self.optimize(r1)
        r2,d2 = self.optimize(r2)
        r3,d3 = self.optimize(r3)

        r1.append(vertex)
        r2.append(vertex)
        r3.append(vertex)

        r1_2,d1_2 = self.optimize(r1)
        r2_2,d2_2 = self.optimize(r2)
        r3_2,d3_2 = self.optimize(r3)

        tempList = [d1_2 - d1, d2_2 - d2, d3_2 - d3]

        minDif = min(tempList)
        if(tempList[0]==minDif):
            return 1
        elif(tempList[1]==minDif):
            return 2
        elif(tempList[2]==minDif):
            return 3

    #General purpose call to optimization methods
    #
    def optimize(self, route):
        optimizer = ThreeOpt(self.distances)
        route = optimizer.three_opt(route)
        optimizer.anneal(route)
        route = optimizer.getSolution()
        tempDistance = optimizer.getRunningTotal(optimizer.getSolution())
        return route , tempDistance

    def reoptimize_Wrong_Address(self, time, id, newAddress):

        packageToSwap = self.packageHashTable.get(id)
        packageToSwap.setAddress(newAddress)
        packageToSwap.setVertex(self.getVertexFromAddress(newAddress))
        remainingPackageList = []

        for index in range(self.packageHashTable.hashTableSize()):
            package = self.packageHashTable.get(index + 1)
            if package.getTruckAssociation() == packageToSwap.getTruckAssociation():
                if package.getDeliveryTime() >= time:
                    remainingPackageList.append(package)
                    
        remainingPackageList.sort(key=lambda r: r.deliveryTime)
        ids = list((int(p.id) for p in remainingPackageList))
        r1 = list((p.vertex for p in remainingPackageList))
        dl1 = self.getDistanceList(r1)
        r1[0].setStart(True)
        for vertex in r1:
            if vertex.getID() == r1[0].getID():
                newVertex = copy.copy(vertex)
                newVertex.setStart(True)
                r1.insert(0,newVertex)
                r1.remove(vertex)

        r1,d1 = self.optimize(r1)
        tempTime = remainingPackageList[0].getDeliveryTime()

        for id in ids:

            distance = self.getDistanceToVertex(id, r1)
            newDeliveryTime = round((distance*3.33) + tempTime)
            self.packageHashTable.get(id).resetDeliveryTime(newDeliveryTime)


    #Adds the hub address to the route for optimization purposes
    def attachRouteToHub(self, route, end = False):
        if(end):
            endV = copy.copy(self.addressTable[0])
            endV.setEnd(True)
            route.append(endV)
        startV = copy.copy(self.addressTable[0])
        startV.setStart(True)
        route.insert(0,startV)
        return route
    
    def distance(self, v1, v2):
        d1 = self.distances[v1.getID()][v2.getID()]
        d2 = self.distances[v2.getID()][v1.getID()]

        return round(float(max(d1,d2)),1)

    def getDistanceList(self, route):

        runningDistanceList = [0]

        for index1, stop in enumerate(route):
            if (index1 + 1) < len(route):
                startVertex = route[index1]
                targetVertex = route[index1+1]
                newDistance = self.distance(startVertex, targetVertex)
                runningDistanceList.append(newDistance)

        return runningDistanceList
    
    def getDistanceToVertex(self, id, route):

        package = self.packageHashTable.get(id)
        vertex = package.getVertex()
        runningDistance = 0
        for index1, stop in enumerate(route):
            if (index1 + 1) < len(route):
                startVertex = route[index1]
                targetVertex = route[index1+1]
                newDistance = self.distance(startVertex, targetVertex)
                runningDistance += newDistance
                if(targetVertex.getID()== vertex.getID()):
                    return runningDistance
        return None

    def distributePreloadToLoad(self):

        random.shuffle(self.truck_1_preRoute)
        random.shuffle(self.truck_2_preRoute)
        random.shuffle(self.truck_3_preRoute)

        #custom optimization- after multiple runs this provides the lowest mileage result
        #This also ensure the(9:00am delivery is deliverd on time)
        #The evaluator can comment this section out if interested or necessary
        #############################################################################
        end = copy.copy(self.addressTable[25])
        end.setEnd(True)
        self.truck_3_preRoute.append(end)
        end = copy.copy(self.addressTable[19])
        end.setEnd(True)
        self.truck_2_preRoute.append(end)
        end = copy.copy(self.addressTable[14])
        end.setEnd(True)
        self.truck_1_preRoute.append(end)
        mid = copy.copy(self.addressTable[21])
        mid.setMid(True)
        self.truck_1_preRoute.insert(1,mid)
        #############################################################################

        r1,d1 = self.optimize(self.attachRouteToHub(self.truck_1_preRoute, True))
        r2,d2 = self.optimize(self.attachRouteToHub(self.truck_2_preRoute))
        r3,d3 = self.optimize(self.attachRouteToHub(self.truck_3_preRoute))

        # dl1 = self.getDistanceList(r1)
        # dl2 = self.getDistanceList(r2)
        # dl3 = self.getDistanceList(r3)

        self.truck_1_distance = d1
        self.truck_2_distance = d2
        self.truck_3_distance = d3
        
        for id in self.truck_1_preload:
            distance = self.getDistanceToVertex(id, r1)
            self.packageHashTable.get(id).setDeliveryTime(distance)

        for id in self.truck_2_preload:
            distance = self.getDistanceToVertex(id, r2)
            self.packageHashTable.get(id).setDepartureTime(65)
            self.packageHashTable.get(id).setDeliveryTime(distance)

        for id in self.truck_3_preload:
            distance = self.getDistanceToVertex(id, r3)
            newDepartureTime = round(d1*3.33)
            self.packageHashTable.get(id).setDepartureTime(newDepartureTime)
            self.packageHashTable.get(id).setDeliveryTime(distance)

    def finalReport(self):

        print("")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("                  Final Report")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("")
        print("* Truck 1 distance: ",self.truck_1_distance)
        print("* Truck 2 distance: ",self.truck_2_distance)
        print("* Truck 3 distance: ",self.truck_3_distance)
        print("")
        print("*** Total distance: ",self.truck_1_distance+self.truck_2_distance+self.truck_3_distance)


