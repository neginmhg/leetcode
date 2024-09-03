""""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) +1
        # Create an array parent where each node is its own parent (initially, parent[i] = i).
        parent = [i for i in range(n)]
        # Create an array rank to manage the union by rank (initially, rank[i] = 1).
        rank = [1] * n

        # Define Helper Functions:

        # Find:
        # If parent[node] is not equal to node, recursively find the root of node.
        # Apply path compression by setting parent[node] to the result of the recursive find.
        # Return the root of node.
        def find(index):
            value  = parent[index]
            if value != index:
                value= find(value)
            return value

        # Union:
        # Find the root of both nodes (root1 for node1, root2 for node2).
        # If root1 is equal to root2, a cycle is detected, return False.
        # Otherwise, perform union by rank:
        # If rank[root1] > rank[root2], set parent[root2] = root1.
        # Else if rank[root1] < rank[root2], set parent[root1] = root2.
        # If ranks are equal, set parent[root2] = root1 and increase rank[root1].
        # Return True.
        def union(node1, node2):
            root1=find(node1)
            root2=find(node2)
            if root1 == root2:
                return False
            if rank[root1]>rank[root2]:
                parent[root2] = root1
            elif rank[root1]<rank[root2]:
                parent[root1] =root2
            else:
                parent[root2]=root1
                rank[root1]+=1
            return True
        



        # Process Each Edge:
        # For each edge [node1, node2] in the edges array:
        # If the union(node1, node2) returns False, return this edge as the redundant one.
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1,node2]
        # Return:
        # If no redundant edge is found during the loop (which shouldn't happen given the problem constraints), 
        # return an empty array or handle it as an edge case.
        return []





#my DFS approach to detect cycles and identify the redundant edge is valid but requires careful implementation, especially for cycle detection and backtracking. After finding a cycle, you would iterate through the edges in reverse to identify the redundant one. 

#However, the Union-Find approach is typically simpler and more efficient for this problem. It directly identifies the redundant edge by checking if two nodes are already in the same set during edge processing, avoiding the need for explicit cycle detection or backtracking. The Union-Find method is often preferred for its simplicity and efficiency in handling such tasks