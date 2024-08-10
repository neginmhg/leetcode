"""[HARD]
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
"""
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea =0
        stack = [] #pair of (index, height)
        for i,h in enumerate(heights):
            start =i 
            while stack and stack[-1][1] > h: #if previous h is bigger than current
                index, height= stack.pop()  #we don't want it
                maxArea= max(maxArea, height* (i-index)) #but keep the maxArea
                #since we popped the index lets update start with the index of current
                start=index
            stack.append((start,h))
        

        #once we go through all heights (reaching the end of list)
        # we still might have h left in stack
        #lets caculate their areas
        for i, h in stack:
            maxArea= max(maxArea, h*(len(heights)-i))
        return maxArea