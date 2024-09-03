"""
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:
Input:
n=3
edges=[[0,1], [0,2]]
Output:
1

Example 2:
Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]
Output:
2

Constraints:
1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""
#union find
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Helper function to find the root of a node
        def find(node):
            # If the node is not its own parent, recursively find the root
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression to flatten the structure
            return parent[node]  # Return the root of the node
        
        # Helper function to unite two components
        def union(node1, node2):
            root1 = find(node1)  # Find the root of the first node
            root2 = find(node2)  # Find the root of the second node
            if root1 != root2:  # If the roots are different, they belong to different components
                parent[root1] = root2  # Union the components by connecting the roots
                return True  # Return True to indicate that a union occurred
            return False  # Return False if the nodes were already in the same component
        
        # Initially, each node is its own parent (disjoint sets)
        parent = [i for i in range(n)]
        components = n  # Start with n components (each node is its own component)
        
        # Process each edge in the graph
        for node1, node2 in edges:
            if union(node1, node2):  # If a union is successful (nodes were in different components)
                components -= 1  # Decrease the number of components by 1
        
        return components  # Return the total number of connected components
