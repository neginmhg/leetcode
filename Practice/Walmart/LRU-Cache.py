class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev = self.next = None
    

class LRUCache:
    def __init__(self,capacity:int):
        self.cap = capacity
        self.cache={}   #map key to node
        self.dummyLeft, self.dummyRight = Node(0,0),Node(0,0)

        #Left= LRU ,Right= MRU
        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft

    def remove(self, node):
        #need prev node and next node to point them together
        prev, next = node.prev, node.next
        prev.next , next.prev= next, prev

    def insert(self,node):
        MRU = self.dummyRight
        prev = MRU.prev
        prev.next , MRU.prev = node
        node.next, node.prev = MRU, prev
    def get(self, key:int)->int:
        #everytime we get need to update it to MRU
        #need helper fucntions ; remove and insert

        if key in self.cache:
            #remove from Doubly linkedlist
            #re-insert to Doubly linkedlist
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key:int, value:int)->None:
        #if key is already in cache, we just need to update it and update to MRU
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        #update Doubly linkedlist
        self.insert(self.cache[key])

        #with capacity need to check len of cache to be <=capacity
        if len(self.cache) > self.cap:
            #remove MRU from Doubly linkedlist
            #remove it from cache
            lru = self.dummyLeft.next
            self.remove(lru)
            del self.cache[lru.val]
    


    #time is O(1)
    #space is O(n)