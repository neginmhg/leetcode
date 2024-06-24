"""
HARD


Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Trees.TreeNode import TreeNode


class Codec:

    def serialize(self, root):
        #We can use a pre-order traversal (node, left, right)
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))       #put the vals and N in array
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)         #convert the array to 1 string with commas
        

    def deserialize(self, data):
        vals = data.split(",")  #turn the string into array of strings
        self.i=0

        def dfs():
            if vals[self.i]=="N":
                self.i+=1
                return None
            node =TreeNode(int(vals[self.i]))
            self.i +=1
            node.left= dfs()
            node.right =dfs()
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))