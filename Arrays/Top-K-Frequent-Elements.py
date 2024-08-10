""" [MEDIUM]
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]"""


#solution= bucket sort
from typing import List
#[1,1,1,2,2,100]
# count bucket --> [0,1,2,3,4,5,6]
#value of 3 index is 1     (count of 1 is 3)
#value of 2 index is 2      (count of 2 is 2)
#value of 1 index is 100    (count of 100 is 1)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        "initialization"
        count={} #map each int
        freq=[[] for i in range(len(nums)+1)]     #[[], [], [], [], [], [], []]
        
        "populate map"
        #count each int and store in dict
        for n in nums:
            count[n]=count.get(n,0)+1            #{1: 3, 2: 2, 3: 1}
        
        "populate bucket"
        #turn dict into bucket sort
        for key, val in count.items():
            freq[val].append(key)#[[], [3], [2], [1], [], [], []]
        
        "retrive the last k items"
        #get the last k frequents
        result=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result

sol=Solution()
sol.topKFrequent([1,1,1,2,2,3],2)

"""
The line for n, c in count.items(): is a for loop that iterates over the items of the dictionary, where n represents the key and c represents the value."""