# Julian A. Chavez
#I.D. #: 000966293


class HashTable:

    #when a HashTable object is created, it reserves the given size
    #fulfills the self, adjusting requirement
    def __init__(self, size):
        self.table = [None] * size

    #simple hashing function
    def hash(self, key):

        hk = int(key) % len(self.table)
        return hk

    #insertion function, if there is a collision then the key/value pair is appended as a list to that index
    #fulfills the self, adjusting requirement
    #essentially O(1) time complexity, in theory it could be slightly slower since there is a possibility of iterating
    #through multiple pairs at a single index, however, the hash table is fixed in size to the amount of deliveries for
    #the day, so there should not be any collision within this project scope.
    def put(self, key, value):

        tableIndex = self.hash(key)

        if self.table[tableIndex] is not None:

            for entry in self.table[tableIndex]:
                if entry[0] == key:
                    entry[1] == value
                    return True

            else:
                self.table[tableIndex].append([key, value])
                return True

        else:
            self.table[tableIndex] = []
            self.table[tableIndex].append([key, value])
            return True

    #simple retrieval method
    def get(self, key):

        tableIndex = self.hash(key)
        
        if self.table[tableIndex] is not None:
            for entry in self.table[tableIndex]:
                if entry[0] == key:
                    return entry[1]

    #returns the length of the hashtable to help other classes iterate through the hashtable
    def hashTableSize(self):
        return len(self.table)
