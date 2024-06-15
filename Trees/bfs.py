import collections
from typing import List

# Define the TreeNode class (assuming it's not pre-defined)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def insert(root, val):
        if root is None:
            return TreeNode(val)
        else:
            if val < root.val:
                root.left = TreeNode.insert(root.left, val)
            else:
                root.right = TreeNode.insert(root.right, val)
        return root

class BFS:
    def bfs(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = collections.deque([root])

        while q:
            level = []  # inner list for nodes at current level
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)  # Append value of current node to level list
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                res.append(level)

        return res




root = TreeNode(5)
root= TreeNode.insert(root,12)
root= TreeNode.insert(root,34)
root= TreeNode.insert(root,43)
root= TreeNode.insert(root,22)
root= TreeNode.insert(root,13)

search=BFS()
print(search.bfs(root))