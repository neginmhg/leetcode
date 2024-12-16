""" [EASY]
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List
class Solution:
    def twoSum(self, nums:List[int], target:int)->List[int]:
        prevMap={}  #dictionary {value:index}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in prevMap:
                return [i, prevMap[diff]]
            prevMap[n]=i
        return []

"""
Time complexity:O(n) iterate in list once and O(1) lookup on dict
Space complexity: O(n) in worst case if need to store all in dict

Edge Cases Handled**
1. Multiple valid pairs: The problem guarantees exactly one solution, so no need to handle duplicates.
2. Negative numbers: The algorithm works for all integers, including negatives.
3. Empty or single-element input: Constraints ensure input is valid, so these edge cases don't arise here.
"""
