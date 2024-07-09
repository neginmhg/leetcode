"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""
#In combinations, where the order of elements does not matter, 
# In permutations, the order of elements matter

# The number of permutations of a set of n elements is n!
# For example, the number of permutations of a set of 3 elements is 3!=3×2×1=6.
from typing import List

"All possible arrangements of a set where the order matters."

class Solution:
    """ There are 2 solutions:
    | Approach      | Time Complexity | Space Complexity |
    |---------------|-----------------|------------------|
    | Iterative     | O(n! * n^2)     | O(n * n!)        |
    | Recursive     | O(n! * n  )     | O(n * n!)        |
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        # time compplexity: n! * n^2

        # Initialize with an empty permutation
        perms =[[]]
        # Iterate over each number in nums
        for n in nums: #for each number
            new_perms=[]
             # Iterate over each existing permutation in perms
            for p in perms:#for each permutation
                # Insert the current number into each possible position in the permutation
                for i in range(len(p)+1):#for positions
                    p_copy=p.copy() # Create a copy of the current permutation
                    p_copy.insert(i,n)  # Insert the current number at position i
                    new_perms.append(p_copy)    # Add the new permutation to new_perms
            
             # Update perms to be the new_perms for the next iteration
            perms=new_perms
        return perms
    


    def permuteRecurssive(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current_permutation: List[int], results: List[List[int]]):
            # Base case: if the current permutation has the same length as nums
            if len(current_permutation) == len(nums):
                results.append(current_permutation.copy())
                return
            
            # Recursive case: try adding each element to the current permutation
            for num in nums:
                if num not in current_permutation:
                    # Add num to the current permutation
                    current_permutation.append(num)
                    # Recursively build the next part of the permutation
                    backtrack(current_permutation, results)
                    # Remove the last added element to backtrack
                    current_permutation.pop()
        
        results = []
        backtrack([], results)
        return results
 
 
"""
Here is the recursive approach step-by-step for generating permutations with `nums = [1, 2, 3]`:

1. **Initialization**:
   - Start with an empty current permutation: `current_permutation = []`
   - Results list: `results = []`

### Step-by-Step Walkthrough with `nums = [1, 2, 3]`

1. **Start**:
   - `current_permutation = []`
   - `results = []`

2. **First Recursive Call**:
   - Loop through `nums = [1, 2, 3]`.
   - **Add 1**:
     - `current_permutation = [1]`
     - Call `backtrack([1], results)`

3. **Second Recursive Call**:
   - `current_permutation = [1]`
   - Loop through `nums = [1, 2, 3]`.
   - **Add 2**:
     - `current_permutation = [1, 2]`
     - Call `backtrack([1, 2], results)`

4. **Third Recursive Call**:
   - `current_permutation = [1, 2]`
   - Loop through `nums = [1, 2, 3]`.
   - **Add 3**:
     - `current_permutation = [1, 2, 3]`
     - Call `backtrack([1, 2, 3], results)`

5. **Base Case Reached**:
   - `current_permutation = [1, 2, 3]`
   - Since the length of `current_permutation` equals the length of `nums`, add `[1, 2, 3]` to `results`.
   - `results = [[1, 2, 3]]`
   - Backtrack: Remove 3.
   - `current_permutation = [1, 2]`

