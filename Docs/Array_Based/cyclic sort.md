**Cyclic Sort** is an in-place sorting algorithm specifically designed for situations where the elements in an array are in a known range, typically between `1` and `n` (where `n` is the length of the array). The goal is to place each element in its correct position without using extra space, by repeatedly swapping elements until each one is at its correct index.

### How It Works:
- **Ideal for arrays** where elements are expected to be within a specific range, such as `1` to `n`.
- Each element `nums[i]` should ideally be placed at index `nums[i] - 1`.
- **Steps**:
  1. Traverse the array and check if the element at index `i` is not in its correct position (i.e., `nums[i] != i + 1`).
  2. If it's not in the right place, swap it with the element that should be at that index.
  3. Repeat this process until all elements are in their correct positions.

### Example:
For an array `nums = [3, 1, 2]`, the correct positions should be:
- `1` should be at index `0`,
- `2` should be at index `1`,
- `3` should be at index `2`.

Using cyclic sort, we swap elements until all are in their correct positions.

### Key Characteristics:
- **Time Complexity**: O(n) because each element is moved at most once.
- **Space Complexity**: O(1) since it's an in-place algorithm.
```
def cyclicSort(nums):
    i = 0
    while i < len(nums):
        # Element is at the correct position, move to the next one
        if nums[i] == i + 1:
            i += 1
        else:
            # Swap the element to its correct position
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
    
    return nums
```
```
def firstMissingPositive(nums):
    # Perform cyclic sort to place elements in the correct position
    cyclicSort(nums)

    # After sorting, the first element not at its correct position will be the answer
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    
    # If all positions are correct, return len(nums) + 1
    return len(nums) + 1
```