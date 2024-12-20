import collections
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
		


class Solution:
    def bfs(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res =[]

        #1. Queue
        q = collections.deque([root])


        #2. while loop and pop q
        while q:
            level=[]
            # 3. For level by level
            for _ in range(len(q)):
                # 4. POPLEFT
                node = q.popleft()
                if node:
                    level.append(node.val)
                    #5. Append to queue left and right 
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                res.append(level)

        return res

