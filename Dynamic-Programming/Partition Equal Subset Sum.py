"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of 
the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

"""
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # If the total sum is odd, we can't partition it into two equal subsets
        if sum(nums) % 2:
            return False
        
        # Target sum for each subset
        target = sum(nums) // 2
        
        # A set to track possible sums we can form
        dp = {0}
        
        # Iterate over each number in the array
        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()
            
            # Check each sum that we have in dp so far
            for t in dp:
                if (t + nums[i]) == target:
                    return True  # We've found a subset that sums to the target
                
                nextDp.add(t + nums[i])  # Add the current number to the sum
                nextDp.add(t)            # Exclude the current number
                
            dp = nextDp  # Move to the next set of possible sums
        
        # After the loop, check if we can form the target sum
        return True if target in dp else False
