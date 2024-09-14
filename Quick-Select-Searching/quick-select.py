"""
1. choose a pivot
2. partition into 2 parts
3. determine position: compare position at pivot with kth position
    - if pivot=kth position then return
    - if pivot>kth position then recursivelly search left
    - if pivot<kth posistion then recursively search right
"""
from typing import List
class Solution:
    def search(self, nums:List[int], k:int)-> int:
        targetIndex=len(nums)-k
        quickSelect(0, len(nums)-1)
        def quickSelect(nums,l,r):
            pivot=nums[r]
            pointer=l
