Here's a quick blueprint to help you decide which algorithm to use based on the problem type during coding interviews:

### **Graph Problem Type & Algorithm Decision Blueprint**

---

### 1. **Shortest Path Problem**
   - **Unweighted graph**:
     - Use **BFS** (find the shortest path by traversing level by level).
   - **Weighted graph with non-negative weights**:
     - Use **Dijkstra's Algorithm** (efficient for sparse graphs).
   - **Weighted graph with negative weights**:
     - Use **Bellman-Ford** (to handle negative weights, but not for all interview questions if it’s not mentioned explicitly).

---

### 2. **Minimum Spanning Tree (MST)**
   - **Dense graph**:
     - Use **Prim’s Algorithm** (efficiency with dense graphs using a priority queue).
   - **Sparse graph**:
     - Use **Kruskal’s Algorithm** (uses Union-Find to manage edge connections).
   
---

### 3. **Cycle Detection**
   - **Directed graph**:
     - Use **DFS** with backtracking (mark nodes as visited, and use recursion stack to detect cycles).
   - **Undirected graph**:
     - Use **DFS** (mark visited nodes and detect cycles during backtracking).
     - Alternatively, use **Union-Find** to check if adding an edge forms a cycle.
   
---

### 4. **Topological Sort (Ordering Problems)**
   - **Directed Acyclic Graph (DAG)**:
     - Use **Topological Sort with BFS** (Kahn’s Algorithm).
   
---

### 5. **Connected Components**
   - **Unweighted graph** (find all connected components or explore all nodes):
     - Use **BFS** or **DFS**.
   - **Undirected graph (disjoint sets)**:
     - Use **Union-Find** to efficiently group nodes into connected components.
   
---

### 6. **Pathfinding / Exploring all Paths**
   - **Unweighted or weighted graph**:
     - Use **DFS** for deep exploration and to find all paths (backtracking may be needed).
     - **BFS** can also be used if all edges are unweighted and you need to find the shortest path in terms of number of steps.

---

### **Quick Decision Flow:**

1. **Is the graph weighted?**
   - If **yes**, use **Dijkstra's** (for non-negative weights) or **Prim’s/Kruskal’s** for MST.
   - If **no**, use **BFS** (for unweighted shortest path or level-order traversal) or **DFS** (for deep exploration).

2. **Is the graph directed?**
   - If **yes**, check for cycles using **DFS** (backtracking), and for task ordering, use **Topological Sort**.
   - If **no**, use **DFS** or **Union-Find** for detecting connected components or cycles.

3. **Does the problem involve dependencies or ordering?**
   - If **yes**, use **Topological Sort with BFS** (Kahn’s Algorithm) for a DAG.

4. **Does the problem ask for MST (minimum spanning tree)?**
   - If **yes**, use **Prim’s** (for dense graphs) or **Kruskal’s** (for sparse graphs).

5. **Does the problem involve disjoint sets or connectivity checks?**
   - Use **Union-Find** for merging sets and checking connectivity.

---

### **Quick Algorithm Summary**

| **Problem**                | **Algorithm**                           |
|----------------------------|-----------------------------------------|
| **Shortest path (unweighted)**  | BFS                                     |
| **Shortest path (weighted, non-negative)** | Dijkstra’s Algorithm                   |
| **MST (dense graph)**          | Prim’s Algorithm                        |
| **MST (sparse graph)**         | Kruskal’s Algorithm                     |
| **Cycle detection (directed)** | DFS (backtracking)                      |
| **Cycle detection (undirected)** | DFS (backtracking) or Union-Find       |
| **Topological Sort**          | Topological Sort with BFS (Kahn’s)      |
| **Connected components**      | BFS/DFS (for unweighted) or Union-Find  |
| **Disjoint set merging**     | Union-Find                              |

---

