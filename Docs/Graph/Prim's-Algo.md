### Problem Overview
In this problem, you are given a list of points in a 2D plane, and your goal is to connect all the points with the minimum cost using the **Manhattan Distance** (sum of absolute differences of the coordinates). This is a **Minimum Spanning Tree (MST)** problem where you need to find the minimum cost to connect all points.

### Key Concepts of Prim's Algorithm
1. **Minimum Spanning Tree (MST):** The problem at hand is an MST problem. The MST connects all vertices (points) in a graph with the minimum sum of edge weights (distances between points).
   
2. **Prim's Algorithm:** A greedy algorithm for finding the MST of a graph. It starts with an arbitrary vertex and grows the MST by repeatedly adding the smallest edge that connects a vertex in the MST to a vertex outside the MST.

   **Steps for Prim's Algorithm:**
   - Start with an arbitrary node.
   - Use a priority queue (min-heap) to store the minimum edges.
   - Always add the smallest edge to the MST, making sure not to add cycles (edges that connect nodes already in the MST).
   - Repeat until all nodes are in the MST.

### When to Apply Prim’s Algorithm
Prim’s algorithm is best suited for situations where:
1. **The graph is dense:** A dense graph has many edges (many possible connections between points), and Prim’s is more efficient than Kruskal’s algorithm here. This is because Prim’s builds the MST incrementally and does not need to sort all edges upfront like Kruskal’s does.
2. **You want to find a minimum spanning tree:** MST problems are classic candidates for Prim's algorithm.
3. **Edge weights are given (or need to be computed):** In your problem, the distance between points was computed using Manhattan distance, which can be treated as edge weights.

### Recognizing the Problem Type for MST Solutions
1. **Graph-based problems:** If the problem involves connecting points or vertices with edges and you are tasked with minimizing the total weight of the connections (e.g., distances, costs, or other metrics), it's often an MST problem.
   
2. **Dense graphs:** If there are many connections possible between the points (like in your case, where every pair of points can be connected), Prim’s algorithm is a good fit. For sparse graphs, Kruskal's might be better.

### Understanding the Code in Detail

#### 1. **Adjacency List Construction:**
   - The adjacency list `adj` stores all possible edges (connections between points) and their respective distances (Manhattan distance between each pair of points).
   - This list is populated by calculating the Manhattan distance between all pairs of points.

   ```python
   adj = {i:[] for i in range(N)}
   for i in range(N):
       x1, y1 = points[i]
       for j in range(i+1, N):
           x2, y2 = points[j]
           dist = abs(x1-x2) + abs(y1-y2)
           adj[i].append([dist, j])
           adj[j].append([dist, i])
   ```

#### 2. **Prim’s Algorithm (Main Logic):**
   - `minH` is a min-heap (priority queue) that stores the edges with the smallest weight (cost).
   - The loop continues to add edges to the MST while avoiding cycles (by using the `visited` set).
   - The process continues until all nodes are included in the MST.

   ```python
   res = 0
   visit = set()
   minH = [[0, 0]]  # Start with node 0 and 0 cost

   while len(visit) < N:
       cost, i = heapq.heappop(minH)  # Get the node with the smallest cost
       if i in visit:
           continue  # Skip if already visited
       res += cost
       visit.add(i)  # Mark the node as visited
       for neiCost, nei in adj[i]:
           if nei not in visit:
               heapq.heappush(minH, [neiCost, nei])  # Push all neighbors to the heap
   ```

### Cheatsheet for Prim's Algorithm

**1. Problem Type Identification:**
   - **Graph Problems**: Is the problem about connecting vertices (points, cities, etc.) with edges (distances, costs)? If yes, it might involve an MST.
   - **Dense Graph**: If every point is connected to every other point (like in your case where you can compute the distance between any two points), Prim's is efficient.
   - **Optimization Goal**: The problem asks to minimize the sum of edge weights (cost, distance, etc.). This is often a cue to use MST algorithms.

**2. Key Data Structures:**
   - **Adjacency List**: To represent the graph with edge weights.
   - **Min-Heap (Priority Queue)**: To always extract the edge with the smallest weight.
   - **Visited Set**: To avoid cycles in the MST.

**3. Algorithm Outline:**
   - **Initialization**: Start with an arbitrary node, and initialize a min-heap with all edges leading from that node.
   - **Iterate**: Pop the smallest edge from the heap, and add it to the MST if it connects a new node.
   - **Update**: For each new node added to the MST, push its adjacent edges to the heap.
   - **Termination**: Repeat until all nodes are included in the MST.

**4. Time Complexity:**
   - **Adjacency List Construction**: \(O(N^2)\) where \(N\) is the number of points.
   - **Prim's Algorithm**: Each operation on the min-heap takes \(O(\log N)\). For \(N\) nodes, the time complexity of Prim’s algorithm is \(O(N \log N)\).

**5. Example Problem Types:**
   - **Connecting points in a 2D grid with minimum cost (like the problem you solved)**.
   - **Network design problems**: Connecting multiple cities or computer networks with the minimum cost.
   - **Minimum-cost spanning tree**: For connecting various components in a graph efficiently.

### Summary
Use **Prim’s algorithm** when you're dealing with dense graphs where you need to find the **minimum spanning tree**. It’s a great fit when the graph has many possible edges, and you want an efficient way to connect all vertices with the smallest possible total cost.