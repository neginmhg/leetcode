"""
1. choose a pivot
2. partition into 2 parts
3. determine position: compare position at pivot with kth position
    - if pivot=kth position then return
    - if pivot>kth position then recursivelly search left
    - if pivot<kth posistion then recursively search right
"""
from random import randint

def quickselect(nums, k):
    """
    Find the kth smallest element in an unsorted list.
    """
    def partition(start, end, pivot_idx):
        pivot_value = nums[pivot_idx]
        # Move pivot to the end
        nums[pivot_idx], nums[end] = nums[end], nums[pivot_idx]
        smaller_idx = start

        # Move smaller elements to the left
        for i in range(start, end):
            if nums[i] < pivot_value:
                nums[smaller_idx], nums[i] = nums[i], nums[smaller_idx]
                smaller_idx += 1
        
        # Move pivot to its final position
        nums[end], nums[smaller_idx] = nums[smaller_idx], nums[end]
        return smaller_idx

    def select(start, end, target_idx):
        """
        Recursively find the kth smallest element.
        """
        if start == end:
            return nums[start]

        # Choose a random pivot
        pivot_idx = randint(start, end)
        pivot_idx = partition(start, end, pivot_idx)

        # Check the pivot's position
        if target_idx == pivot_idx:
            return nums[target_idx]
        elif target_idx < pivot_idx:
            return select(start, pivot_idx - 1, target_idx)
        else:
            return select(pivot_idx + 1, end, target_idx)

    # k is 1-based; convert to 0-based index
    return select(0, len(nums) - 1, k - 1)

