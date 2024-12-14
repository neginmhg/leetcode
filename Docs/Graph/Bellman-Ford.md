### **Bellman-Ford Algorithm Overview**

https://www.youtube.com/watch?v=obWXjtg0L64

The **Bellman-Ford Algorithm** is a well-known algorithm used to find the shortest path from a single source node to all other nodes in a weighted graph. Unlike **Dijkstra's Algorithm**, which works only with graphs containing non-negative weights, the Bellman-Ford algorithm can handle graphs with negative edge weights and can also detect negative weight cycles.

### **Key Characteristics of Bellman-Ford**
- **Single Source Shortest Path**: Finds the shortest path from a starting node to all other nodes.
- **Handles Negative Weights**: Unlike Dijkstra's algorithm, Bellman-Ford can handle negative edge weights.
- **Detects Negative Weight Cycles**: The algorithm can also detect if there is a negative weight cycle in the graph. A negative cycle means there’s a cycle in the graph where the sum of the edge weights is negative, which implies that there’s no finite shortest path.
- **Less Efficient than Dijkstra**: While Bellman-Ford works for graphs with negative weights, it is generally slower than Dijkstra's algorithm when there are no negative weight edges, with a time complexity of \(O(V \times E)\).

### **Steps of the Bellman-Ford Algorithm**

1. **Initialization**:
   - Create a distance array `dist[]` to hold the shortest distance from the source node to each other node. Initialize all distances to infinity (`∞`), except the source node, which is set to 0.
     ```python
     dist[source] = 0
     dist[other_nodes] = ∞
     ```

2. **Relaxation**:
   - For each edge `(u, v, weight)` in the graph, if the distance to `v` through `u` is shorter than the current known distance to `v`, update it:
     ```python
     if dist[u] + weight < dist[v]:
         dist[v] = dist[u] + weight
     ```
   - This relaxation process is repeated **V-1 times** where `V` is the number of vertices (nodes) in the graph. The reason for repeating `V-1` times is that the longest path in a graph can have at most `V-1` edges (if there are no cycles).

3. **Negative Cycle Detection**:
   - After relaxing all edges `V-1` times, we perform an additional pass to check for negative weight cycles. If any edge `(u, v)` can still be relaxed (i.e., if `dist[u] + weight < dist[v]`), then a negative weight cycle exists, and the algorithm reports this.

### **Time Complexity**
- The time complexity of the Bellman-Ford algorithm is **O(V * E)**, where:
  - `V` is the number of vertices (nodes).
  - `E` is the number of edges.
  
  This is because in the worst case, we perform **V-1 relaxations** for every edge, resulting in **V * E** operations.

### **Space Complexity**
- The space complexity is **O(V)** because we need to store the distances for each of the `V` nodes.

### **When to Use Bellman-Ford**
- **Negative Edge Weights**: Bellman-Ford is useful when the graph contains edges with negative weights.
- **Negative Weight Cycles**: Bellman-Ford can detect negative weight cycles in the graph, which is a scenario that Dijkstra's algorithm cannot handle.
- **Simplicity**: Bellman-Ford is simple to implement and doesn’t require complex data structures like heaps or priority queues, unlike Dijkstra’s algorithm.

---

### **Bellman-Ford Algorithm in Code (Python)**

Here’s how you can implement the Bellman-Ford algorithm in Python:

```python
class Solution:
    def bellmanFord(self, edges, V, source):
        # Initialize the distance array with infinity
        dist = [float('inf')] * V
        dist[source] = 0
        
        # Relax all edges V-1 times
        for _ in range(V - 1):
            for u, v, weight in edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
        
        # Check for negative weight cycles
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                print("Graph contains negative weight cycle")
                return None  # or return an indication of a negative cycle
        
        return dist
```

### **Explanation of the Code**
- **Initialization**: The `dist[]` array is initialized with `infinity` for all nodes except the source node, which is set to 0.
- **Relaxation**: For each of the `V-1` iterations, all edges are relaxed, meaning we check if the current distance can be updated to a smaller value through the edge `(u, v)`.
- **Negative Cycle Detection**: After the `V-1` relaxations, we check one more time to see if any edge can still be relaxed. If so, it means there is a negative weight cycle in the graph.

## **Advantages of Bellman-Ford**
1. **Handles Negative Weights**: Unlike Dijkstra's algorithm, Bellman-Ford can handle negative weights.
2. **Cycle Detection**: It can detect negative weight cycles, which is a major advantage in certain types of graphs.

## **Disadvantages of Bellman-Ford**
1. **Inefficient for Large Graphs**: Its time complexity of \(O(V \times E)\) makes it inefficient for large graphs compared to Dijkstra’s algorithm, especially when all edge weights are non-negative.
2. **Slower than Dijkstra**: When no negative weights are present, Dijkstra's algorithm is generally faster with a time complexity of \(O(E \log V)\).

## **When Not to Use Bellman-Ford**
- **If there are no negative weights**: If the graph has no negative weights, Bellman-Ford is generally slower than Dijkstra’s algorithm.
- **When you don't need cycle detection**: If you don't need to detect negative cycles, Dijkstra's algorithm is typically a better choice.

---

## **Summary**
- **Bellman-Ford** is an algorithm for finding the shortest paths from a single source node to all other nodes in a graph, and it works with graphs that have negative edge weights.
- It handles negative weight cycles and ensures the shortest path calculation is correct even when negative edges are present.
- It is slower than **Dijkstra's algorithm**, but useful when negative weights are involved or negative cycles need to be detected.
