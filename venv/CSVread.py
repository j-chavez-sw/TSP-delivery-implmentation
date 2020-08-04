# Julian A. Chavez
#I.D. #: 000966293

import csv

class CSVread:



    def getDistanceTable():
        with open('DistanceTable.csv') as distanceTable:
            results = csv.reader(distanceTable, delimiter=',')
            results = list(results)
        
        return results
        
    def getDistances():
        with open('Distances.csv') as distances:
            resultsDistances = csv.reader(distances, delimiter=',')
            resultsDistances = list(resultsDistances)
    
        return resultsDistances

    def getPackages():
        with open('Packages.csv') as packages:
            resultsPackages = csv.reader(packages, delimiter=',')
            resultsPackages = list(resultsPackages)

        return resultsPackages