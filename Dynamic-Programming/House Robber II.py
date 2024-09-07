"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3

"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return(max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1])))
    def helper(self,nums):
        rob1, rob2 =0,0
        for n in nums:
            temp=max(n+rob1, rob2)
            rob1= rob2
            rob2=temp
        return rob2
"Special Case (Single House): If there is only one house (i.e., nums = [x]), then the answer is simply nums[0]. In this case, nums[1:] and nums[:-1] would result in empty lists, so the helper function would return 0. Including nums[0] ensures that if there's only one house, the solution still works correctly by returning the money in that house."
#To handle this, you break the problem into two scenarios:
#Rob houses excluding the first house.
#Rob houses excluding the last house.

"""Why Two Helper Calls?
Since the houses are arranged in a circle, robbing the first house prevents you from robbing the last house, and robbing the last house prevents you from robbing the first house. So, you split the problem into two subproblems:
Excluding the first house: This is handled by self.helper(nums[1:]).
Excluding the last house: This is handled by self.helper(nums[:-1]).
The final solution is the maximum of the three cases:

Rob only the first house.
Rob all houses except the first.
Rob all houses except the last."""