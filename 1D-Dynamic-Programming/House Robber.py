"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have security 
systems connected and it will automatically contact the police if two adjacent 
houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
#Why is this DP?
#At its core, this problem is about making a sequence of 
# choices (to rob or not to rob a house) while adhering to a 
# constraint (no two adjacent houses can be robbed). The goal is to 
# maximize the total amount of money robbed.
#This is a classic Dynamic Programming (DP) problem because the 
# decision at each house depends on previous decisions, and we can 
# build the solution incrementally by solving smaller subproblems.
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Edge case: only one house
        if len(nums) == 1:
            return nums[0]
        
        #[rob1, rob2, n, n+1, ...]
        rob1, rob2 =0,0
        for n in nums:
            temp=max(n+rob1, rob2)
            rob1= rob2
            rob2=temp
        return rob2

#At any given house, you have two choices:
#Rob the current house, which means you cannot rob the previous one.
#Skip the current house and take whatever you have from the previous one.