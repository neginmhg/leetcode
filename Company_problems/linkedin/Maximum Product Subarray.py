"""
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def maxProduct(self,nums):
        if not nums:
            return 0
        
        max_product = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        for num in nums[1:]:
            # If num is negative, swap current_max and current_min
            if num < 0:
                current_max, current_min = current_min, current_max

            # Calculate current maximum and minimum products
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            # Update the overall max product
            max_product = max(max_product, current_max)

        return max_product
        