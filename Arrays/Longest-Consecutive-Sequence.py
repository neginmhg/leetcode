"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


from typing import List

# Solve this question without SROTING: since sorting has nlogn complexity 
# therefore it's not the most optimal solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #turn the list into set to get rid of dups
        numsSet=set(nums)
        longest=0
        for n in numsSet:
            if n-1 not in numsSet: # *** it will only process the starting numbers meaning 0 and 15
                length=0
                while n+length in numsSet:
                    length+=1
                longest=max(length,longest)
        return longest

s=Solution()
print(s.longestConsecutive([9,3,7,2,5,8,0,15,16,17,18,19,20,3,4,6,0,1])) #complexity O(n) jus because of line that I put *** in.