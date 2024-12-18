class Solution:
    def two_pointer(self, nums, target):
        # Initialize two pointers
        left, right = 0, len(nums) - 1

        # Iterate while left pointer is less than the right pointer
        while left < right:
            # Perform your logic here
            value = nums[left] + nums[right]

            if value == target:  # Condition to check if the target is met
                # Return the indices of the two numbers
                return [left, right]
            elif value < target:
                # Move the left pointer to increase the sum
                left += 1
            else:
                # Move the right pointer to decrease the sum
                right -= 1

        # If no valid result is found, return some default value
        return -1
