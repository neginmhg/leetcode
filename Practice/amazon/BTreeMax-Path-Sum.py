"""
[hard]
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Trees.TreeNode import TreeNode

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
         # Initialize the global maximum path sum with the root's value
        res= [root.val]     #global var

        def dfs(root):
            if not root:
                return 0        # Base case: if the node is None, return 0
            
             # Recursively calculate the maximum gains from left and right subtrees
            leftMax = dfs(root.left)
            rightMax =dfs(root.right)

             # If the left or right subtree has a negative gain, we ignore it by taking max with 0
            leftMax = max(leftMax,0)
            rightMax = max(rightMax, 0 )

             # Calculate the current path sum passing through the current node
            current_max_path = root.val + leftMax + rightMax
            res[0] = max(res[0], current_max_path)

            # Return the maximum gain from the current node to its parent
            return root.val+max(leftMax,rightMax)
        
        dfs(root)
        return res[0]