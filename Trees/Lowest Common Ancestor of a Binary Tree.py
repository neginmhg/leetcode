"""
THIS IS FOR BINARY TREE, NOT BST.

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
"The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).


input:
root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
output:
3
The LCA of nodes 5 and 1 is 3.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: If the current node is None, or it's one of p or q, return it.
        if not root or root == p or root == q:
            return root

        # Recursively find LCA in the left and right subtrees.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return non-null, this is the LCA.
        if left and right:
            return root

        # Otherwise, return the non-null result.
        return left if left else right
