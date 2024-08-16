### **1. Depth-First Search (DFS)**

- **Use When**:

  - You need to **explore all possible paths** or nodes in a graph or tree.
  - The problem involves **finding connected components**, **cycles**, or **paths** in graphs or trees.
  - You are dealing with **recursion or traversal** where exploring one branch deeply before backtracking is beneficial.

- **Examples**:
  - **Tree Traversal**: In-order, pre-order, and post-order traversals of a tree.
  - **Finding Connected Components**: In an undirected graph, to find all nodes connected to a starting node.
  - **Path Finding**: Finding paths between nodes or exploring all possible paths.
  - **Cycle Detection**: Detecting cycles in a graph.
  - **Solving Puzzles**: Problems like finding all solutions in a maze or solving Sudoku.

### **2. Breadth-First Search (BFS)**

- **Use When**:

  - You need to find the **shortest path** in an unweighted graph or grid.
  - The problem involves **level-order traversal** of a tree or graph.
  - You need to explore nodes level by level or **find the shortest path** in terms of number of edges or steps.

- **Examples**:
  - **Shortest Path**: Finding the shortest path in an unweighted grid or graph (e.g., shortest path in a maze).
  - **Level Order Traversal**: Traversing a tree level by level.
  - **Minimum Steps**: Problems where you need to find the minimum number of steps to reach a target (e.g., shortest path in a maze with obstacles).
  - **Finding All Nodes at a Certain Depth**: In a tree or graph.

### **3. Backtracking**

- **Use When**:

  - You need to **explore all potential solutions** to find one that satisfies certain constraints.
  - The problem involves **combinatorial search**, such as generating permutations, combinations, or solving constraint satisfaction problems.
  - You need to **incrementally build solutions** and **discard** those that do not meet the constraints.

- **Examples**:
  - **Generating Permutations/Combinations**: Problems involving generating all permutations or combinations of a set.
  - **Constraint Satisfaction**: Solving puzzles like N-Queens or Sudoku, where you need to place items while satisfying constraints.
  - **Pathfinding in Constraint-Based Puzzles**: Finding paths in mazes or other constraint-based puzzles where partial solutions need to be explored.
  - **Subset Sum**: Finding subsets of a set that sum to a specific target value.

### Summary:

- **DFS**: Use for deep exploration of nodes or paths in graphs/trees, connected components, cycle detection, or recursive problem-solving.
- **BFS**: Use for shortest path problems in unweighted graphs, level-order traversal, or problems requiring exploration by levels.
- **Backtracking**: Use for problems requiring exhaustive search with constraints, such as generating permutations, solving puzzles, or finding valid solutions incrementally.
