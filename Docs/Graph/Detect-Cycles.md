# **DFS** + **BFS** template for cycle detection. 
## DFS --> visit state array
## BFS --> Topological sort

### **DFS Template with Visit State Array**
```python
def detect_cycle_dfs(graph, numNodes):
    """
    Detects a cycle in a directed graph using DFS with a Visit State Array.
    :param graph: Adjacency list representing the graph {node: [neighbors]}.
    :param numNodes: Total number of nodes in the graph.
    :return: True if there is a cycle, False otherwise.
    """
    # 0 = unvisited, 1 = visiting, 2 = visited
    visitState = [0] * numNodes

    def dfs(node):
        if visitState[node] == 1:  # Cycle detected
            return True
        if visitState[node] == 2:  # Already processed
            return False

        # Mark node as visiting
        visitState[node] = 1
        for neighbor in graph[node]:
            if dfs(neighbor):  # If any neighbor detects a cycle
                return True
        
        # Mark node as visited
        visitState[node] = 2
        return False

    # Check all nodes for cycles
    for node in range(numNodes):
        if visitState[node] == 0:  # Start DFS if the node is unvisited
            if dfs(node):
                return True
    
    return False
```

---

### **BFS Template using Topological Sort**
```python
from collections import deque

def detect_cycle_bfs(graph, numNodes):
    """
    Detects a cycle in a directed graph using BFS (Kahn's Algorithm for Topological Sort).
    :param graph: Adjacency list representing the graph {node: [neighbors]}.
    :param numNodes: Total number of nodes in the graph.
    :return: True if there is a cycle, False otherwise.
    """
    # Calculate in-degrees for all nodes
    inDegree = [0] * numNodes
    for node in graph:
        for neighbor in graph[node]:
            inDegree[neighbor] += 1

    # Collect all nodes with 0 in-degree
    queue = deque([node for node in range(numNodes) if inDegree[node] == 0])
    visitedCount = 0

    while queue:
        current = queue.popleft()
        visitedCount += 1

        # Reduce in-degree of neighbors
        for neighbor in graph[current]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:  # Add to queue if in-degree becomes 0
                queue.append(neighbor)

    # If visited nodes != total nodes, there is a cycle
    return visitedCount != numNodes
```

---

### **When to Use Which Template**
1. **DFS Template**:
   - Works for **directed graphs**.
   - Use it when you need a recursive/explicit approach to detect cycles.
   - Use this for problems like checking dependencies or preconditions (e.g., course schedule problems).

2. **BFS Template**:
   - Works for **directed graphs** using **in-degree tracking** (topological sort).
   - Use it for problems involving order, like scheduling tasks or courses.
   - Efficient for detecting cycles in large, sparse graphs.

---

### Example Input Format
For both templates, the `graph` should be represented as an adjacency list:
```python
graph = {
    0: [1],
    1: [2],
    2: [0],  # Cycle here
    3: [4],
    4: []
}
numNodes = 5
```

---

You can now plug in any graph into these templates to detect cycles using DFS or BFS!