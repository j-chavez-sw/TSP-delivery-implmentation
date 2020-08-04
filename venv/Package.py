# Julian A. Chavez
#I.D. #: 000966293


class Package:
    
    def __init__(self, id, add, city, state, zip, deadline, kilo, notes, vertex):
        
        self.id = id
        self.address = add
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.kilo = kilo
        self.notes = notes
        self.vertex = vertex
        self.status ="HUB"
        self.departureTime= 480
        self.deliveryTime = 0
        self.unloaded = True
        self.preloaded = False
        self.loaded = False
        self.enroute = False
        self.delivered = False
        self.priority = False
        self.onTime = True
        self.loadPriority = False
        self.loadAssociation = []
        self.truckPriority = False
        self.truckAssociation = 0
        self.discrepant = False

        #this instantiation logic helps when the packages are filtered for conditions in the WGUPSHub class
        if deadline != "EOD":
            self.priority = True

        if "Delayed" in notes:
            self.onTime = False
            self.status = "DELAYED"

        if "Must" in notes:
            self.loadPriority = True
            tempnotes = notes.split(", ", 1)
            notes = tempnotes[0]
            notes2 = tempnotes[1]

            id1 = int("".join(filter(str.isdigit, notes)))
            id2 = int("".join(filter(str.isdigit, notes2)))
            self.loadAssociation = [id1, id2]

        if "Can only be" in notes:
            self.truckPriority = True
            self.truckAssociation = int("".join(filter(str.isdigit, notes)))

        if "Wrong" in notes:
            self.discrepant = True

    def __str__(self):
        return self.address

    #this class mostly contains setters and getters
    def getUnloaded(self):
        return self.unloaded
    
    def getPreloaded(self):
        return self.preloaded

    def getLoaded(self):
        return self.loaded
    
    def getEnroute(self):
        return self.enroute

    def getDelivered(self):
        return self.delivered

    def getPriority(self):
        return self.priority

    def getLoadPriority(self):
        return self.loadPriority

    def getLoadAssociation(self):
        return self.loadAssociation

    def getOnTime(self):
        return self.onTime

    def getTruckPriority(self):
        return self.truckPriority

    def getTruckAssociation(self):
        return self.truckAssociation

    def getDiscrepant(self):
        return self.discrepant

    def setUnloaded(self):
        self.unloaded = True
        self.loaded = False
        self.enroute = False
        self.delivered = False
        self.status = "Waiting - HUB"

    def setPreloaded(self):
        self.preloaded = True

    def setLoaded(self):
        self.unloaded = False
        self.loaded = True
        self.enroute = False
        self.delivered = False
        self.status = "Loaded - TRUCK"

    def setEnroute(self):
        self.unloaded = False
        self.loaded = False
        self.enroute = True
        self.delivered = False
        self.status = "Enroute - TRUCK"

    def setDelivered(self):
        self.unloaded = False
        self.loaded = False
        self.enroute = False
        self.delivered = True
        hr = int(self.deliveryTime/60)
        min = int(self.deliveryTime % 60)
        timeString = str(hr) + ":" + str(min).zfill(2)
        self.status = "Delivered @ " + timeString
        
    def setTruckAssociation(self, truckNumber):
        self.truckAssociation = truckNumber
        self.truckPriority = True

    def lookup(self, minutes):
        if(minutes < self.departureTime):
            self.setUnloaded()
        elif(minutes >= 480 and minutes < self.departureTime):
            self.setLoaded()
        elif(minutes >= self.departureTime and minutes < self.deliveryTime):
            self.setEnroute()
        elif(minutes >= self.deliveryTime):
            self.setDelivered()
        return self.getInformation()
        
    def getInformation(self):
        string = self.id + " | " + self.address + " | " + self.status + " | " + self.city + " | " + self.deadline + " | " + self.zip + " | " + self.kilo
        return string

    def setDeliveryTime(self, distance):
        self.deliveryTime = round(3.33*distance) + self.departureTime
        
    def resetDeliveryTime(self, time):
        self.deliveryTime = time


    def getDeliveryTime(self):
        return self.deliveryTime
    
    def setDepartureTime(self, time):
        self.departureTime += time
        
    def getDepartureTime(self):
        return self.departureTime

    def getVertex(self):
        return self.vertex

    def setVertex(self, vertex):
        self.vertex = vertex
    
    def setStatus(self, status):
        self.status = status
    
    def getStatus(self):
        return self.status
    
    def getID(self):
        return int(self.id)
    
    def getAddress(self):
        return self.address
    
    def setAddress(self, address):
        self.address = address
    
    def getCity(self):
        return self.city
    
    def getZip(self):
        return self.zip
    
    def getDeadline(self):
        return self.deadline
    
    def getNotes(self):
        return self.notes