"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
"""
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Two Secrets you need to solve the problem:
        # 1. LinkedList
        # 2. Floyd's algorithm

        # Step 1: Find the intersection point of the two pointers.
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]  # Move one step
            fast = nums[nums[fast]]  # Move two steps
            if slow == fast:
                break
        
        # Step 2: Find the entrance of the cycle.
        finder = nums[0]
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]
        
        return slow

# Example usage:
nums = [1, 3, 4, 2, 2]
sol = Solution()
print(sol.findDuplicate(nums))  # Output: 2
