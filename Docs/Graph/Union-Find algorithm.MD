The Union-Find algorithm, also known as Disjoint Set Union (DSU), is a data structure used to efficiently handle and query the union and find operations on disjoint sets. It's particularly useful for problems involving connectivity and component analysis in graphs. Here's a detailed explanation:
<br>
https://www.youtube.com/watch?v=ayW5B2W9hfo

### **Key Concepts**

1. **Disjoint Sets**:

   - A disjoint set is a collection of non-overlapping sets. Each element belongs to exactly one set.
   - Union-Find manages multiple sets, allowing operations to merge sets and determine which set an element belongs to.

2. **Operations**:
   - **Find**: Determine the root or representative of the set that an element belongs to.
   - **Union**: Merge two sets into a single set.

### **Union-Find Data Structure**

The Union-Find data structure typically uses two key arrays:

1. **Parent Array**:

   - Keeps track of the parent of each element. If `parent[i] == i`, then `i` is a root (i.e., it is the representative of its set).

2. **Rank/Size Array** (optional):
   - Keeps track of the rank (or size) of each set. This helps in optimizing the union operation by attaching the smaller tree under the root of the larger tree.

### **Algorithm Details**

#### 1. **Find Operation**

- **Purpose**: To find the representative (root) of the set containing a specific element.
- **Path Compression**: Optimizes the `find` operation by making nodes point directly to the root, thus flattening the structure and speeding up future operations.

**Implementation**:

```python
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])  # Path compression
    return parent[node]
```

- If `parent[node]` is not the node itself, recursively find the root and make the node point directly to the root.

#### 2. **Union Operation**

- **Purpose**: To merge two sets into a single set.
- **Union by Rank/Size**: Optimizes the `union` operation by attaching the smaller tree under the root of the larger tree, keeping the tree as flat as possible.

**Implementation**:

```python
def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        parent[root1] = root2  # Union the components
        return True
    return False
```

- Find the roots of both nodes. If they are different, attach one tree to the other and update the root.

### **Efficiency**

- **Time Complexity**:
  - Both `find` and `union` operations are nearly constant time due to path compression and union by rank. The amortized time complexity for each operation is \(O(\alpha(n))\), where \(\alpha\) is the Inverse Ackermann function, which grows very slowly.
- **Space Complexity**:
  - The space complexity is \(O(n)\) for storing the parent (and optionally rank/size) arrays.

### **Applications**

- **Graph Connectivity**: Determine if two nodes are in the same connected component.
- **Kruskal's Algorithm**: Used to find the Minimum Spanning Tree (MST) of a graph.
- **Network Connectivity**: Identify clusters or connected components in a network.

### **Example**

Consider a graph with 5 nodes and the following edges: `[[0, 1], [1, 2], [3, 4]]`. The goal is to find the number of connected components.

1. Initialize each node as its own parent.
2. Perform union operations for each edge:
   - Union(0, 1)
   - Union(1, 2)
   - Union(3, 4)
3. After processing all edges, find the number of unique roots to determine the number of connected components.

The Union-Find algorithm is efficient and effective for handling dynamic connectivity problems, making it a powerful tool in graph algorithms and network analysis.
