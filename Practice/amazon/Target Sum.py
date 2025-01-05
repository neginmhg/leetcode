"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""
from typing import List
class Solution:
    #Dynamic Programming (Top-Down)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #cache dict to store (index,total):#ways to target
        dp = {}
        def backtrack(i, t):
            #base case: reach end of list
            if i ==len(nums):
                return 1 if t==target else 0
            #base case: if (index,total) already in DP
            #The value for each key is the number of ways to 
            #reach the target from that index with that sum.
            if (i,t) in dp:
                return dp[(i,t)]
            
            #Recursive function
            dp[(i,t)] = backtrack(i+1, t + nums[i]) 
            + backtrack(i+1, t -nums[i])

            return dp[(i,t)]
        
        return backtrack(0,0)
    
""" 
t sum of all elements in array and n is length of list
Time complexity: O(n*t)
Space complexity: O(n*t)
"""