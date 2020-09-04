#implement a hashtable with chaining in python
#initialize Node
class ListNode:

    def __init__(self,key, value):
        self.pair = (key,value)
        self.next = None

class HashTable:

    def __init__(self):
        self.m = 100 #number size of table
        self.table = [None] * self.m


    def is_empty(self, hashvalue):
        return self.table[hashvalue] == None

    def hash_function(self, key):
        hashvalue = key % len(self.table)
        return hashvalue

    def insert(self, key, value):
        new = ListNode(key,value)
        hashvalue = self.hash_function(key)

        if self.is_empty(hashvalue):
            self.table[hashvalue] = new
        else:
            new.next = self.table[hashvalue]
            self.table[hashvalue] = new



    #def print_table(self):


    #driver code
if __name__=='__main__':

    hashtable = HashTable()
    hashtable.insert(5,"Terje")
    hashtable.insert(5,"Finn")
    print(hashtable.table)
