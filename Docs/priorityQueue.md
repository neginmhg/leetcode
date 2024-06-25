# Priority Queue Implementation in Python using `heapq`

A priority queue is a data structure that stores elements along with their priorities and allows elements to be removed in order of their priority. In Python, you can implement a priority queue efficiently using the `heapq` module, which provides a min-heap implementation.

## Basics of Priority Queue

### Operations:

- **Insertion**: Insert an element with a priority.
- **Deletion**: Remove the element with the highest (or lowest) priority.
- **Peek**: Retrieve the element with the highest (or lowest) priority without removing it.

### Implementation in Python

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def peek(self):
        return self._queue[0][-1]

    def __len__(self):
        return len(self._queue)
```

### Explanation

- **Initialization**: `_queue` is initialized as an empty list, `_index` keeps track of insertion order for tie-breaking.
- **Push Operation**: `push` method adds an element with its priority using `heappush`.
- **Pop Operation**: `pop` method removes and returns the item with the smallest priority using `heappop`.
- **Peek Operation**: `peek` method retrieves the item with the smallest priority without removing it.
- **Length Operation**: `__len__` method returns the number of elements in the priority queue.

### Example Usage

```python
pq = PriorityQueue()
pq.push("task1", 5)
pq.push("task2", 1)
pq.push("task3", 3)

print(pq.pop())  # Output: task2 (priority 1)
print(pq.pop())  # Output: task3 (priority 3)

pq.push("task4", 0)
print(pq.peek())  # Output: task4 (priority 0)

print(len(pq))  # Output: 2 (two elements left in the priority queue)
```

### Tips for Usage

- Ensure that the items you push into the priority queue can be compared (either by default comparison or by defining a custom comparison method).
- Handle tie-breaking if needed by including an index or a timestamp along with priorities.

This should provide you with a clear understanding of how to implement and utilize a priority queue in Python using `heapq`.
