class Solution:
    def dfs(self, graph, node, visited):
        # 1. Base Case: If the node is already visited, return
        if node in visited:
            return
        visited.add(node)  # Mark the current node as visited

        # 2. Process the current node (e.g., print it, check conditions)
        print(node)  # For example, print the node value

        # 3. Recurse to neighbors (for each neighboring node in graph)
        for neighbor in graph[node]:
            # 4. Recursive call for neighbors
            self.dfs(graph, neighbor, visited)

    def main(self, graph):
        visited = set()  # Set to track visited nodes
        for node in graph:
            if node not in visited:
                self.dfs(graph, node, visited)  # Start DFS from the node
