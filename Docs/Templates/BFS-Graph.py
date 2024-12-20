from collections import deque

class Solution:
    def bfs(self, graph, start):
        # Edge case: if start node is not in the graph
        if start not in graph:
            return []

        res = []  # To store the levels of nodes visited
        visited = set()  # To keep track of visited nodes

        # 1. Initialize queue with the start node
        q = deque([start])

        # 2. While loop to process the queue
        while q:
            level = []  # To store nodes at the current level
            # 3. Iterate over the nodes at the current level (all nodes in the queue)
            for _ in range(len(q)):
                # 4. Dequeue the front node
                node = q.popleft()

                # 5. Process the node (e.g., store its value)
                if node not in visited:
                    visited.add(node)
                    level.append(node)

                    # 6. Add unvisited neighbors to the queue
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            q.append(neighbor)

            # Add the current level's nodes to the result
            if level:
                res.append(level)

        return res
