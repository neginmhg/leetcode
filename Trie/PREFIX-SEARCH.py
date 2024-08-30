
""" Restaurant Search with Prefix Matching

You are given a list of restaurant names and a list of search queries. For each query, you need to return a list of restaurant names that start with the given query string. The number of results returned for each query should be limited to a maximum of **K** restaurant names.

#### **Input:**
- **N:** An integer representing the number of restaurant names.
- **M:** An integer representing the number of search queries.
- **K:** An integer representing the maximum number of restaurants to return for each query.
- **Restaurant Names:** A list of **N** strings, where each string is the name of a restaurant.
- **Queries:** A list of **M** strings, where each string is a search query.

#### **Output:**
For each query, return a list of up to **K** restaurant names that start with the query string. The restaurant names should be returned in lexicographical order.

#### **Example:**

**Input:**
```
N = 5
restaurants = ["panda express", "panera bread", "domino's pizza", "pizza hut", "starbucks"]
M = 3
queries = ["pan", "pi", "star"]
K = 2
```

**Output:**
```
[
  ["panda express", "panera bread"],  // For the query "pan"
  ["pizza hut", "domino's pizza"],    // For the query "pi"
  ["starbucks"]                       // For the query "star"
]
```

---

### Constraints:
- **1 ≤ N, M ≤ 10^5**
- **1 ≤ K ≤ 100**
- **1 ≤ Length of each restaurant name ≤ 100**
- **1 ≤ Length of each query ≤ 100**

### Goal:
Efficiently find and return up to **K** restaurant names for each query, where each name starts with the query string. Optimize the solution to handle large input sizes.

---

This problem requires an efficient search mechanism to handle potentially large datasets of restaurant names and queries, making the Trie (Prefix Tree) approach an optimal solution.
### **1. **Understand the Problem Requirements

- **Input:**
  - **N:** Number of restaurant names.
  - **M:** Number of search queries.
  - **K:** Maximum number of restaurants to return for each query.
  - **Restaurant Names:** A list of N restaurant names.
  - **Queries:** A list of M search queries.

- **Output:**
  - For each query, return up to **K** restaurants whose names start with the query string.

- **Example:**
  - If K=2 and the query is "pan", the output might be `["panda express", "panera bread"]`.

### **2. **Potential Approaches

#### **a. **Brute Force Approach

- **Description:** For each query, iterate through all restaurant names and check if the name starts with the query string. If it does, add it to the result until you have **K** matches.
- **Time Complexity:** O(M * N * L), where L is the average length of the restaurant name. This approach can be inefficient if N or M is large.

#### **b. **Optimized Approach Using Trie (Prefix Tree)

- **Description:** Use a Trie data structure to store all restaurant names. Each node in the Trie represents a character, and paths down the tree represent prefixes of restaurant names. For each query, traverse the Trie to find all names that match the prefix.

- **Steps:**
  1. **Build the Trie:**
     - Insert all restaurant names into the Trie.
     - Each node in the Trie will store the character and a list of names that pass through that node.

  2. **Search the Trie:**
     - For each query, traverse the Trie from the root following the characters in the query string.
     - Once you reach the end of the query string, return up to **K** restaurant names from that node.

- **Time Complexity:**
  - **Trie Construction:** O(N * L)
  - **Query:** O(M * Q), where Q is the length of the query string. Retrieving results is efficient since you only traverse relevant parts of the Trie.
"""
### **3. **Implementation in Python



class TrieNode:
    def __init__(self):
        self.children = {}
        self.restaurants = []

class Trie:
    def __init__(self,k):
        self.root = TrieNode()
        self.k = k
    def insert(self, name):
        node = self.root
        for char in name:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            # We store the name at every node along the path
            if len(node.restaurants) < self.k:  # Limit to storing K results
                node.restaurants.append(name)

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.restaurants
    

class Solution:
    def restaurant_search(restaurants, queries, k):
        trie = Trie(k)

        # Insert all restaurant names into the Trie
        for name in restaurants:
            trie.insert(name.lower())  # Convert to lowercase for case-insensitive search

        # Process each query
        results = []
        for query in queries:
            matches = trie.search(query.lower())
            #results.append(matches) depending on return type choose this or not
            results.append(", ".join(matches))  # Join results with a comma and space

        return results

k=2

restaurants = ["panda express", "panera bread", "domino's pizza", "pizza hut", "starbucks"]
queries = ["pan", "star"]
res = Solution.restaurant_search(restaurants, queries,k)
print(res)
"""
# Example usage
N = 5
restaurants = ["panda express", "panera bread", "domino's pizza", "pizza hut", "starbucks"]
M = 3
queries = ["pan", "pi", "star"]
K = 2

print(restaurant_search(N, restaurants, M, queries, K))


### **4. **Explanation

- **Trie Construction:** 
  - We insert each restaurant name into the Trie, storing a list of matching restaurants at each node.
  
- **Query Handling:**
  - For each search query, we traverse the Trie following the characters in the query string. 
  - Once the query string is exhausted, we return the list of restaurants stored at that node.

### **5. **Performance Considerations

- **Memory Usage:** The Trie can use a significant amount of memory, especially if there are many restaurants with long names. However, it efficiently supports fast prefix searches.
- **Search Efficiency:** The Trie allows for very fast prefix searches, which is crucial when handling a large number of queries.

This approach is well-suited for scenarios where you need to handle a large number of restaurant names and search queries efficiently, such as in a search bar for a service like DoorDash.
"""