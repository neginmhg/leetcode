"""
You are given an integer array nums. This array contains n elements, where exactly n - 2 elements are special numbers. One of the remaining two elements is the sum of these special numbers, and the other is an outlier.

An outlier is defined as a number that is neither one of the original special numbers nor the element representing the sum of those numbers.

Note that special numbers, the sum element, and the outlier must have distinct indices, but may share the same value.

Return the largest potential outlier in nums.

 

Example 1:

Input: nums = [2,3,5,10]

Output: 10

Explanation:

The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.

Example 2:

Input: nums = [-2,-1,-3,-6,4]

Output: 4

Explanation:

The special numbers could be -2, -1, and -3, thus making their sum -6 and the outlier 4.

Example 3:

Input: nums = [1,1,1,1,1,5,5]

Output: 5

Explanation:

The special numbers could be 1, 1, 1, 1, and 1, thus making their sum 5 and the other 5 as the outlier.

 

Constraints:

3 <= nums.length <= 105
-1000 <= nums[i] <= 1000
The input is generated such that at least one potential outlier exists in nums.
"""
from typing import List, Counter
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        #sum(n-2 items) + special number +outlier =total
        #lets call sum(n-2 items) + special number = 2S
        #so 2S + outlier = total
        # S = (total-outlier)/2

        #create a map frequency 
        total =sum(nums)
        numsFreq = Counter(nums)
        result = float('-inf')
        for outlier in nums:            
            #if S can be formed that means the outlier can  be the final answer
            if (total-outlier)%2 ==0:
                #reduce count of outlier temporarily
                numsFreq[outlier]-=1
                #Calculate S
                S = (total-outlier)//2
                if numsFreq[S]>0:
                    result = max(result, outlier)           
                #put the freq back for the next loop 
                numsFreq[outlier]+=1
        return result
    
s = Solution()
outlier=s.getLargestOutlier([2,3,5,10])

print(outlier)

