"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

"""
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]
    
    
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # Calculate the target index for the kth largest element in a sorted array
        targetIndex = len(nums) - k

        # Define the quick select function to partition the array and find the target index
        def quickSelect(l, r):
            pivot = nums[r]  # Choose the rightmost element as the pivot
            pointer = l  # Initialize pointer at the leftmost element
            
            # Partition the array such that elements <= pivot are on the left and > pivot on the right
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer]  # Swap elements to partition
                    pointer += 1  # Move pointer to the right
            
            # Swap the pivot element to its correct position
            nums[pointer], nums[r] = nums[r], nums[pointer]

            # Recursively apply quick select to the appropriate partition
            if pointer > targetIndex:  # If pointer is greater, search the left partition
                return quickSelect(l, pointer - 1)
            elif pointer < targetIndex:  # If pointer is lesser, search the right partition
                return quickSelect(pointer + 1, r)
            else:  # If pointer is equal to the target index, return the element at pointer
                return nums[pointer]

        # Initiate quick select from the start to end of the array
        return quickSelect(0, len(nums) - 1)

    
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        # start with heap of size k
        heap = nums[:k]
        heapq.heapify(heap)  # O(k)
        
        # Iterate over the remaining elements in the array
        for num in nums[k:]:
            if num > heap[0]:  # Compare with the smallest element in the heap (root)
                heapq.heappushpop(heap, num)  # Push the new big element and pop the smallest
        
        # The root of the heap is the k-th largest element
        return heap[0]
    """
    This should help you remember:
    1. Start with a heap of size `k`.
    2. Sweep through the array, comparing elements with the smallest (root of the heap).
    3. If its bigger, replace the root.
    4. At the end, the root is the k-th largest element!
    """ 