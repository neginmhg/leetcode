"""
Given the root of a binary search tree (BST) and a target value `k`, return the `k` values in the BST that are closest to `k` in value.

**Input:**
- `root`: The root of a binary search tree (`TreeNode`).
- `k`: An integer representing the number of closest values to return.
- `target`: A floating-point number representing the target value to find the closest values to.

**Output:**
- A list of `k` integers that are closest to the `target` value.

**Example:**
# Input
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
k = 3
target = 3.714286
# Output
[4, 3, 5]

**Explanation:**
In this example, the BST is structured as follows:
```
    4
   / \
  2   5
 / \
1   3
```
The closest values to the target `3.714286` are `4`, `3`, and `5`.
"""
from typing import List
from collections import deque
from Trees import TreeNode
class Solution:
    def closestKValues(root: TreeNode, k: int, target: float) -> List[int]:
        #in order traversal and a queue
        q=deque    #store k closest to target
        def inOrderT(node):
            if not node:
                return
            inOrderT(node.left)
            
            if(len(q)<k):
                q.append(node.val)
            else:
                if(abs(node.val - target)< abs(q[0]-target)):
                    q.popleft()
                    q.append(node.val)
                else: 
                    #if the val is bigger then that means the rest of node vals will be bigger too, so let's return and get out
                    return
            
            inOrderT(node.right)
        inOrderT(root)
        return list(q)
#In the best case, it only needs to visit a portion of the tree, potentially reducing the time complexity to O(log n + k). In the worst case, it still has O(n) time complexity, but the early stopping allows for significant pruning in many real-world cases.

"""The total space complexity of the solution consists of two main components: space for the result storage (deque) and space for the recursion stack (or iterative traversal stack) during the in-order traversal.

Components of Space Complexity:
- Deque (or Result Storage) Space:
We maintain a deque that stores at most k elements (the k closest values).
This results in a space complexity of O(k) for storing the k closest values.

- Recursion Stack Space (or Iterative Stack):
The in-order traversal of the tree is performed recursively. The space required for the recursion stack is proportional to the height of the tree.
In the worst case, for a highly skewed tree (where the tree behaves like a linked list), the recursion depth will be equal to the number of nodes, which results in O(n) space.
In the best case, for a balanced binary search tree (BST), the height of the tree is O(log n), where n is the number of nodes.
"""