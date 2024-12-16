"""
Design a data structure that supports the following operations:

inc(key): Inserts a new key with a value of 1. If the key already exists, increment its value by 1.
dec(key): Decrements an existing key by 1. If the value is 0 after the decrement, the key should be removed from the data structure.
getMaxKey(): Returns one of the keys with the maximal value. If no key exists, return an empty string "".
getMinKey(): Returns one of the keys with the minimal value. If no key exists, return an empty string "".


Constraints:
The operations inc, dec, getMaxKey, and getMinKey must be done in O(1) time complexity.
The number of different keys in the data structure is at most 10^5.
The keys used are strings of lowercase letters.

"""
class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_node = {}  # Maps key to Node
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_after_node(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def inc(self, key: str) -> None:
        if key not in self.key_node:
            # If the key doesn't exist, insert it with count 1
            if self.head.next.count != 1:
                new_node = Node(1)
                self._insert_after_node(self.head, new_node)
            self.head.next.keys.add(key)
            self.key_node[key] = self.head.next
        else:
            # If the key exists, move it to the next count
            curr_node = self.key_node[key]
            next_node = curr_node.next
            if next_node.count != curr_node.count + 1:
                next_node = Node(curr_node.count + 1)
                self._insert_after_node(curr_node, next_node)
            next_node.keys.add(key)
            curr_node.keys.remove(key)
            if not curr_node.keys:
                self._remove_node(curr_node)
            self.key_node[key] = next_node

    def dec(self, key: str) -> None:
        curr_node = self.key_node[key]
        if curr_node.count == 1:
            # If count becomes 0, remove the key
            del self.key_node[key]
        else:
            # Move to the previous count
            prev_node = curr_node.prev
            if prev_node.count != curr_node.count - 1:
                prev_node = Node(curr_node.count - 1)
                self._insert_after_node(curr_node.prev, prev_node)
            prev_node.keys.add(key)
            self.key_node[key] = prev_node
        curr_node.keys.remove(key)
        if not curr_node.keys:
            self._remove_node(curr_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
#Why next()?
#The keys in each node are stored in a Python set, and sets do not have an inherent order. Using next(iter(...)) gives us any key from the set, since we just need one valid key with the maximum count.
""""
Choice of Solution:
The key challenge in this problem is to perform all operations (inc, dec, getMaxKey, getMinKey) in O(1) average time complexity. This requirement led to the choice of combining two data structures:

1. A hash map (dictionary in Python) for quick key-value lookups.
2. A doubly linked list to maintain the order of counts efficiently.

This combination allows us to have the best of both worlds: fast lookups and easy reordering.

How it Works:
The solution uses a custom Node class to represent groups of keys with the same count. These nodes are arranged in a doubly linked list, sorted by count.

1. Hash Map (key_node):
   - Maps each key to its corresponding Node in the linked list.
   - Allows O(1) access to a key's current count and position.

2. Doubly Linked List:
   - Each Node represents a count and contains a set of keys with that count.
   - Nodes are arranged in ascending order of count.
   - Allows O(1) insertion and deletion of nodes.

3. Key Operations:
   - inc(key): 
     - If the key doesn't exist, add it to the first node or create a new node with count 1.
     - If it exists, move it to the next count, creating a new node if necessary.
   - dec(key):
     - Move the key to the previous count or remove it if the count becomes 0.
   - getMaxKey(): Return a key from the last non-dummy node.
   - getMinKey(): Return a key from the first non-dummy node.

Example:
Let's walk through an example to illustrate how this works:

```python
allOne = AllOne()

# Initial state: empty
# List: [Head] <-> [Tail]

allOne.inc("apple")
# List: [Head] <-> [Count:1, Keys:{"apple"}] <-> [Tail]
# key_node: {"apple": Node(count=1)}

allOne.inc("banana")
# List: [Head] <-> [Count:1, Keys:{"apple", "banana"}] <-> [Tail]
# key_node: {"apple": Node(count=1), "banana": Node(count=1)}

allOne.inc("apple")
# List: [Head] <-> [Count:1, Keys:{"banana"}] <-> [Count:2, Keys:{"apple"}] <-> [Tail]
# key_node: {"apple": Node(count=2), "banana": Node(count=1)}

allOne.getMaxKey()  # Returns "apple"
allOne.getMinKey()  # Returns "banana"

allOne.dec("apple")
# List: [Head] <-> [Count:1, Keys:{"apple", "banana"}] <-> [Tail]
# key_node: {"apple": Node(count=1), "banana": Node(count=1)}

allOne.getMaxKey()  # Returns "apple" or "banana" (both have count 1)
allOne.getMinKey()  # Returns "apple" or "banana" (both have count 1)
```

In this example, we can see how the structure maintains the counts efficiently:
- Keys with the same count are grouped in the same node.
- Incrementing or decrementing a key moves it to the appropriate node.
- The linked list structure allows for easy access to max and min keys.

This implementation ensures that all operations maintain O(1) average time complexity, meeting the problem's requirements. The combination of a hash map for quick lookups and a doubly linked list for maintaining order allows for efficient updates and retrieval of max/min keys.

"""