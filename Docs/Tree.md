### 1. **Basic Concepts of Trees**

- **Tree**: A hierarchical data structure with a root node and zero or more child nodes, where each child node is a root of a subtree.
- **Binary Tree**: Each node has at most two children (left and right).
- **Binary Search Tree (BST)**: A binary tree where the left child’s value is less than the parent’s value, and the right child’s value is greater than the parent’s value.
- **Balanced Tree**: A tree where the height difference between left and right subtrees of any node is not more than one.
- **Height of a Tree**: The number of edges on the longest path from the root to a leaf.

### 2. **Common Tree Traversal Methods**

- **Inorder Traversal** (Left, Root, Right): Useful for BSTs to get sorted order.
- **Preorder Traversal** (Root, Left, Right): Useful for copying the tree or prefix expression.
- **Postorder Traversal** (Left, Right, Root): Useful for deleting the tree or postfix expression.
- **Level Order Traversal**: Uses a queue to visit nodes level by level.

### 3. **Tree Node Definition**

Here’s a basic `TreeNode` class definition in Python:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### 4. **Common Tree Traversal Snippets**

**Inorder Traversal (Recursive)**:

```python
def inorderTraversal(root):
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    return inorder(root)
```

**Inorder Traversal (Iterative)**:

```python
def inorderTraversal(root):
    stack, result = [], []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result
```

**Preorder Traversal (Recursive)**:

```python
def preorderTraversal(root):
    def preorder(node):
        return [node.val] + preorder(node.left) + preorder(node.right) if node else []
    return preorder(root)
```

**Preorder Traversal (Iterative)**:

```python
def preorderTraversal(root):
    if not root:
        return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
```

**Postorder Traversal (Recursive)**:

```python
def postorderTraversal(root):
    def postorder(node):
        return postorder(node.left) + postorder(node.right) + [node.val] if node else []
    return postorder(root)
```

**Postorder Traversal (Iterative)**:

```python
def postorderTraversal(root):
    if not root:
        return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]
```

**Level Order Traversal**:

