"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

from Trees.TreeNode import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursive DFS
        if not root:
            return 0
        return 1 +max(self.maxDepth(root.left),self.maxDepth(root.right))     
    
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        #BFS and queue
        if not root:
            return 0
        level=0
        q =deque([root])
        while(q):
            for i in range(len(q)):
                node= q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level +=1
        return level
        """Why This Works
        Breadth-First Search: BFS is ideal for this problem because it processes all nodes level by level. By counting the number of levels, we directly obtain the depth of the tree.
        Queue Usage: The queue ensures that nodes are processed in the correct order (level by level). Each level is fully processed before moving to the next level.
        Level Counter: The level variable increments after processing all nodes at the current level, accurately counting the depth of the tree."""

def maxDepth3(self, root: Optional[TreeNode]) -> int:
    # Initialize a stack with a tuple containing the root node and its depth (1)
    stack = [[root, 1]]
    # Initialize the result variable to keep track of the maximum depth found
    res = 0
    
    # Iterate while there are elements in the stack
    while stack:
        # Pop a node and its depth from the stack
        node, depth = stack.pop()
        
        # If the node is not None, update the maximum depth and push its children to the stack
        if node:
            # Update the result with the maximum depth found so far
            res = max(res, depth)
            # Push the left child and its depth to the stack
            stack.append([node.left, depth + 1])
            # Push the right child and its depth to the stack
            stack.append([node.right, depth + 1])
    
    # Return the maximum depth found
    return res