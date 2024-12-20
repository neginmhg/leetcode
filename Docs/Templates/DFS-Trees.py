"""
How to Know How Many Returns You Need?

-- 1 return statement is typically enough in most DFS problems 
    because recursion naturally follows the "last-in, first-out" 
    principle, and you can propagate results upward 
    (i.e., from child to parent).


-- Multiple return statements are needed 
    when you need to make decisions or accumulate results based on child 
    nodes or conditions. For example, in a problem where you need to check 
    if a node’s value satisfies certain conditions, or 
    if the subtree rooted at a node has a property 
    (like being balanced or a BST).

"""

class Solution:
    def inorder(self, root):
        # Base Case: If the root is None (empty node)
        if not root:
            return
        
        # Recursive DFS: First visit left child
        self.inorder(root.left)  # Recur on left child
        
        # Process the current node (after visiting left child)
        print(root.val)  # Example processing step (printing the value)
        
        # Recursive DFS: Visit right child
        self.inorder(root.right)  # Recur on right child

    def sumOfNodes(self, root):
        # Base case
        if not root:
            return 0
        
        # Recursive DFS: Sum left and right subtrees and the current node value
        left_sum = self.sumOfNodes(root.left)
        right_sum = self.sumOfNodes(root.right)
        
        # Return the sum of current node and both subtrees
        return root.val + left_sum + right_sum
    

    def isValidBST(self, root):
        # Helper function to validate the BST
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            # Base case: If the node is None, it's valid
            if not node:
                return True
            
            # If the current node's value is out of the valid range, return False
            if not (lower < node.val < upper):
                return False
            
            # Recursively validate left and right subtrees
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
        
        # Start DFS with the root and the full range
        return dfs(root)
