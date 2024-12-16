""""
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
 

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
"""
from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if total % k:
            return False
        target = total//k
        used=[False]*len(nums)
        nums.sort(reverse=True)

        def backtrack(i, k, subsetSum):
            if k==0:
                return True
            if subsetSum==target:
                return backtrack(0, k-1,0)
            for j in range(i, len(nums)):
                if used[j] or subsetSum+nums[j]>target:
                    continue
                used[j]=True
                if backtrack(j+1, k, subsetSum+nums[j]):
                    return True
                used[j] =False
            return False
        return backtrack(0, k, 0)



    def canPartitionKSubsets2(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if total % k:
            return False
        target = total//k
        subsets=[0]*k
        nums.sort(reverse=True)

        def bt(i):
            if i==len(nums):
                return True
            num = nums[i]
            for j in range(k):
                if subsets[j] + num <= target:  # Check if we can add to subset
                    subsets[j] += num  # Add number to the subset
                    if bt(i + 1):  # Recur for the next number
                        return True
                    subsets[j] -= num  # Backtrack (remove number)

                # Important to avoid TLE
                if subsets[j] == 0:
                    break
            
            return False
        return bt(0)
"""
Add a number to a subset to see if we can form valid partitions.
Try the next number in the list recursively, checking if adding this number helps us achieve the goal.
If it works, we’re done! But if it doesn’t, we remove that number and try placing it in a different subset, allowing us to explore all possible configurations."""


""""
def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if total % k:
            return False
        target = total//k
        subsets=[0]*k
        nums.sort(reverse=True)

        def bt(i):
            if i==len(nums):
                return True
            num = nums[i]
            for j in range(k):
                if subsets[j] + num <= target:  # Check if we can add to subset
                    subsets[j] += num  # Add number to the subset
                    if bt(i + 1):  # Recur for the next number
                        return True
                    subsets[j] -= num  # Backtrack (remove number)

                # Important to avoid TLE
                if subsets[j] == 0:
                    break
            
            return False
        return bt(0)
"""