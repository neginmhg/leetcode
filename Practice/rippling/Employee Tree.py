"""
Part 1: Count Direct Reportees

Given a tree-like structure where each node represents an employee and the root node represents the CEO of the company, determine the number of direct reportees of a given manager. Each node has references to its children (direct reportees).



Part 2: Find Common Manager

Given two employees in the organizational tree, find their lowest common manager (i.e., the lowest node in the tree that is an ancestor of both employees).



Part 3: Minimum Weight Branch

Each node in the tree has a weight. Find the branch of the tree with the minimum sum of weights, with the constraint that if you choose a node, you cannot choose its immediate parent or any of its immediate children (no two directly connected nodes can be part of the branch).

"""
class EmployeeNode:
    def __init__(self, id):
        self.id = id
        self.children = []

def count_direct_reportees(manager: EmployeeNode) -> int:
    # The direct reportees are simply the children of the manager.
    return len(manager.children)

# Example usage:
# Constructing the tree:
# CEO -> Manager1, Manager2 -> Employee1, Employee2
ceo = EmployeeNode("CEO")
manager1 = EmployeeNode("Manager1")
manager2 = EmployeeNode("Manager2")
employee1 = EmployeeNode("Employee1")
employee2 = EmployeeNode("Employee2")

ceo.children = [manager1, manager2]
manager1.children = [employee1, employee2]

# Counting direct reportees of Manager1
print(count_direct_reportees(manager1))  # Output: 2

def find_lca(root: EmployeeNode, emp1: str, emp2: str) -> EmployeeNode:
    if not root or root.id == emp1 or root.id == emp2:
        return root

    found = []
    for child in root.children:
        lca = find_lca(child, emp1, emp2)
        if lca:
            found.append(lca)

    # If two children return non-null, root is the LCA.
    if len(found) > 1:
        return root
    # If one child returns non-null, propagate it upward.
    return found[0] if found else None

# Example usage:
lca = find_lca(ceo, "Employee1", "Manager2")
print(lca.id)  # Output: "CEO"

class WeightedNode:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
        self.children = []

def min_weight_branch(root: WeightedNode) -> int:
    def dfs(node):
        if not node.children:
            return (node.weight, 0)  # (Include node, Exclude node)

        include = node.weight
        exclude = 0
        for child in node.children:
            child_include, child_exclude = dfs(child)
            include += child_exclude  # If we include this node, exclude its children
            exclude += min(child_include, child_exclude)  # Min of including or excluding each child

        return (include, exclude)

    return min(dfs(root))

# Example usage:
# Constructing the tree with weights:
root = WeightedNode("CEO", 10)
manager1 = WeightedNode("Manager1", 5)
manager2 = WeightedNode("Manager2", 20)
employee1 = WeightedNode("Employee1", 1)
employee2 = WeightedNode("Employee2", 2)

root.children = [manager1, manager2]
manager1.children = [employee1, employee2]

# Finding the minimum weight branch
print(min_weight_branch(root))  # Output depends on the tree structure and weights

