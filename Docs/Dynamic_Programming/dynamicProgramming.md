Dynamic Programming (DP) is a powerful technique used to solve problems by breaking them down into simpler subproblems and storing the results of these subproblems to avoid redundant calculations. Here’s a comprehensive guide to help you tackle DP problems on LeetCode.
DP= recursion +memoization()
steps:
1. write the recursive equation
2. write the base case 
3. add memo to optimize answers
### **Key Concepts of Dynamic Programming**

1. **Overlapping Subproblems:**
   - Problems can be broken down into subproblems that are reused multiple times. DP avoids solving the same subproblem multiple times by storing the results.

2. **Optimal Substructure:**
   - The solution to the problem can be composed of solutions to subproblems.

3. **Memoization vs. Tabulation:**
   - **Memoization (Top-Down):** Recursively break down the problem and store the results of subproblems (using a hash map or an array) to avoid redundant calculations.
   - **Tabulation (Bottom-Up):** Solve the problem by iteratively filling up a table (usually an array) based on previously solved subproblems.

### **Common Dynamic Programming Patterns**

1. **1D DP Array Problems:**
   - **Fibonacci Numbers:** Problems that involve linear recurrence relations.
     - **Example:** [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
   - **Pattern:** 
     - Identify the base cases.
     - Use a single array (or variables) to store previous results.

   ```python
   def fib(n):
       if n <= 1:
           return n
       dp = [0] * (n + 1)
       dp[1] = 1
       for i in range(2, n + 1):
           dp[i] = dp[i - 1] + dp[i - 2]
       return dp[n]
   ```

2. **2D DP Array Problems (Grid-Based DP):**
   - **Unique Paths:** Problems where you need to find the number of ways or minimum paths in a grid.
     - **Example:** [Unique Paths](https://leetcode.com/problems/unique-paths/)
   - **Pattern:** 
     - Use a 2D array to store results.
     - Fill the table based on previous cells (usually from top and left).

   ```python
   def uniquePaths(m, n):
       dp = [[1] * n for _ in range(m)]
       for i in range(1, m):
           for j in range(1, n):
               dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
       return dp[m - 1][n - 1]
   ```

3. **Subset/Partition DP Problems:**
   - **Knapsack:** Problems involving selection of items to maximize/minimize some value.
     - **Example:** [0/1 Knapsack Problem](https://leetcode.com/problems/partition-equal-subset-sum/)
   - **Pattern:** 
     - Use a 1D or 2D DP array to store possible values.
     - Iterate over items and update DP array.

   ```python
   def canPartition(nums):
       total = sum(nums)
       if total % 2 != 0:
           return False
       target = total // 2
       dp = [False] * (target + 1)
       dp[0] = True
       for num in nums:
           for i in range(target, num - 1, -1):
               dp[i] = dp[i] or dp[i - num]
       return dp[target]
   ```

4. **Longest Subsequence Problems:**
   - **Longest Increasing Subsequence (LIS):** Problems that require finding the longest subsequence with specific properties.
     - **Example:** [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
   - **Pattern:**
     - Use a 1D array where each entry represents the longest subsequence ending at that position.
     - Update the array by checking all previous positions.

   ```python
   def lengthOfLIS(nums):
       if not nums:
           return 0
       dp = [1] * len(nums)
       for i in range(1, len(nums)):
           for j in range(i):
               if nums[i] > nums[j]:
                   dp[i] = max(dp[i], dp[j] + 1)
       return max(dp)
   ```

5. **Palindrome-Based Problems:**
   - **Palindromic Substrings:** Problems dealing with palindromes in strings.
     - **Example:** [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
   - **Pattern:**
     - Use a 2D DP array where `dp[i][j]` represents if the substring from `i` to `j` is a palindrome.
     - Expand around centers or use tabulation to check palindromes.

   ```python
   def longestPalindrome(s):
       n = len(s)
       dp = [[False] * n for _ in range(n)]
       start, max_len = 0, 1
       for i in range(n):
           dp[i][i] = True
       for length in range(2, n + 1):
           for i in range(n - length + 1):
               j = i + length - 1
               if s[i] == s[j]:
                   if length == 2 or dp[i + 1][j - 1]:
                       dp[i][j] = True
                       if length > max_len:
                           start = i
                           max_len = length
       return s[start:start + max_len]
   ```

6. **String Matching/Transformation Problems:**
   - **Edit Distance:** Problems involving transforming one string into another with minimum operations.
     - **Example:** [Edit Distance](https://leetcode.com/problems/edit-distance/)
   - **Pattern:**
     - Use a 2D DP array where `dp[i][j]` represents the minimum operations to convert `s1[0:i]` to `s2[0:j]`.
     - Fill the table based on insertion, deletion, and substitution.

   ```python
   def minDistance(word1, word2):
       m, n = len(word1), len(word2)
       dp = [[0] * (n + 1) for _ in range(m + 1)]
       for i in range(m + 1):
           dp[i][0] = i
       for j in range(n + 1):
           dp[0][j] = j
       for i in range(1, m + 1):
           for j in range(1, n + 1):
               if word1[i - 1] == word2[j - 1]:
                   dp[i][j] = dp[i - 1][j - 1]
               else:
                   dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
       return dp[m][n]
   ```

7. **State Compression DP:**
   - **Problems involving bitwise operations to compress states.**
     - **Example:** [Travelling Salesman Problem (TSP)](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)
   - **Pattern:**
     - Use bitmasks to represent states and use a DP table to keep track of the minimal cost/steps to achieve a state.

   ```python
   def shortestPathLength(graph):
       n = len(graph)
       dp = [[float('inf')] * n for _ in range(1 << n)]
       queue = deque([(i, 1 << i, 0) for i in range(n)])
       for i in range(n):
           dp[1 << i][i] = 0
       while queue:
           u, mask, dist = queue.popleft()
           if mask == (1 << n) - 1:
               return dist
           for v in graph[u]:
               next_mask = mask | (1 << v)
               if dist + 1 < dp[next_mask][v]:
                   dp[next_mask][v] = dist + 1
                   queue.append((v, next_mask, dist + 1))
       return -1
   ```

### **Approach to Solving DP Problems**

1. **Identify if the problem is a DP problem:**
   - Look for phrases like “minimum,” “maximum,” “number of ways,” or “can be achieved by.”

2. **Define the state:**
   - Identify the variables that change and define your DP state around them.

3. **Identify the recurrence relation:**
   - Determine how the current state can be derived from previous states.

4. **Base Case(s):**
   - Identify the simplest case that can be solved trivially.

5. **Implement the DP table or recursive function with memoization.**

6. **Optimize if necessary:**
   - Look for ways to reduce space or time complexity, often by converting a 2D DP to 1D or reducing state space.

### **Common DP Problems to Practice on LeetCode**

1. **Easy:**
   - [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
   - [House Robber](https://leetcode.com/problems/house-robber/)
   - [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

2. **Medium:**
   - [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
   - [Coin Change](https://leetcode.com/problems/coin-change/)
   - [Partition Equal
  

The decision of whether to have a `dp` array of size `n` or `n + 1` depends on whether your dynamic programming (DP) solution needs to account for **"nothing"** or **"empty"** state scenarios, in addition to processing the full range of elements. Let's break it down:

### Use `dp` size `n + 1` when:
You need to track the **state before processing the first element**, often represented as an **empty string** or **base case**. This extra state helps handle cases where no characters or elements have been processed yet.

#### Examples where `dp` size is `n + 1`:

1. **Decoding ways (like this problem)**:
   - You need a `dp[0]` to represent the **empty string** (no characters processed yet). This allows you to initialize the base case (1 way to decode nothing).
   - Then you process from `dp[1]` to `dp[n]` to compute the number of ways to decode up to each character.
   
   For string `"226"` (length `n = 3`), you need a `dp` of size `n + 1 = 4` to account for:
   ```
   dp = [dp[0], dp[1], dp[2], dp[3]]  # Size = n + 1
   ```

2. **Fibonacci or other recurrence relations with base cases**:
   - You often define `dp[0]` as part of your base case (e.g., Fibonacci with `dp[0] = 0` and `dp[1] = 1`).
   - The extra space (`n + 1`) ensures you can define this base case and still compute values for the full range from `1` to `n`.

3. **Knapsack problem**:
   - The size of `dp` is often `n + 1` when you need to include a "0 capacity" base case (when the knapsack is empty).
   - Similarly, in **subset sum** problems, you may need `dp[0]` to represent the case when no elements have been selected yet (like a sum of 0).

#### Why use `n + 1`?
- The **extra `dp[0]`** position is crucial for handling base cases, like the **empty string** or **no elements** processed. Without this, the recurrence relation would fail to initialize correctly.

---

### Use `dp` size `n` when:
You only need to track the states **for each element** and don’t care about an "empty" or "nothing" state. In other words, you only need to compute values for the elements directly and don't need a base case for "zero elements."

#### Examples where `dp` size is `n`:

1. **Maximum subarray sum (Kadane's Algorithm)**:
   - Here, you only care about the largest sum ending at each position `i`, so you don't need a `dp[0]` for an empty array.
   - For an array of size `n`, you would use a `dp` array of size `n`:
     ```
     dp = [dp[0], dp[1], ..., dp[n-1]]  # Size = n
     ```

2. **Longest increasing subsequence**:
   - The `dp[i]` represents the length of the longest subsequence that ends at index `i`. There’s no "empty sequence" base case needed, so a `dp` array of size `n` suffices.

3. **Other single-pass problems**:
   - If you are processing elements directly in a single pass (e.g., finding the max or min value up to index `i`), you don’t need an extra slot for an "empty" state.

#### Why use `n`?
- If you don’t need to consider an "empty state" or "base case," having an extra slot is unnecessary. You just need to track the state up to the `n`-th element directly, and a `dp` array of size `n` is sufficient.

---

### Summary:
- Use **size `n + 1`** when you need to account for a **base case** like an empty string, no elements selected, or a "0th" state.
- Use **size `n`** when you only care about the **elements themselves** and don’t need a base case for zero elements.

.
