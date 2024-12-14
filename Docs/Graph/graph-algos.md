### **Key Graph Algorithms to Know**

#### **1. Breadth-First Search (BFS)** 
- **Use Cases**: Shortest path in an unweighted graph, level-order traversal, finding connected components.
- **Recognizing BFS Problems**:
  - "Find the shortest path" in unweighted graphs.
  - "Explore all neighbors first" or "traverse level by level."
  - Examples: 
    - Word Ladder
    - Number of Islands
    - Minimum Knight Moves

#### **2. Depth-First Search (DFS)**
- **Use Cases**: Traversing all nodes, detecting cycles, pathfinding, backtracking problems.
- **Recognizing DFS Problems**:
  - "Find all paths" or "exhaustively search."
  - Problems involving recursion or backtracking.
  - Examples:
    - Pacific Atlantic Water Flow
    - Clone Graph
    - Path Sum

#### **3. Dijkstra’s Algorithm**
- **Use Cases**: Single-source shortest path in weighted graphs (non-negative weights).
- **Recognizing Dijkstra Problems**:
  - "Find the shortest path" in weighted graphs.
  - Use priority queues or heaps.
  - Examples:
    - Network Delay Time
    - Cheapest Flights Within K Stops

#### **4. Bellman-Ford Algorithm**
- **Use Cases**: Single-source shortest path, handles negative weights.
- **Recognizing Bellman-Ford Problems**:
  - Problems with negative edge weights.
  - Examples:
    - Negative Weight Cycle Detection
    - Arbitrage Detection in Currency Exchange

#### **5. Floyd-Warshall Algorithm**
- **Use Cases**: All-pairs shortest path, dynamic programming on graphs.
- **Recognizing Floyd-Warshall Problems**:
  - Problems requiring shortest paths between all pairs of nodes.
  - Examples:
    - Shortest Distance Between All Nodes
    - Transitive Closure

#### **6. Union-Find (Disjoint Set Union - DSU)**
- **Use Cases**: Connected components, cycle detection, Kruskal’s MST.
- **Recognizing Union-Find Problems**:
  - "Check if nodes are in the same group" or "merge groups."
  - Examples:
    - Redundant Connection
    - Number of Connected Components in an Undirected Graph

#### **7. Kruskal’s Algorithm**
- **Use Cases**: Minimum Spanning Tree (MST).
- **Recognizing Kruskal Problems**:
  - Problems asking for "minimum cost to connect all nodes."
  - Examples:
    - Minimum Spanning Tree
    - Optimize Water Distribution in a Village

#### **8. Prim’s Algorithm**
- **Use Cases**: Minimum Spanning Tree (alternative to Kruskal’s).
- **Recognizing Prim Problems**:
  - Problems emphasizing greedily adding edges.
  - Examples:
    - Connecting Cities With Minimum Cost
    - Prim’s MST Problems

#### **9. Topological Sorting**
- **Use Cases**: Ordering tasks with dependencies, detecting cycles in Directed Acyclic Graphs (DAGs).
- **Recognizing Topological Sort Problems**:
  - "Ordering tasks based on dependencies."
  - Examples:
    - Course Schedule
    - Alien Dictionary

#### **10. Tarjan’s Algorithm**
- **Use Cases**: Strongly Connected Components (SCC), articulation points (critical nodes).
- **Recognizing Tarjan Problems**:
  - "Find all critical connections or nodes."
  - Examples:
    - Critical Connections in a Network
    - Strongly Connected Components

#### **11. A* Search**
- **Use Cases**: Pathfinding with heuristics.
- **Recognizing A* Problems**:
  - Problems requiring shortest path with a heuristic.
  - Examples:
    - Pathfinding in Grids
    - Complex Shortest Path Problems

#### **12. Dynamic Programming on Graphs**
- **Use Cases**: Longest path in a DAG, count paths.
- **Recognizing DP Problems**:
  - Problems involving states and transitions in DAGs.
  - Examples:
    - Longest Path in a DAG
    - Counting Paths in Graphs

---

### **How to Identify Which Algorithm to Use**

1. **Understand the Graph Representation**:
   - **Matrix/Adjacency List**: BFS or DFS is usually the go-to for exploration.
   - **Weighted Graph**: Think Dijkstra, Bellman-Ford, or Floyd-Warshall.
   - **Unweighted Graph**: BFS works best for shortest paths.

2. **Problem Requirements**:
   - **Shortest Path**: Unweighted (BFS); Weighted (Dijkstra, Bellman-Ford, or A*).
   - **Connected Components**: Union-Find or DFS/BFS.
   - **Cycles**: Use DFS, Union-Find, or Topological Sorting.
   - **Dependencies**: Topological Sorting.
   - **Critical Connections/Nodes**: Tarjan’s Algorithm.

3. **Graph Constraints**:
   - **Small Graphs (<= 100)**: Consider Floyd-Warshall or DFS variations.
   - **Large Graphs (> 10⁴)**: Use BFS, Dijkstra, or Union-Find for efficiency.

4. **Clues from the Problem**:
   - **"Level-by-level traversal"**: BFS.
   - **"All paths" or "Exhaustive Search"**: DFS or backtracking.
   - **"Dependencies/order"**: Topological Sort.
   - **"Minimum cost to connect nodes"**: Kruskal’s or Prim’s.

---

### **Tips for LeetCode Practice**
1. **Master BFS/DFS First**: They form the basis for many other algorithms.
2. **Practice Recognizing Patterns**: Categorize problems as traversal, pathfinding, connectivity, etc.
3. **Memorize Key Templates**: Use BFS/DFS, Union-Find, and Dijkstra templates to speed up problem-solving.
4. **Look at Constraints**: Small constraints often allow brute force (DFS), while large graphs require optimized algorithms.
5. **Solve Problems Iteratively**: Start with simple traversal problems and progress to weighted graphs and DP-based approaches.

---

### **Recommended Practice Problems on LeetCode**
1. **Easy**:
   - Number of Islands
   - Flood Fill
   - Path Sum
2. **Medium**:
   - Word Ladder
   - Course Schedule
   - Network Delay Time
3. **Hard**:
   - Minimum Cost to Connect All Points
   - Critical Connections in a Network
   - Longest Increasing Path in a Matrix
