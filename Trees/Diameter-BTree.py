"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:
Input: root = [1,2]
Output: 1
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Using a Mutable Object (list): In Python, lists are mutable objects, which means they can be modified after they are created. When you pass a list as an argument or use it within nested functions (closures), changes made to the list inside those functions are reflected in the original list.
        diameter = [0]  # Initialize the diameter with 0. Using a list allows us to modify it within nested functions.
        
        def depth(root):
            if not root:
                return -1  # Base case: if the node is None, return -1 (indicating the height of an empty tree)
            
            left = depth(root.left)   # Recursively find the depth of the left subtree
            right = depth(root.right) # Recursively find the depth of the right subtree
            
            # The diameter at this node is the sum of the left depth and right depth + 2 (since we count edges)
            diameter[0] = max(diameter[0], 2 + left + right)
            
            # Return the height of the tree rooted at this node
            return 1 + max(left, right)
        
        depth(root)  # Initial call to the helper function
        return diameter[0]  # Return the maximum diameter found