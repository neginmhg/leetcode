""""
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort the list to handle duplicates easily.

        def backtrack(i, subset):
            # Base case: if we have considered all elements
            if i == len(nums):
                res.append(subset[::])  # Add a copy of the current subset to the results.
                return

            # Include nums[i] in the subset and move to the next element
            subset.append(nums[i])
            backtrack(i + 1, subset)  # Explore subsets including nums[i]
            subset.pop()  # Backtrack: Remove nums[i] from the subset

            # Skip all duplicates of nums[i] to avoid generating duplicate subsets
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1  # Move to the next distinct element
            
            # Explore subsets without including nums[i]
            backtrack(i + 1, subset)  # Explore subsets excluding nums[i]

        backtrack(0, [])  # Start with an empty subset and from the 0th index
        return res  # Return the list of all unique subsets
