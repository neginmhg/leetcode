"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 
"""

from typing import List
class Solution:
    #the subsets problem you provided is a combination problem, not a permutation problem. 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        subset=[]
        def dfs(i):
            if i>= len(nums):       #after we went through the whole nums
                res.append(subset.copy()) #then add a copy of nums
                return  #We return to stop further processing in this recursive branch.
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            #decision not to include nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
