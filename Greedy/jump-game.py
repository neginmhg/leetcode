"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal= len(nums)-1       #final index
        for i in range(len(nums)-1, -1, -1):
            #if we can reach goal
            if i+nums[i]>= goal:
                goal=i      #update to new goal
        return True if goal==0 else False  #if goal was never updated or never reached 0 it means false

# Instantiate the Solution class
sol = Solution()

# Edge cases to test:
test_cases = [
    ([0], True),  # Single element array
    ([0, 0, 0], False),  # Array with all zeros
    ([10, 1, 1, 1, 1], True),  # Large jump at the beginning
    ([3, 2, 1, 0, 4], False),  # Unable to move past a zero
    ([2, 3, 1, 1, 4], True),  # Exact jumps to goal
    ([1, 2, 3, 0], True),  # Zero in the last index
    ([100000] + [1] * 100000, True),  # Large input size
    ([1, 1, 1, 1, 1], True),  # Array full of ones
    ([0, 1, 2, 3, 4], False),  # Zero at the start
    ([1, 0], True),  # Small jumps reaching the end
]

# Run the tests
for i, (input, output) in enumerate(test_cases):
    result = sol.canJump(input)
    print(f"Test case {i+1}: {'Passed' if result == output else 'Failed'}")
