"""
Given a binary tree, collect a tree's nodes as if you were doing this: 
- Collect all the leaf nodes.
- Remove all the leaf nodes.
- Repeat until the tree is empty.

You need to return the list of all the nodes collected in a step-by-step manner.

### Example 1:

**Input:**
```
        1
       / \
      2   3
     / \
    4   5
```

**Output:**
```
[[4, 5, 3], [2], [1]]
```

**Explanation:**
- In the first step, collect all the leaves: `[4, 5, 3]`.
- In the second step, after removing the leaves, the tree becomes:
  ```
      1
     / 
    2  
  ```
  Now, the leaf is `[2]`.
- In the third step, after removing leaf `2`, the tree becomes:
  ```
  1
  ```
  The leaf is `[1]`.

Thus, the final result is `[[4, 5, 3], [2], [1]]`.

### Constraints:
- The number of nodes in the tree is in the range `[1, 1000]`.
- `-1000 <= Node.val <= 1000`.

### Notes:
- The problem essentially involves collecting leaf nodes at each level and reducing the tree size level by level.

"""
from Trees import TreeNode
from typing import List
class Solution:
    def findLeaves(root: TreeNode) -> List[List[int]]:
    # your code here
    #post order dfs
        res=[]
        def getHeight(node):
            if not node:
                return -1
            curHeight= max(getHeight(node.left), getHeight(node.right)) +1
            # Ensure the result list has enough space for the current height
            if curHeight == len(res):
                res.append([])
            
            # Add the current node's value to its corresponding height level
            res[curHeight].append(node.val)
            
            return curHeight
        
        getHeight(root)
        return res