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
        # Ensure nums1 is the smaller array             
        #time complexity:   O(log(min(m,n)))
        #space: O(1)
        #Make sure nums1 is the smaller one
        total = len(nums1)+len(nums2)
        half = total//2
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        
        #Focus on the small one : nums1
        # put l and r on the small one
        l,r =0, len(nums1)-1

        #2pointer while
        while True:
            #Find middle for nums1 and nums2:
            #Middle of nums1 --> i
            i = (r+l)//2
            #Middle of nums2 --> j
            j = half-i -2

            #Middle left and middle right 
            left1 = nums1[i] if i>=0 else float('-inf')
            right1 = nums1[i+1] if (i+1)<len(nums1) else float('inf')


            left2= nums2[j] if j>=0 else float('-inf')
            right2=nums2[j+1] if (j+1)<len(nums2) else float('inf')

            #If we found the correct middles i and j
            if left1<=right2 and left2<=right1:
                if total%2:
                    return min(right1,right2)
                else:
                    # If even total length, return the average of the two medians
                    return (max(left1,left2) + min(right1,right2))/2
                
            elif(left1>right2):
                #if right too big move it left
                r =i-1
            else:
                l=i+1