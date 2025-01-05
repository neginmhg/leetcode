"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Function to swap elements at indices i and j
        def swap(index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        # Get the length of the list
        size = len(nums)
      
        # Iterating through the list to place numbers on their correct positions
        for i in range(size):
            # Continuously swap the current element 
            #until it's in its correct position
            # or it's out of range [1, n]
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                swap(i, nums[i] - 1)
       
        # After placing each element in its correct position, or as correct as possible, 
        # traverse the list to find the first missing positive integer
        for i in range(size):
            # If the current number isn't the right number at index i, return i + 1,
            # because it is the first missing positive integer
            if i + 1 != nums[i]:
                return i + 1
              
        # If all previous positions contain the correct integers, 
        # then the first missing positive integer is n + 1 
        return size + 1
