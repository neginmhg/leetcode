"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
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
import collections
from typing import List, Optional
from Trees.TreeNode import TreeNode

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []       
        #need a queue
        q=collections.deque([root])
        #need result
        result=[]
        while q:
            rightMostNode=None
            #loop through each level and pop q
            for _ in range(len(q)):
                node=q.popleft()
                if node:
                    rightMostNode=node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if rightMostNode is not None:
                result.append(rightMostNode)
        return result