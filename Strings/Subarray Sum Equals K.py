"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

"""

from typing import List

#https://www.youtube.com/watch?v=fFVZt-6sgyo
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0  # Initialize result to store the count of subarrays with sum equal to k
        curSum = 0  # Initialize current cumulative sum
        countSum = {0: 1}  # Dictionary to store the frequency of cumulative sums

        for num in nums:
            curSum += num  # Add the current number to the cumulative sum
            diff = curSum - k  # Calculate the difference needed to form a subarray sum equal to k

            # If the difference exists in the dictionary, it means there is a subarray
            # that ends at the current index with sum equal to k, so add its frequency to the result
            res += countSum.get(diff, 0)

            # Update the dictionary with the current cumulative sum
            # If curSum already exists in the dictionary, increment its count by 1
            # Otherwise, add curSum to the dictionary with an initial count of 1
            countSum[curSum] = 1 + countSum.get(curSum, 0)

        return res  # Return the total count of subarrays with sum equal to k
"""
This approach works by using a concept called "prefix sum." Let's break it down simply:

1. **Prefix Sum:** As you go through the array, you keep a running total of all the numbers you've seen so far (this is the `curSum`). This helps you know the sum of any subarray that ends at the current position.

2. **Finding Subarrays:** To find if there's a subarray that sums to `k`, you want to check if there's any previous subarray that, when removed from the current sum, leaves you with `k`. This is where the difference `curSum - k` comes in. If `curSum - k` was seen before, it means the part of the array between that previous sum and the current position adds up to `k`.

3. **Using a HashMap:** The hashmap (`countSum`) keeps track of how many times each prefix sum has appeared. If `curSum - k` is already in the hashmap, it means there's one or more subarrays that end at the current position and sum to `k`. You then add those to your result.

In simple terms, you're tracking all possible sums as you go through the array and checking if removing a previous sum gives you the target sum `k`. This way, you efficiently count all the subarrays that match your target without checking every possible subarray directly.
"""