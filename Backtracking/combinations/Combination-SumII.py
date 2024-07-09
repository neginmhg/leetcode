"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Step 1: Sort the candidates to handle duplicates.
        res = []  # Initialize the result list to store unique combinations.

        def backtrack(cur, pos, target):
            # Base case: If target is 0, we've found a valid combination.
            if target == 0:
                res.append(cur.copy())
                return
            # If target is negative, no valid combination can be found.
            if target < 0:
                return
            
            prev = -1  # Initialize `prev` to keep track of the last used element.
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:  # Skip duplicates.
                    continue
                cur.append(candidates[i])  # Include the current number in the combination.
                backtrack(cur, i + 1, target - candidates[i])  # Explore further combinations.
                cur.pop()  # Backtrack by removing the last included number.
                prev = candidates[i]  # Update `prev` to the current number.
        
        backtrack([], 0, target)  # Start the backtracking process with an empty combination.
        return res  # Return the list of all unique combinations.


"The prev variable is used to ensure that the same number is not used more than once at the same level of recursion. This is essential for avoiding duplicate combinations in the final result."