6. **Backtrack to Second Call**:
   - `current_permutation = [1, 2]`
   - Continue the loop in the second call.
   - **Add 3** (skipping because it's already present in `current_permutation`).
   - Backtrack: Remove 2.
   - `current_permutation = [1]`

7. **Backtrack to First Call**:
   - `current_permutation = [1]`
   - Continue the loop in the first call.
   - **Add 3**:
     - `current_permutation = [1, 3]`
     - Call `backtrack([1, 3], results)`

8. **Second Recursive Call**:
   - `current_permutation = [1, 3]`
   - Loop through `nums = [1, 2, 3]`.
   - **Add 2**:
     - `current_permutation = [1, 3, 2]`
     - Call `backtrack([1, 3, 2], results)`

9. **Base Case Reached**:
   - `current_permutation = [1, 3, 2]`
   - Since the length of `current_permutation` equals the length of `nums`, add `[1, 3, 2]` to `results`.
   - `results = [[1, 2, 3], [1, 3, 2]]`
   - Backtrack: Remove 2.
   - `current_permutation = [1, 3]`
   - Backtrack: Remove 3.
   - `current_permutation = [1]`

10. **Backtrack to Start**:
    - `current_permutation = [1]`
    - Continue the loop in the first call.
    - **Add 2**:
      - `current_permutation = [2]`
      - Call `backtrack([2], results)`

11. **Second Recursive Call**:
    - `current_permutation = [2]`
    - Loop through `nums = [1, 2, 3]`.
    - **Add 1**:
      - `current_permutation = [2, 1]`
      - Call `backtrack([2, 1], results)`

12. **Third Recursive Call**:
    - `current_permutation = [2, 1]`
    - Loop through `nums = [1, 2, 3]`.
    - **Add 3**:
      - `current_permutation = [2, 1, 3]`
      - Call `backtrack([2, 1, 3], results)`

13. **Base Case Reached**:
    - `current_permutation = [2, 1, 3]`
    - Since the length of `current_permutation` equals the length of `nums`, add `[2, 1, 3]` to `results`.
    - `results = [[1, 2, 3], [1, 3, 2], [2, 1, 3]]`
    - Backtrack: Remove 3.
    - `current_permutation = [2, 1]`

14. **Backtrack to Second Call**:
    - `current_permutation = [2, 1]`
    - Continue the loop in the second call.
    - **Add 3** (skipping because it's already present in `current_permutation`).
    - Backtrack: Remove 1.
    - `current_permutation = [2]`

15. **Backtrack to First Call**:
    - `current_permutation = [2]`
    - Continue the loop in the first call.
    - **Add 3**:
      - `current_permutation = [2, 3]`
      - Call `backtrack([2, 3], results)`

16. **Second Recursive Call**:
    - `current_permutation = [2, 3]`
    - Loop through `nums = [1, 2, 3]`.
    - **Add 1**:
      - `current_permutation = [2, 3, 1]`
      - Call `backtrack([2, 3, 1], results)`

17. **Base Case Reached**:
    - `current_permutation = [2, 3, 1]`
    - Since the length of `current_permutation` equals the length of `nums`, add `[2, 3, 1]` to `results`.
    - `results = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]]`
    - Backtrack: Remove 1.
    - `current_permutation = [2, 3]`
    - Backtrack: Remove 3.
    - `current_permutation = [2]`
    - Backtrack: Remove 2.
    - `current_permutation = []`

18. **Backtrack to Start**:
    - `current_permutation = []`
    - Continue the loop in the first call.
    - **Add 3**:
      - `current_permutation = [3]`
      - Call `backtrack([3], results)`

19. **Second Recursive Call**:
    - `current_permutation = [3]`
    - Loop through `nums = [1, 2, 3]`.
    - **Add 1**:
      - `current_permutation = [3, 1]`
      - Call `backtrack([3, 1], results)`

20. **Third Recursive Call**:
    - `current_permutation = [3, 1]`
    - Loop through `nums = [1, 2, 3]`.
    - **Add 2**:
      - `current_permutation = [3, 1, 2]`
      - Call `backtrack([3, 1, 2], results)`

21. **Base Case Reached**:
    - `current_permutation = [3, 1, 2]`
    - Since the length of `current_permutation` equals the length of `nums`, add `[3, 1, 2]` to `results`.
    - `results = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]]`
    - Backtrack: Remove 2.
    - `current_permutation = [3, 1]`

22. **Backtrack to Second Call**:
    - `current_permutation = [3, 1]`
    - Continue the loop in the second call.
    - **Add 2** (skipping because it's already present in `current_permutation`).
    - Backtrack: Remove 1.
    - `current_permutation = [3]`

23. **Backtrack to First Call**:
    - `current_permutation = [3]`
    - Continue the loop in the first call.
    - **Add 2**:
      - `current_permutation = [3, 2]`
      - Call `backtrack([3, 2], results)`

24. **Second Recursive Call**:
    - `current_permutation = [3, 2]`
    - Loop through `nums = [1, 2, 3]`.
    - **Add 1**:
      - `current_permutation = [3, 2, 1]`
      - Call `backtrack([3, 2, 1
 """