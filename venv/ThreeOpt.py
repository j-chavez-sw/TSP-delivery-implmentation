# Julian A. Chavez
#I.D. #: 000966293



from Vertex import *
import random
from math import exp
import copy


# inspiration from a Udemy course by Holczer Balazs - https://www.udemy.com/course/advanced-algorithms-in-java/
# inspiration from Wikipedia article on 3-opt algorithms - https://en.wikipedia.org/wiki/3-opt
class ThreeOpt:

    def __init__(self, vertexList):
        self.list = vertexList
        self.runningTotal = 0
        self.best = []
        self.runningDistanceList = []

    #method to determine the distance between two stops. Uses the 2 dimensional matrix created from reading the given
    #excel file, converted to csv
    def distance(self, v1, v2):
        d1 = self.list[v1.getID()][v2.getID()]
        d2 = self.list[v2.getID()][v1.getID()]

        return round(float(max(d1, d2)), 1)

    #method returns the total distance of a given route
    def getRunningTotal(self, route):

        total = 0
        self.runningDistanceList = []

        for index1, stop in enumerate(route):
            if (index1 + 1) < len(route):
                startVertex = route[index1]
                targetVertex = route[index1 + 1]
                newDistance = self.distance(startVertex, targetVertex)
                self.runningDistanceList.append(newDistance)
                total += newDistance

        return round(total,1)

    #this method determines whether the route segment contains a stop that is not swappable
    #i.e. stops at the hub, priority swaps, or custom optimization stops that are at fixed points in the route
    def isSegmentSwappable(self, route):
        for vertex in route:
            if not vertex.isSwappable():
                return False
        return True

    #inspiration from Wikipedia article on 3-opt algorithms - https://en.wikipedia.org/wiki/3-opt
    def reverse(self, route, index1, index2, index3):
        r1 = route[index1 - 1]
        r2 = route[index1]
        r3 = route[index2 - 1]
        r4 = route[index2]
        r5 = route[index3 - 1]
        r6 = route[index3 % len(route)]
        s1 = self.distance(r1, r2) + self.distance(r3, r4) + self.distance(r5, r6)
        s2 = self.distance(r1, r3) + self.distance(r2, r4) + self.distance(r5, r6)
        s3 = self.distance(r1, r2) + self.distance(r3, r5) + self.distance(r4, r6)
        s4 = self.distance(r1, r4) + self.distance(r5, r2) + self.distance(r3, r6)
        s5 = self.distance(r6, r2) + self.distance(r3, r4) + self.distance(r5, r1)

        if s1 > s2:
            if(self.isSegmentSwappable(route[index1:index2])):
                route[index1:index2] = reversed(route[index1:index2])
                return -s1 + s2
        elif s1 > s3:
            if(self.isSegmentSwappable(route[index2:index3])):
                route[index2:index3] = reversed(route[index2:index3])
                return -s1 + s3
        elif s1 > s5:
            if(self.isSegmentSwappable(route[index1:index3])):
                route[index1:index3] = reversed(route[index1:index3])
                return -s1 + s5
        elif s1 > s4:
            if (self.isSegmentSwappable(route[index2:index3]) and self.isSegmentSwappable(route[index1:index2])):
                temp = route[index2:index3] + route[index1:index2]
                route[index1:index3] = temp
                return -s1 + s4
        return 0

    #inspiration from Wikipedia article on 3-opt algorithms - https://en.wikipedia.org/wiki/3-opt
    # O(n^3) time complexity
    # the 3-opt algorithm iterates through different subsets of a delivery route and compares them to find more
    # efficient pathways. if a more efficient solution is found, the subsets are swapped
    def three_opt(self, route):
        counter = 0
        while True:
            counter+=1
            change = 0
            for (index1, index2, index3) in self.subsets(len(route)):
                change += self.reverse(route, index1, index2, index3)
            if change >= 0:
                break
            if counter == 1000:
                break
        self.best = route
        return route

    #inspiration from Wikipedia article on 3-opt algorithms - https://en.wikipedia.org/wiki/3-opt
    def subsets(self, size):
        return ((a, b, c)
                for a in range(size)
                for b in range(a + 2, size)
                for c in range(b + 2, size + (a > 0)))

    #this method is called by the anneal() method
    #it determines whether the stop swap is worth swapping
    def acceptance(self, energy, newEnergy, temp):
        if(newEnergy < energy):
            return 1.0

        return exp((energy-newEnergy)/temp)

    #method returns the optimized route for the class instance
    def getSolution(self):
        return self.best

    #method returns a list of distances between route stops
    def getDistanceList(self):
        return self.runningDistanceList

    #inspiration from a Udemy course by Holczer Balazs - https://www.udemy.com/course/advanced-algorithms-in-java/
    #man algorithms that are greedy or find local minimums to create a path can sacrifice global optimization for local
    #minimization. the annealing process can help break apart those clusters to find a more efficient global optimization
    #instead of iterating through a route like many other algorithms, the annealing process find random locations and
    #swaps them, and checks them for a better result.
    #O(n) time complexity
    def anneal(self, tour):
        temp = 10000.0
        cr = .003

        self.best = tour


        while(temp > 1):
            current = copy.copy(self.best)
            new_route = copy.copy(current)


            randIndex1 = int(len(new_route) * random.random())
            vertex1 = new_route[randIndex1]
            randIndex2 = int(len(new_route) * random.random())
            vertex2 = new_route[randIndex2]

            if(vertex1.isSwappable() and vertex2.isSwappable()):

                new_route[randIndex2] = vertex1
                new_route[randIndex1] = vertex2


                currentEnergy = self.getRunningTotal(current)
                neighborEnergy = self.getRunningTotal(new_route)


                if(self.acceptance(currentEnergy, neighborEnergy, temp) > random.random()):
                    current = copy.copy(new_route)

                if(self.getRunningTotal(current) < self.getRunningTotal(self.best)):
                    self.best = copy.copy(current)

                temp *= 1 - cr


