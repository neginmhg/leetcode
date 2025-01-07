""" [HARD]
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

"""
from typing import List
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums:List[int], k:int)->int:
        freq = defaultdict(int)
        res =0
        l_far =0
        l_near=0
        for r in range(len(nums)):
            freq[nums[r]]+=1

            #while more than k distinct
            #move left near to right
            while len(freq)>k:
                freq[nums[l_near]]-=1
                if freq[nums[l_near]]==0:
                    del freq[nums[l_near]]
                l_near+=1
                l_far=l_near

            #if we have extra of nums[l_near]
            #we can afford to lose it 
            while freq[nums[l_near]]>1:
                freq[nums[l_near]]-=1
                l_near+=1

            #found distint numbers in window
            if len(freq)==k:
                res += l_near-l_far+1
        return res
            

#both space and time : O(n)
"""
l_near to r:
    This is the tightest valid window containing exactly k distinct integers.
    By incrementing l_near, we ensure that there are no unnecessary duplicates of the leftmost element in the window.
l_far to r:
    This is the widest valid window containing exactly k distinct integers.
    l_far stays as far left as possible while still maintaining the condition of exactly k distinct integers.        
"""