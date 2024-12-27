"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2

        if nums1 <nums2:
            A,B = B,A
        
        total = len(A) + len(B)
        half = total//2
        
        l,r = 0, len(A)-1
        #binary search to find i which is middle of A
        while True:
            i =  (l+r)//2
            j = half -i-2

            #middle left and rights
            ALeft =     A[i]      if i>=0         else    float('-inf')
            ARight =    A[i+1]    if i+1 <len(A)  else    float('inf')      
            BLeft =     B[j]      if j>=0         else    float('-inf')
            BRight =    B[j+1]    if j+1<len(B)   else    float('inf') 

            #get of while loops
            if ALeft <= BRight and BLeft<= ARight:
                #calculate the median
                #odd 
                if total%2:
                    median = min(ARight, BRight)
                else :
                    median = (max(ALeft,BLeft) + min(BRight, ARight))/2
                return median
            elif ALeft>BRight:
                #move the partition to left
                r = i-1
            else:
                #move the partition to right
                l=i+1

    "time complexity:   O(log(min(m,n)))"