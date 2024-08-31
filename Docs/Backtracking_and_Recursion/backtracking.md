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

# There are indeed two common approaches to implementing backtracking for problems like generating subsets:

## 1. **Backtracking with Loop**

This approach uses a loop to iterate over elements and then applies the recursive call within the loop. Here’s a breakdown:

#### **Approach**

1. **Start with an Empty Subset**.
2. **Use a Loop** to iterate over the elements starting from the current position.
3. **Include the Element** in the subset and make a recursive call to explore further subsets.
4. **Backtrack**: Remove the element and continue the loop to explore other possibilities.

#### **Example**

```python
def backtrack_with_loop(nums, start, path, res):
    res.append(path.copy())  # Add the current subset to the result
    for i in range(start, len(nums)):
        path.append(nums[i])  # Include the current element
        backtrack_with_loop(nums, i + 1, path, res)  # Explore further with the current element included
        path.pop()  # Backtrack: Remove the element
```

#### **Explanation**

- **Loop through elements**: Use a loop to consider each element starting from the current index.
- **Recursive Exploration**: For each element, recursively call the function to include the current element and explore further.
- **Backtrack**: After the recursive call, remove the last included element and proceed with the next element in the loop.

## 2. **Backtracking Without Explicit Loop**

In this approach, there’s no explicit loop; instead, you rely on recursive calls to handle the iteration and exploration.

#### **Approach**

1. **Start with an Empty Subset**.
2. **Make a Recursive Call** to explore subsets that include the current element.
3. **Backtrack**: Remove the element from the subset.
4. **Make Another Recursive Call** to explore subsets that exclude the current element.

#### **Example**

```python
def backtrack_without_loop(nums, index, path, res):
    if index == len(nums):  # Base case: if index exceeds the length of nums
        res.append(path.copy())  # Add the current subset to the result
        return

    # Include the current element
    path.append(nums[index])
    backtrack_without_loop(nums, index + 1, path, res)

    # Backtrack: Remove the element and explore the next possibility
    path.pop()
    backtrack_without_loop(nums, index + 1, path, res)
```

#### **Explanation**

- **Recursive Calls**: Make a recursive call to explore subsets that include the current element and then backtrack by removing the element.
- **Further Exploration**: After backtracking, make another recursive call to explore subsets that exclude the current element.
- **Base Case**: When all elements have been considered, add the current subset to the result.

### **Summary**

- **Backtracking with Loop**: Uses a loop to iterate over elements, with recursive calls inside the loop to explore subsets. Backtracking is handled after the recursive call by removing the last included element.
- **Backtracking Without Explicit Loop**: Relies on recursive calls to explore subsets. Backtracking is done by removing the element and making another recursive call to explore subsets without the current element.

Both approaches effectively generate all possible subsets, but the loop-based approach often provides a more structured way to handle iteration and exploration. The no-loop approach tends to be more direct but can be less intuitive when handling certain types of problems.

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
