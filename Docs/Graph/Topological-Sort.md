Topological sorting is a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge \( (u, v) \) from vertex \( u \) to vertex \( v \), \( u \) comes before \( v \) in the ordering. This means that each vertex appears before all vertices to which it has outgoing edges.
https://www.youtube.com/watch?v=cIBFEhD77b4

### Key Points of Topological Sort:

1. **Applies to DAGs**: Topological sorting is only defined for Directed Acyclic Graphs. A DAG is a graph with directed edges and no cycles.

2. **Unique Order**: A graph can have multiple topological sorts. However, for a given DAG, any valid topological sort is a valid linearization of the graph.

3. **Use Cases**:
   - **Task Scheduling**: Determine the order in which tasks should be executed given dependencies.
   - **Course Prerequisites**: Determine the order of courses to take based on prerequisite relationships.
   - **Build Systems**: Determine the order in which to build components based on dependencies.

### Algorithms for Topological Sort:

1. **Kahn's Algorithm (BFS-Based)**
2. **Depth-First Search (DFS)-Based Algorithm**

#### **1. Kahn's Algorithm (BFS-Based)**

This algorithm uses the concept of in-degree (number of incoming edges) to perform topological sorting.

**Steps:**

1. **Compute In-Degree**: Calculate the in-degree of each vertex. The in-degree of a vertex is the number of edges coming into that vertex.

2. **Initialize Queue**: Initialize a queue and enqueue all vertices with in-degree 0 (i.e., vertices with no incoming edges).

3. **Process Queue**:

   - While the queue is not empty:
     - Dequeue a vertex from the queue.
     - Append this vertex to the topological sort order.
     - For each outgoing edge from this vertex to another vertex:
       - Decrease the in-degree of the adjacent vertex by 1.
       - If the in-degree of the adjacent vertex becomes 0, enqueue it.

4. **Check for Cycles**: If the topological sort order contains all the vertices, then the graph is a DAG. Otherwise, if there are vertices left unprocessed, the graph contains cycles.

**Example Code:**

```python
from collections import deque, defaultdict

def topological_sort_kahn(graph):
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    top_order = []

    while queue:
        node = queue.popleft()
        top_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return top_order
```

#### **2. DFS-Based Algorithm**

This algorithm uses Depth-First Search (DFS) to achieve topological sorting.

**Steps:**

1. **Initialize**: Create a stack to store the topological order. Also, maintain a set to keep track of visited nodes.

2. **DFS Traversal**:

   - For each unvisited vertex, perform DFS.
   - During the DFS traversal, once all the adjacent vertices are processed, push the current vertex to the stack.

3. **Reverse the Stack**: The topological sort order is obtained by reversing the stack.

**Example Code:**

```python
def topological_sort_dfs(graph):
    stack = []
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]
```

### Summary

- **Topological Sort** is a way to order vertices in a DAG such that each vertex appears before any vertices to which it has outgoing edges.
- It is used for various applications like task scheduling, course ordering, and build systems.
- The two primary algorithms for topological sorting are Kahn's Algorithm (BFS-based) and the DFS-based Algorithm.

# DFS vs. Kahn's Algorithm (Queue-Based):

| **DFS (Stack)**                                                          | **Kahn’s Algorithm (Queue)**                                           |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Uses **stack** and adds nodes to the stack in post-order                 | Uses a **queue** to process nodes with in-degree 0 first               |
| Requires **reversing** the stack at the end to get the topological order | No need to reverse; nodes are added to the result in the correct order |
| Easier to implement recursively                                          | More complex, but avoids reversing                                     |
| Can handle **backtracking** scenarios naturally                          | More suited for real-time task scheduling problems                     |

### Summary:

- **DFS-based topological sort** uses a **stack**, and since nodes are processed in a post-order fashion (dependencies come last), we need to reverse the stack to get the correct topological order.
- **Kahn’s Algorithm** uses a **queue** to process nodes with zero dependencies first, so the order is built directly without needing to reverse it.

# When use **DFS-based topological sort** and **Kahn’s Algorithm**:

| **DFS-Based Topological Sort**                                                               | **Kahn’s Algorithm (Queue-Based)**                                                          |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Best for **recursion-based problems** or problems that benefit from **post-order traversal** | Best for **iterative problems** or when you need **real-time task processing**              |
| Useful for **cycle detection** in problems where backtracking is required                    | Effective for **cycle detection** in task scheduling scenarios                              |
| **Handles strongly connected components** in problems like SCC detection                     | Useful when **processing dependencies in layers** (BFS-like)                                |
| Requires **reversing** the stack to get topological order                                    | **No need to reverse**; directly generates topological order                                |
| Example: Course scheduling, file compilation, dependency management                          | Example: Parallel job scheduling, real-time task processing, level-by-level problem solving |
