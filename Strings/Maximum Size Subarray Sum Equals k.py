"""
Given an integer array `nums` and an integer `k`, you need to find the maximum length of a subarray that sums to `k`.

Example 1:
```
Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3, and has a length of 4.
```

Example 2:
```
Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1, and has a length of 2.
```

Constraints:
- The length of `nums` will be between `1` and `10^5`.
- The elements of `nums` will be between `-10^4` and `10^4`.
- The value of `k` will be between `-10^4` and `10^4`.
"""
from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Initialize variables
        max_length = 0  # To store the maximum length of subarray found
        cur_sum = 0  # Current cumulative sum
        index_map = {0: -1}  # Map to store the first occurrence index of each cumulative sum

        # Iterate through the list
        for i, num in enumerate(nums):
            cur_sum += num  # Update the cumulative sum

            # Check if the current cumulative sum minus k has been seen before
            diff = cur_sum - k
            if (diff) in index_map:
                # Calculate the length of the subarray
                length = i - index_map[diff]
                # Update the maximum length found
                max_length = max(max_length, length)

            # Update the index_map with the current cumulative sum if it's not already present
            if cur_sum not in index_map:
                index_map[cur_sum] = i

        return max_length
