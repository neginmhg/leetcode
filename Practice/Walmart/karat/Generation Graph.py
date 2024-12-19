"""
You are tasked with generating a generation graph based on a list of relationships where each relationship describes a parent-child connection. Each node in the graph represents a person, and the edges represent parent-child relationships.

Problem Requirements:

You are given a list of relationships where each relationship is represented as a pair of integers [a, b]. The pair [a, b] indicates that a is the parent of b.
You need to return the generation graph based on these relationships. The generation graph should show the hierarchical relationship between individuals, where nodes represent people, and edges represent parent-child relationships.
The graph should be organized such that you can easily find the generation (level) of each person. People at the same level share the same generation, and the goal is to provide a way to retrieve the generation of a person.
Example:

Input:

relationships = [
    [0, 1],  # 0 is the parent of 1
    [0, 2],  # 0 is the parent of 2
    [1, 3],  # 1 is the parent of 3
    [1, 4],  # 1 is the parent of 4
    [2, 5],  # 2 is the parent of 5
    [2, 6],  # 2 is the parent of 6
]
Output:

{
    0: 0,  # Generation 0 (top-level ancestor)
    1: 1,  # Generation 1 (children of 0)
    2: 1,  # Generation 1 (children of 0)
    3: 2,  # Generation 2 (children of 1)
    4: 2,  # Generation 2 (children of 1)
    5: 2,  # Generation 2 (children of 2)
    6: 2   # Generation 2 (children of 2)
}
Here, each person is assigned to a specific generation, where:

Person 0 is at generation 0 (the root ancestor).
Persons 1 and 2 are at generation 1 (children of 0).
Persons 3, 4, 5, and 6 are at generation 2 (children of 1 and 2).
Constraints:

There will be at most 10,000 relationships.
Each relationship consists of two unique people (a and b), with a != b.
The relationships will form a valid tree (i.e., no cycles).
"""

from collections import defaultdict, deque
class Solution:
    def generate_graph(relationships):
        # Step 1: Create adjacency list and track in-degrees (for topological sorting)
        adj_list = defaultdict(list)
        in_degree = defaultdict(int)
        
        # Step 2: Build the graph based on the relationships
        for parent, child in relationships:
            adj_list[parent].append(child)
            in_degree[child] += 1
            if child not in in_degree:
                in_degree[child] = 0
            if parent not in in_degree:
                in_degree[parent] = 0
        
        # Step 3: Perform a topological sort to determine generation levels
        generation = {}
        queue = deque([node for node in in_degree if in_degree[node] == 0])  # Start with root nodes
        
        # Level of generation starts with 0
        level = 0
        while queue:
            next_queue = deque()
            while queue:
                node = queue.popleft()
                generation[node] = level  # Assign the generation level
                for neighbor in adj_list[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        next_queue.append(neighbor)
            queue = next_queue
            level += 1
        
        return generation


    # Example usage
    relationships = [
        [0, 1],  # 0 is the parent of 1
        [0, 2],  # 0 is the parent of 2
        [1, 3],  # 1 is the parent of 3
        [1, 4],  # 1 is the parent of 4
        [2, 5],  # 2 is the parent of 5
        [2, 6],  # 2 is the parent of 6
    ]

    generation_graph = generate_graph(relationships)
    print(generation_graph)



"""
Time Complexity:
Building the graph: O(E), where E is the number of relationships (edges).
Topological Sort: O(V + E), where V is the number of nodes (unique people) and E is the number of edges (relationships).
Thus, the overall time complexity is O(V + E), where V is the number of distinct individuals and E is the number of relationships.

Space Complexity:
Adjacency list and in-degree map: O(V + E) space, as we store nodes and edges.
"""