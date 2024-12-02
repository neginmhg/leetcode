
### **General Template**

1. **Define the DP Table:**
   - Create a 2D DP table (`dp`), where each cell represents the result for a subproblem.
   - Decide the dimensions of the table based on the input size.

2. **State the DP Relation:**
   - Write the recurrence relation to populate the `dp` table.
   - Break the problem into subproblems and relate them using the `dp` table.

3. **Base Case Initialization:**
   - Populate the base cases in the `dp` table, usually corresponding to empty strings, arrays, or edge cases.

4. **Iterate Through the Table:**
   - Use nested loops to fill the `dp` table based on the recurrence relation.
   - Start from smaller subproblems and build up to the entire problem.

5. **Return the Final Answer:**
   - The solution is often found in the last cell (`dp[n][m]`) or aggregated across the table.

---

### **Solution for the Example Problem**

Here’s how you can apply the bottom-up approach to the given problem:

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        
        # Step 1: Define the DP table
        # dp[i][j] = Number of ways to match t[0:i] with s[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Step 2: Base case initialization
        # When t is an empty string, there's exactly 1 way to match
        for j in range(n + 1):
            dp[0][j] = 1
        
        # Step 3: Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, add two possibilities:
                # (1) Match t[i-1] with s[j-1]
                # (2) Skip s[j-1] and keep matching t[0:i] with s[0:j-1]
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    # Skip s[j-1] and keep matching
                    dp[i][j] = dp[i][j - 1]
        
        # Step 4: Return the final answer
        return dp[m][n]
```

---

### **Template Summary:**

**Bottom-Up:**

1. **Define the DP Table:**  
   - A 2D array `dp` where `dp[i][j]` solves the subproblem for `t[:i]` and `s[:j]`.

2. **Base Cases:**  
   - Typically, `dp[0][j] = 1` (t is empty).  
   - Often `dp[i][0] = 0` (t is non-empty, s is empty).

3. **Nested Loops:**  
   - Outer loop over `i` (for string `t`).  
   - Inner loop over `j` (for string `s`).

4. **Transition Relation:**  
   - `dp[i][j] = dp[i-1][j-1] + dp[i][j-1]` (if characters match).  
   - Else, `dp[i][j] = dp[i][j-1]`.

5. **Final Answer:**  
   - Return `dp[m][n]` or other appropriate result.

---

### **Tips for Solving Any 2D DP Problem**

- **Understand the Problem:**  
  Visualize the recursive structure and subproblem dependencies.

- **Draw the Grid:**  
  Sketch out the DP table and label rows/columns to match the problem's components.

- **Base Cases:**  
  Identify cases where no computation is needed (e.g., empty strings or arrays).

- **Transition Relation:**  
  Focus on how the current subproblem depends on smaller subproblems.

- **Optimize Memory:**  
  If only the previous row/column is needed, use a 1D array instead of 2D.

By practicing this template, you can approach all 2D DP problems systematically!