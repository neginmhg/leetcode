"""
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 10^5
-104 <= nums[i] <= 10^4
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's algorithm
        maxSum= float('-inf')
        curSum=0

        for n in nums:
            curSum+=n
            maxSum=max(curSum, maxSum)

            if curSum<0:
                curSum=0
        return maxSum
"""
Time Complexity
    O(n): The algorithm makes a single pass through the array, where 
    n is the number of elements in the input array. Each element is processed exactly once, leading to linear time complexity.

Space Complexity
    O(1): Kadane's Algorithm uses a constant amount of extra space. It only requires a few variables to keep track of the current sum and the maximum sum found so far, regardless of the size of the input array.
"""