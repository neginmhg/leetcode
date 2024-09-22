Summarizing the time complexities for various data structures regarding common operations:

| Data Structure               | Access                               | Search                        | Insertion                     | Deletion                              | Sorting                   |
| ---------------------------- | ------------------------------------ | ----------------------------- | ----------------------------- | ------------------------------------- | ------------------------- |
| **Array**                    | O(1)                                 | O(n)                          | O(n)                          | O(n)                                  | O(n log n)                |
| **Dynamic Array**            | O(1)                                 | O(n)                          | O(1) amortized                | O(n)                                  | O(n log n)                |
| **Singly Linked List**       | O(n)                                 | O(n)                          | O(1)                          | O(1) (if at head) / O(n) (if at tail) | O(n) (not sorted)         |
| **Doubly Linked List**       | O(n)                                 | O(n)                          | O(1)                          | O(1)                                  | O(n) (not sorted)         |
| **Stack**                    | O(1)                                 | O(n)                          | O(1)                          | O(1)                                  | O(n) (not sorted)         |
| **Queue**                    | O(1)                                 | O(n)                          | O(1)                          | O(1)                                  | O(n) (not sorted)         |
| **Hash Table**               | O(1) average / O(n) worst            | O(1) average / O(n) worst     | O(1) average / O(n) worst     | O(1) average / O(n) worst             | O(n log n) (for keys)     |
| **Set**                      | O(1) average / O(n) worst            | O(1) average / O(n) worst     | O(1) average / O(n) worst     | O(1) average / O(n) worst             | O(n log n) (for elements) |
| **Binary Tree**              | O(n)                                 | O(n)                          | O(log n) average / O(n) worst | O(log n) average / O(n) worst         | O(n) (not sorted)         |
| **Binary Search Tree**       | O(n) worst / O(log n) average        | O(n) worst / O(log n) average | O(log n) average / O(n) worst | O(log n) average / O(n) worst         | O(n) (in-order)           |
| **AVL Tree**                 | O(log n)                             | O(log n)                      | O(log n)                      | O(log n)                              | O(n) (in-order)           |
| **Red-Black Tree**           | O(log n)                             | O(log n)                      | O(log n)                      | O(log n)                              | O(n) (in-order)           |
| **Heap**                     | O(n)                                 | O(n)                          | O(log n)                      | O(log n)                              | O(n log n)                |
| **Trie**                     | O(m) (m = length of string)          | O(m)                          | O(m)                          | O(m)                                  | O(m \* n) (for n strings) |
| **Graph (Adjacency Matrix)** | O(1)                                 | O(n)                          | O(1)                          | O(1)                                  | O(n^3) (Floyd-Warshall)   |
| **Graph (Adjacency List)**   | O(n)                                 | O(n)                          | O(1)                          | O(1)                                  | O(n + m) (for edges)      |
| **Segment Tree**             | O(log n)                             | O(log n)                      | O(log n)                      | O(log n)                              | O(n log n)                |
| **Fenwick Tree**             | O(log n)                             | O(log n)                      | O(log n)                      | O(log n)                              | O(n log n)                |
| **Disjoint Set**             | O(α(n)) (inverse Ackermann function) | N/A                           | O(α(n))                       | O(α(n))                               | N/A                       |

### Notes:

- **Amortized Time**: Refers to the average time taken over a sequence of operations, not the worst-case time for any single operation.
- **Sorting**: The complexities provided are general cases; for specific data structures, sorting might require additional steps (like using a different structure to sort).
- **Graphs**: The time complexities can vary based on the specific algorithms used for searching (like BFS or DFS) and their representation (adjacency matrix vs. adjacency list).
