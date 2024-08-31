### Depth-First Search (DFS)

#### Principles of DFS

DFS explores as far as possible along each branch before backtracking. In the context of trees, this means visiting nodes deeper in the tree before visiting nodes that are shallower. For graphs, DFS can be implemented using either recursion (the call stack) or an explicit stack data structure.

#### Types of DFS Traversals for Trees

1. **Pre-order Traversal**: Visit the root node, then the left subtree, and finally the right subtree.
2. **In-order Traversal**: Visit the left subtree, the root node, and finally the right subtree.
3. **Post-order Traversal**: Visit the left subtree, the right subtree, and finally the root node.

#### DFS Implementation for Trees

Let's start with a TreeNode class and then implement the three types of DFS traversals:

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Pre-order Traversal
def preorder_traversal(root):
    if root is None:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

# In-order Traversal
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

# Post-order Traversal
def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]
```

#### DFS Implementation for Graphs

Graphs can contain cycles, so we need to keep track of visited nodes to avoid infinite loops.

```python
def dfs_graph(node, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return
    visited.add(node)
    # Process the node (e.g., print it)
    print(node)
    for neighbor in node.neighbors:
        dfs_graph(neighbor, visited)
```

### Breadth-First Search (BFS)

#### Principles of BFS

BFS explores all the nodes at the present depth level before moving on to nodes at the next depth level. It is typically implemented using a queue.

#### BFS Implementation for Trees

```python
from collections import deque

def bfs_traversal(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
```

#### BFS Implementation for Graphs

For graphs, BFS also requires tracking visited nodes to prevent revisiting.

```python
from collections import deque

def bfs_graph(start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        # Process the node (e.g., print it)
        print(node)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
```

### Applications of DFS and BFS

#### DFS Applications

1. **Topological Sorting**: Useful for ordering tasks with dependencies.
2. **Solving Mazes and Puzzles**: Finding paths from start to goal.
3. **Connected Components**: Identifying all components in a graph.
4. **Tree Traversals**: In-order, pre-order, and post-order traversals are all DFS.

#### BFS Applications

1. **Shortest Path in Unweighted Graph**: BFS finds the shortest path between two nodes.
2. **Level Order Traversal**: Printing nodes level by level in a tree.
3. **Finding Connected Components**: In unweighted graphs.
4. **Breadth of Search**: Useful when the solution is likely to be found close to the starting node.

### Choosing Between DFS and BFS

- Use **DFS** when you want to explore as deep as possible before backtracking. This is useful when you need to visit all nodes or paths, such as in puzzles or tree traversals.
- Use **BFS** when you need the shortest path in an unweighted graph or when you want to explore nodes level by level, such as in level order traversal of a tree.

### Examples and Problems

Here are some common problems where DFS and BFS are applicable:

1. **Binary Tree Level Order Traversal** (BFS):

   ```python
   from collections import deque

   def level_order_traversal(root):
       if not root:
           return []
       result, queue = [], deque([root])
       while queue:
           level = []
           for _ in range(len(queue)):
               node = queue.popleft()
               if node:
                   level.append(node.value)
                   queue.append(node.left)
                   queue.append(node.right)
           if level:
               result.append(level)
       return result
   ```

2. **Number of Islands** (DFS/BFS):

   ```python
   def num_islands(grid):
       if not grid:
           return 0

       def dfs(grid, i, j):
           if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
               return
           grid[i][j] = '0'  # Mark as visited
           dfs(grid, i + 1, j)
           dfs(grid, i - 1, j)
           dfs(grid, i, j + 1)
           dfs(grid, i, j - 1)

       count = 0
       for i in range(len(grid)):
           for j in range(len(grid[0])):
               if grid[i][j] == '1':
                   count += 1
                   dfs(grid, i, j)
       return count
   ```

3. **Clone Graph** (BFS):

   ```python
   from collections import deque

   class Node:
       def __init__(self, val=0, neighbors=None):
           self.val = val
           self.neighbors = neighbors if neighbors is not None else []

   def clone_graph(node):
       if not node:
           return None
       clones = {node: Node(node.val)}
       queue = deque([node])
       while queue:
           current = queue.popleft()
           for neighbor in current.neighbors:
               if neighbor not in clones:
                   clones[neighbor] = Node(neighbor.val)
                   queue.append(neighbor)
               clones[current].neighbors.append(clones[neighbor])
       return clones[node]
   ```
