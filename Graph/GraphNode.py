class GraphNode:
    def __init__(self, value):
        """
        Initialize a graph node with a given value.
        """
        self.value = value           # Value of the node
        self.neighbors = []          # List of adjacent nodes (edges)

    def add_neighbor(self, neighbor):
        """
        Add a neighbor to this node's list of neighbors.
        """
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def __repr__(self):
        """
        Return a string representation of the node.
        """
        return f"GraphNode({self.value})"

# Example usage
if __name__ == "__main__":
    # Create nodes
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)

    # Connect nodes
    node1.add_neighbor(node2)
    node1.add_neighbor(node3)
    node2.add_neighbor(node3)

    # Print nodes and their neighbors
    print(node1)  # Output: GraphNode(1)
    print(node1.neighbors)  # Output: [GraphNode(2), GraphNode(3)]
    print(node2)  # Output: GraphNode(2)
    print(node2.neighbors)  # Output: [GraphNode(3)]
