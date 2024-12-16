"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""
#Two-pass Binary Search:
    #First Pass: Locate the first occurrence of the target.
    #Second Pass: Locate the last occurrence of the target.
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findPosition(isFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            pos = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    pos = mid  # Record the position
                    if isFirst:
                        right = mid - 1  # Narrow the search to the left half
                    else:
                        left = mid + 1   # Narrow the search to the right half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return pos
        
        # Binary search for the first and last positions
        firstPos = findPosition(True)
        
        # If the first occurrence is not found, the target is not in the array
        if firstPos == -1:
            return [-1, -1]
        
        lastPos = findPosition(False)
        
        return [firstPos, lastPos]

# Example usage:
sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))  # Output: [3, 4]
print(sol.searchRange([5,7,7,8,8,10], 6))  # Output: [-1, -1]
print(sol.searchRange([], 0))               # Output: [-1, -1]
