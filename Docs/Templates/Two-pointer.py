class Solution:
    def two_pointer(self, nums, target):
        # 1. L to 0, R to len-1
        left, right = 0, len(nums) - 1

        # 2. while l<r
        while left < right:
            # Logic and update left and right 
            value = nums[left] + nums[right]

            if value == target: 
                return [left, right]
            elif value < target:
                left += 1
            else:
                right -= 1

        # If no valid result is found, return some default value
        return -1
