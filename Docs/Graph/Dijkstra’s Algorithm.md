### **Dijkstra’s Algorithm: Everything You Need to Know**

Dijkstra’s algorithm is a **single-source shortest path algorithm** for graphs with **non-negative edge weights**. It computes the shortest distance from a given source node to all other nodes in the graph.

---

### **Key Concepts**

1. **Graph Representation**:
   - Use an **adjacency list** for efficiency. This represents the graph as a dictionary where keys are nodes and values are lists of `(neighbor, weight)` pairs.

2. **Algorithm Mechanics**:
   - Maintain a **priority queue (min-heap)** to always process the closest unvisited node.
   - Keep track of the shortest known distance to each node using a `distance` dictionary initialized to infinity (`float('inf')`).
   - Update neighbors of the current node if a shorter path is found.
   - Stop once all nodes are visited or the target node is reached.

3. **Time Complexity**:
   - **O((V + E) log V)** using a min-heap.
     - **V**: Number of vertices (nodes).
     - **E**: Number of edges.

4. **Properties**:
   - Works only for graphs with **non-negative weights**.
   - It does **not handle negative weights**; use Bellman-Ford in that case.
   - If the graph is sparse, Dijkstra is very efficient.

---

### **Template Code for Dijkstra’s Algorithm**

Here’s a reusable Python3 implementation:

```python
import heapq

def dijkstra(graph, source):
    """
    Dijkstra's Algorithm to find the shortest path from a source node to all other nodes.
    
    :param graph: Adjacency list where graph[u] = [(v, weight), ...]
    :param source: The starting node.
    :return: A dictionary with the shortest distances to all nodes.
    """
    # Priority queue (min-heap): stores (distance, node)
    min_heap = [(0, source)]
    # Distance dictionary: shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    
    while min_heap:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(min_heap)
        
        # Skip processing if we have already found a better path
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    
    return distances
```

---

### **How to Use This Template**

1. **Input Format**:
   - The graph should be represented as an adjacency list.
   - Example: 
     ```python
     graph = {
         0: [(1, 4), (2, 1)],
         1: [(3, 1)],
         2: [(1, 2), (3, 5)],
         3: []
     }
     source = 0
     ```

2. **Output**:
   - A dictionary with the shortest distance from the source to every other node.
   - For the example above:
     ```
     {0: 0, 1: 3, 2: 1, 3: 4}
     ```

3. **Variants**:
   - To find the shortest distance to a specific target node, you can break out of the loop once the target is dequeued from the priority queue.
   - Add a `prev` dictionary to reconstruct the shortest path.

---

### **Common Modifications**

#### **1. Find the Shortest Path (Not Just Distance)**
Add a `prev` dictionary to store the predecessor of each node:

```python
def dijkstra_with_path(graph, source):
    min_heap = [(0, source)]
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    prev = {node: None for node in graph}  # To reconstruct the path

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current_node
                heapq.heappush(min_heap, (distance, neighbor))
    
    return distances, prev

# Path reconstruction
def reconstruct_path(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return path[::-1]  # Reverse the path
```

#### **2. For Large Graphs (Space Optimization)**
If memory is a concern, store visited nodes in a `set` instead of a `distances` dictionary.

#### **3. Handle Edge Cases**
- **Disconnected Graph**: Ensure the algorithm returns `float('inf')` for unreachable nodes.
- **Empty Graph**: Return an empty dictionary.
- **Negative Weights**: Check for negatives before running Dijkstra.

---

### **Practice Problems on LeetCode**

1. **Medium**:
   - [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)
   - [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

2. **Hard**:
   - [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
   - [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/)

---

### **Tips for Using Dijkstra’s Algorithm in Problems**

1. **Recognize Weighted Graphs**: Problems involving distances or costs often need Dijkstra.
2. **Non-Negative Weights**: Ensure all weights are non-negative, or use Bellman-Ford if negative weights are possible.
3. **Target Node**: If only the shortest path to a target node is needed, break the loop early.
4. **Edge Cases**: Always test for disconnected nodes and unreachable targets.
