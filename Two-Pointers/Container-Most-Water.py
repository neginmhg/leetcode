"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result=0
        l,r=0, len(height)-1 #set your pointers
        while l<r:
            area=(r-l)*min(height[l],height[r])
            result=max(area, result)
            if height[l] < height[r]:
                l+=1
            elif height[l] > height[r]:
                r-=1
            else:
                l+=1 #or r-=1 , doesn't matter just move a pointer

        return result

s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))