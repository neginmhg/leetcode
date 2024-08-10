# Backtracking

### Whenever you see words like:

- generate all
- compute all
- exhaust all decisions
- possiblities
- combinations

Backtracking is a general **RECURSSION** algorithm for finding all (or some) solutions to computational problems, especially those involving **combinatorial** optimization. It incrementally builds candidates to the solutions and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

### 3 things to figure out when doing backtracking

1. **Choices:** The set of possible decisions/POSSIBILITIES you can make at each step.
2. **Constraints:** The rules/CONDITIONS that must be followed for the decisions.
3. **Goal:** The condition/BASE CASE that identifies a complete solution.

### Steps to Implement Backtracking

1. Choose a candidate.
2. Check if the candidate leads to a solution.
3. If a solution is found, return or store it.
4. If not, discard/POP/remove/etc the candidate and backtrack.
5. Repeat until all candidates are exhausted.
   <br>

### Example Problems

#### 1. **Subset Sum Problem**

**Problem:** Given a set of integers, find all subsets that sum up to a given target.

```python
def find_subsets(nums, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            if nums[i] > target:
                continue
            backtrack(i + 1, path + [nums[i]], target - nums[i])

    nums.sort()
    result = []
    backtrack(0, [], target)
    return result

# Example usage
nums = [2, 3, 6, 7]
target = 7
print(find_subsets(nums, target))  # Output: [[7]]
```

#### 2. **N-Queens Problem**

**Problem:** Place N queens on an N×N chessboard so that no two queens threaten each other.

```python
def solve_n_queens(n):
    def is_not_under_attack(row, col):
        for prev_row in range(row):
            if queens[prev_row] == col or \
               abs(queens[prev_row] - col) == row - prev_row:
                return False
        return True

    def place_queen(row):
        if row == n:
            result.append(queens[:])
            return
        for col in range(n):
            if is_not_under_attack(row, col):
                queens[row] = col
                place_queen(row + 1)
                queens[row] = -1

    result = []
    queens = [-1] * n
    place_queen(0)
    return result

# Example usage
n = 4
solutions = solve_n_queens(n)
for sol in solutions:
    print(sol)
```

### Tips for Implementing Backtracking Algorithms

1. **Prune Early:** Avoid unnecessary recursive calls by checking constraints early.
2. **Use Additional Data Structures:** Hash sets or arrays can be used to keep track of used elements.
3. **Sort Inputs:** Sorting can help in pruning and improving the efficiency of the algorithm.
4. **Use Helper Functions:** Breaking the problem into smaller helper functions can make the code more readable and maintainable.

### Practice Problems

- [LeetCode 39: Combination Sum](https://leetcode.com/problems/combination-sum/)
- [LeetCode 40: Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
- [LeetCode 46: Permutations](https://leetcode.com/problems/permutations/)
- [LeetCode 47: Permutations II](https://leetcode.com/problems/permutations-ii/)
- [LeetCode 51: N-Queens](https://leetcode.com/problems/n-queens/)

### Summary

Backtracking is a powerful technique for solving combinatorial problems. By carefully choosing and discarding candidates, you can efficiently explore possible solutions. Practice with different types of problems to get a good grasp of this algorithm.
