"""

You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

The first n elements belonging to the first part and their sum is sumfirst.
The next n elements belonging to the second part and their sum is sumsecond.
The difference in sums of the two parts is denoted as sumfirst - sumsecond.

For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.

 

Example 1:

Input: nums = [3,1,2]
Output: -1
Explanation: Here, nums has 3 elements, so n = 1. 
Thus we have to remove 1 element from nums and divide the array into two equal parts.
- If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
- If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
- If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
The minimum difference between sums of the two parts is min(-1,1,2) = -1. 
Example 2:

Input: nums = [7,9,5,8,1,3]
Output: 1
Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
It can be shown that it is not possible to obtain a difference smaller than 1.
 

Constraints:

nums.length == 3 * n
1 <= n <= 105
1 <= nums[i] <= 105
"""

from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total_elements = len(nums)
        one_third_length = total_elements // 3  # Calculate the size of one-third of the array
        
        # Initialize variables for prefix sum and heap
        prefix_sum = 0
        max_heap_prefix = []  # Max-heap to keep track of the largest 'n' elements in the prefix
        prefix_sums = [0] * (total_elements + 1)  # Initialize prefix sum array
        
        # Calculate prefix sums and maintain the heap with the largest 'n' elements
        for i in range(1, one_third_length * 2 + 1):
            prefix_sum += nums[i - 1]
            heappush(max_heap_prefix, -nums[i - 1])  # Push negated values to simulate a max-heap
            if len(max_heap_prefix) > one_third_length:
                prefix_sum += heappop(max_heap_prefix)  # Remove the smallest (most negative) element when heap size exceeds 'n'
            prefix_sums[i] = prefix_sum
        
        # Initialize variables for suffix sum and heap
        suffix_sum = 0
        min_heap_suffix = []  # Min-heap to keep track of the smallest 'n' elements in the suffix
        suffix_sums = [0] * (total_elements + 1)  # Initialize suffix sum array
        
        # Calculate suffix sums and maintain the heap with the smallest 'n' elements
        for i in range(total_elements, one_third_length - 1, -1):
            suffix_sum += nums[i - 1]
            heappush(min_heap_suffix, nums[i - 1])  # Push values to simulate a min-heap
            if len(min_heap_suffix) > one_third_length:
                suffix_sum -= heappop(min_heap_suffix)  # Remove the largest element when heap size exceeds 'n'
            suffix_sums[i] = suffix_sum
        
        # Find the minimum difference between the prefix and suffix sums
        min_difference = float('inf')  # Start with an infinitely large difference
        for i in range(one_third_length, one_third_length * 2 + 1):
            min_difference = min(min_difference, prefix_sums[i] - suffix_sums[i + 1])  # Compare and store the minimum
        
        return min_difference
