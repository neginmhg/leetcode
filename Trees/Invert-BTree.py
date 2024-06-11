"""
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #DFS recursevly

        #If the current node (root) is None, it returns None. This stops the recursion when it reaches a leaf node's childre
        if not root:
            return None

        #swap the children
        tmp = root.left
        root.left=root.right
        root.right=tmp

        #call the left subtree
        self.invertTree(root.left)
        #call the right subtree
        self.invertTree(root.right)
        return root
"""Why is this DFS?
    Depth-First Search (DFS) is a method for exploring a tree or graph where you start at the root and explore as far as possible along each branch before backtracking. There are three main types of DFS traversal: pre-order, in-order, and post-order. This specific implementation uses pre-order traversal (root, left, right) for the following reasons:

    Visit Root First: The function first processes the current node (swapping its children).
    Recursively Visit Left Subtree: It then recursively inverts the left subtree by calling self.invertTree(root.left).
    Recursively Visit Right Subtree: It finally recursively inverts the right subtree by calling self.invertTree(root.right)."""