"""
Given n nodes labeled from 0 to n-1 and a list of edges where edges[i] = [a, b] indicates that there is an undirected edge between nodes a and b, write a function to check if these edges make up a valid tree.

Key Points:
A tree is a connected graph without cycles.
The graph should have exactly n-1 edges if it has n nodes (necessary condition for a tree).
Example 1:
Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output: True

Explanation: The graph is connected and contains no cycles, and has exactly n-1 edges. Therefore, it forms a valid tree.

Example 2:
Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: False

Explanation: The graph contains a cycle (1-2-3-1), so it cannot be a valid tree.

Example 3:
Input:

n = 4
edges = [[0, 1], [2, 3]]
Output: False

Explanation: The graph is not connected (two disconnected components), so it cannot be a valid tree.

Constraints:
1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= a, b < n
a != b
There are no duplicate edges.
"""

#Check two conditions:
#Connectedness: The graph must be fully connected, meaning all nodes are reachable from any other node.
#No Cycles: The graph should not contain any cycles.

#Hints:
#hashset to store visited nodes while traversing
#at the end if len(set)==# of nodes then that means all nodes where connected
#if we find a node that is already in set then there's a cycle
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. Create the neighbor map and then populate it
        neighborMap = {i: [] for i in range(n)}
        for node1, node2 in edges:
            neighborMap[node1].append(node2)
            neighborMap[node2].append(node1)
        
        # 2. Create a set to track visited nodes
        visit = set()

        # 3. DFS function to detect cycles
        def isTree(current, prev):
            if current in visit:#found cycle
                return False          
            visit.add(current)
            for nei in neighborMap[current]:
                if nei == prev:
                    continue
                if not isTree(nei, current):
                    return False
            return True

        # 4. Start DFS from node 0, with no parent (-1), and check if all nodes are visited
        return isTree(0, -1) and len(visit) == n




"""
    1. **Visit the Node**: If the current node hasn't been visited, add it to the visited set.
    2. **Explore Neighbors**: For each neighbor of the current node:
    - **Skip the Parent**: If the neighbor is the parent (the node you came from), ignore it.
    - **Recursively Visit**: If the neighbor isn't the parent, recursively apply the same process to it.
    3. **Backtrack**: If a node's only unvisited neighbor is its parent, backtrack to explore other paths.
"""