```python
from collections import deque

def levelOrder(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

### 5. **Common Tree Problems**

- **Maximum Depth of Binary Tree**: Find the maximum depth of the tree.
- **Symmetric Tree**: Check if a tree is symmetric around its center.
- **Binary Tree Level Order Traversal**: Return the level order traversal of the tree nodes.
- **Validate Binary Search Tree**: Check if a tree is a valid BST.
- **Lowest Common Ancestor**: Find the lowest common ancestor of two nodes in a BST.
- **Path Sum**: Check if there is a path in the tree with a sum equal to a given value.
<hr><br><br>

# Tree Problems & The tricks:

Certainly! Here’s a list of tree problems with tips or tricks to help you remember how to approach them:

### Basic Tree Problems

1. **Maximum Depth of Binary Tree** (Easy)

   - **Trick**: Use a recursive approach to traverse the tree. At each node, return `1 + max(depth of left subtree, depth of right subtree)`. You can also use a BFS approach to count levels.

2. **Min Depth of Binary Tree** (Easy)

   - **Trick**: Similar to maximum depth but stop as soon as you reach a leaf node. Use a recursive approach that returns `1 + min(depth of left subtree, depth of right subtree)`.

3. **Balanced Binary Tree** (Easy)

   - **Trick**: Check the height of the left and right subtrees for every node. If the height difference is more than 1 for any node, it’s not balanced. Use a helper function to compute both height and balance status simultaneously.

4. **Same Tree** (Easy)

   - **Trick**: Compare the root nodes and recursively check if both left and right subtrees are the same. Return `True` if both trees are identical.

5. **Symmetric Tree** (Easy)
   - **Trick**: Use a recursive approach to check if the left subtree is a mirror of the right subtree. Compare nodes in a mirrored fashion.

### Tree Traversal

1. **Binary Tree Inorder Traversal** (Easy)

   - **Trick**: Use the left-root-right order. For iterative traversal, use a stack to manage nodes and process them in the correct order.

2. **Binary Tree Preorder Traversal** (Easy)

   - **Trick**: Use the root-left-right order. For iterative traversal, use a stack and process the root first, then push the right and left children onto the stack.

3. **Binary Tree Postorder Traversal** (Easy)

   - **Trick**: Use the left-right-root order. For iterative traversal, use two stacks or a modified approach with a single stack to process nodes in the correct order.

4. **Level Order Traversal** (Medium)

   - **Trick**: Use a queue (BFS). Enqueue the root and then iteratively dequeue nodes, enqueue their children, and collect node values by level.

5. **Zigzag Level Order Traversal** (Medium)
   - **Trick**: Use a deque and a flag to switch between left-to-right and right-to-left order for each level. Adjust the direction at each level.

### Tree Construction and Serialization

1. **Construct Binary Tree from Preorder and Inorder Traversal** (Medium)

   - **Trick**: Use the first element of the preorder list as the root. Find this root in the inorder list to divide the tree into left and right subtrees. Recursively apply this process.

2. **Construct Binary Tree from Inorder and Postorder Traversal** (Medium)

   - **Trick**: Use the last element of the postorder list as the root. Find this root in the inorder list to divide the tree into left and right subtrees. Recursively apply this process.

3. **Serialize and Deserialize Binary Tree** (Hard)
   - **Trick**: For serialization, perform a BFS or DFS and convert the tree into a string with delimiters. For deserialization, use a queue or index-based approach to reconstruct the tree from the string.

### Tree Path and Sum Problems

1. **Path Sum** (Easy)

   - **Trick**: Use a recursive approach to check if there’s a path with a given sum. Subtract the node’s value from the target sum and check the left and right subtrees.

2. **Path Sum II** (Medium)

   - **Trick**: Similar to Path Sum, but collect all paths instead of just checking. Use a recursive approach to build paths and add valid paths to the result list.

3. **Maximum Path Sum** (Hard)

   - **Trick**: Use a helper function to compute the maximum path sum including the current node and update the global maximum. Return the maximum gain from the current node to its parent.

4. **Binary Tree Maximum Path Sum** (Hard)
   - **Trick**: Compute the maximum path sum through each node considering both single-path and split-path scenarios. Use a helper function to calculate the maximum path sum and update the global maximum.

### Binary Search Tree (BST) Specific Problems

1. **Validate Binary Search Tree** (Medium)

   - **Trick**: Use a recursive approach with a range for valid values. Ensure that the left subtree values are within the valid range for a BST and similarly for the right subtree.

2. **Invert Binary Tree** (Easy)

   - **Trick**: Swap the left and right children of each node recursively. It’s a straightforward application of swapping nodes.

3. **Recover Binary Search Tree** (Hard)
   - **Trick**: Find the two swapped nodes by performing an in-order traversal. Use the properties of in-order traversal to identify nodes that are out of order.

### Tree Manipulation

1. **Delete Node in a BST** (Medium)

   - **Trick**: Handle three cases for the node to be deleted: no children, one child, or two children. For two children, replace the node with its in-order successor or predecessor.

2. **Lowest Common Ancestor of a Binary Search Tree** (Easy)

   - **Trick**: Use the properties of BST to find the LCA. If both nodes are smaller than the current node, move to the left child. If both are larger, move to the right child.

3. **Lowest Common Ancestor of a Binary Tree** (Medium)
   - **Trick**: Use a recursive approach to find the LCA. Return the node if it matches one of the targets, or if one target is found in the left subtree and the other in the right subtree.

### Additional Complex Problems

1. **Kth Smallest Element in a BST** (Medium)

   - **Trick**: Perform an in-order traversal and keep count of nodes visited. The kth visited node is the answer. Alternatively, use a min-heap or iterative approach.

2. **Binary Tree Cameras** (Hard)

   - **Trick**: Use a post-order traversal to place cameras. A node requires a camera if neither of its children has a camera.

3. **Count Complete Tree Nodes** (Medium)
   - **Trick**: Use a binary search approach to count nodes efficiently. For a complete tree, use the properties of full levels and last level nodes to count nodes quickly.

These tricks and formulas should help in quickly recalling the strategies and approaches for various tree problems.
