"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=0   #keep track of how many nodes have been visited
        cur=root
        stack=[]
        #DFS
        while cur and stack:
            "This inner while loop goes as far left down the tree as possible, pushing each node onto the stack. This ensures that nodes are processed in ascending order, as the leftmost node in a BST is the smallest."
            while cur:# add root and all lefts to stack
                stack.append(cur)
                cur=cur.left
            cur=stack.pop() #poping the smallest
            n +=1
            if n==k:
                return cur.val
            cur=cur.right

"The whole process uses an iterative in-order traversal (left, root, right) with the help of a stack, allowing it to find the kth smallest element efficiently without requiring extra space for a full list of node values."