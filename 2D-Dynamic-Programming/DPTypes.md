### **1. Subsequence Problems**
These problems involve finding patterns or sequences within a larger sequence.

- **Examples:**
  - Longest Common Subsequence (LCS)
  - Longest Increasing Subsequence (LIS)
  - Number of Distinct Subsequences
  - Edit Distance (Minimum Operations to Transform One String into Another)
  - Palindromic Substrings / Longest Palindromic Subsequence

- **Key Idea:**  
  Use 2D DP with relationships between indices of the strings or sequences.

---

### **2. Knapsack Problems**
These problems involve selecting items with constraints (like weight or capacity) to maximize or minimize a certain value.

- **Examples:**
  - 0/1 Knapsack
  - Unbounded Knapsack
  - Subset Sum Problem
  - Partition Equal Subset Sum
  - Coin Change (Min Coins or Number of Ways)

- **Key Idea:**  
  Use 1D or 2D DP arrays where each state represents a possible combination of capacity or value.

---

### **3. Grid/Matrix-Based Problems**
These problems require navigating or finding optimal paths in a 2D grid or matrix.

- **Examples:**
  - Minimum Path Sum
  - Unique Paths
  - Dungeon Game (Survival Problems)
  - Maximal Square (Finding Largest Square of 1s)
  - Cherry Pickup

- **Key Idea:**  
  Use 2D DP where each cell depends on adjacent cells (left, top, diagonal).

---

### **4. Partitioning Problems**
These problems involve dividing an array or string into subarrays or substrings to achieve a specific goal.

- **Examples:**
  - Palindrome Partitioning (Minimum Cuts)
  - Word Break Problem
  - Burst Balloons (Max Coins)
  - Split Array into Largest Sum

- **Key Idea:**  
  Use DP to evaluate all possible partitions and minimize/maximize a given function.

---

### **5. Game Theory Problems**
These problems involve making optimal decisions in turn-based games.

- **Examples:**
  - Predict the Winner
  - Stone Game (and Variants)
  - Nim Game
  - Optimal Strategy for a Game

- **Key Idea:**  
  Use DP to model the choices of both players and calculate outcomes recursively.

---

### **6. Interval DP Problems**
These involve dividing a range or interval into smaller parts to find the optimal solution.

- **Examples:**
  - Matrix Chain Multiplication
  - Burst Balloons
  - Merging Stones (Minimum Cost)
  - Minimum Cost to Cut a Stick

- **Key Idea:**  
  Use 2D DP where `dp[i][j]` represents the optimal solution for the range `[i, j]`.

---

### **7. Tree-Based DP**
These problems involve traversing a tree and computing optimal values for each subtree.

- **Examples:**
  - Diameter of a Binary Tree
  - House Robber III (on Trees)
  - Binary Tree Maximum Path Sum
  - Maximum Weight Independent Set (on Trees)

- **Key Idea:**  
  Use DFS with DP to compute values for each node based on its children.

---

### **8. Bitmask DP**
These problems involve subsets or combinations that can be represented as binary states.

- **Examples:**
  - Traveling Salesman Problem (TSP)
  - Minimum XOR Sum of Two Arrays
  - Assigning Tasks or Jobs
  - Partition Problems with Constraints

- **Key Idea:**  
  Use a DP array indexed by bitmasks to represent subsets or states.

---

### **9. Linear DP**
These problems involve finding the optimal solution for arrays or lists by considering adjacent elements.

- **Examples:**
  - House Robber
  - Maximum Subarray (Kadane's Algorithm)
  - Jump Game (and Variants)
  - Climbing Stairs

- **Key Idea:**  
  Use a 1D DP array where `dp[i]` depends on previous states like `dp[i-1]` or `dp[i-2]`.

---

### **10. Probability/Expectation Problems**
These problems involve calculating probabilities or expected values using DP.

- **Examples:**
  - Dice Roll Simulation
  - New 21 Game
  - Domino and Tromino Tiling
  - Random Walks on a Grid

- **Key Idea:**  
  Use DP to compute probabilities recursively for each state.

---

### **11. Memory Optimization Problems**
These involve choosing actions or paths to minimize memory usage or maximize resource utilization.

- **Examples:**
  - Fibonacci Sequence (Space Optimization)
  - Maximum Profit in Job Scheduling
  - Weighted Interval Scheduling

- **Key Idea:**  
  Use state compression to reduce space or optimize for memory usage.

---

### **12. Counting Problems**
These problems require counting the number of ways to achieve a goal.

- **Examples:**
  - Unique Paths
  - Coin Change (Number of Ways)
  - Decode Ways (Number of Decodings for a String)
  - Count of Palindromic Subsequences

- **Key Idea:**  
  Use DP to count combinations or sequences recursively.

---

### **Approach for Any DP Problem**

1. Identify the type of problem (from the list above).
2. Define the state of your DP table (`dp[i][j]` or `dp[i]`).
3. Write the transition relation (recurrence).
4. Initialize base cases.
5. Use iteration or recursion to fill the DP table.
6. Return the final result.

Practicing problems from each category will help you recognize patterns and become more proficient with DP techniques!