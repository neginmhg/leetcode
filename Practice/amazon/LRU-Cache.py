class Node:
    def __init__(self, key=0, val=0, next =None, prev=None):
        self.key =key
        self.val =val
        self.next =next
        self.prev =prev
    

class LRUCache:
    def __init__(self, capacity: int):
        self.cap =capacity
        #map {key :node}
        self.map= {}
        #dummyLeft <-> node1 <-> node2 <->dummyRight
        self.dummyLeft =Node() #lru
        self.dummyRight = Node() #fru
        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft

    def remove(self, node):
        nextNode=node.next
        prevNode =node.prev
        nextNode.prev = prevNode
        prevNode.next = nextNode
        
    def add(self,node):
        fruNode=self.dummyRight.prev
        fruNode.next=node
        node.next = self.dummyRight
        node.prev= fruNode
        self.dummyRight.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            node=self.map[key]
            val =node.val
            self.remove(node)
            self.add(node)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
            #didn't add this line last time
            #need to make sure to create a new node
            self.map[key] = Node(key, value)
            self.add(self.map[key])
        else:
            self.map[key] = Node(key, value)
            self.add(self.map[key])
        if len(self.map) > self.cap:
            lru = self.dummyLeft.next
            self.remove(lru)
            del self.map[lru.key]
        
        