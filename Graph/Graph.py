class Graph:
    def __init__(self, directed=False):
        """
        Initialize the graph.
        :param directed: Boolean indicating if the graph is directed.
        """
        self.directed = directed  # Indicates whether the graph is directed or undirected
        self.nodes = {}           # Dictionary to hold node values and their adjacency lists

    def add_node(self, value):
        """
        Add a node to the graph.
        :param value: The value of the node to add.
        """
        if value not in self.nodes:
            self.nodes[value] = []

    def add_edge(self, from_node, to_node):
        """
        Add an edge between two nodes.
        :param from_node: The starting node of the edge.
        :param to_node: The ending node of the edge.
        """
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)
        
        self.nodes[from_node].append(to_node)
        if not self.directed:
            self.nodes[to_node].append(from_node)

    def __repr__(self):
        """
        Return a string representation of the graph.
        """
        result = []
        for node, neighbors in self.nodes.items():
            result.append(f"{node} -> {', '.join(map(str, neighbors))}")
        return "\n".join(result)

# Example usage
if __name__ == "__main__":
    # Create a directed graph
    graph = Graph(directed=True)

    # Add nodes and edges
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(1, 3)

    # Print the graph
    print(graph)

    # Output:
    # 1 -> 2, 3
    # 2 -> 3
    # 3 -> 
