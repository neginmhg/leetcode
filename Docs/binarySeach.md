# Binary Search Guide

## Concept

<div style="font-size:25px;">

Binary search is an efficient algorithm to find a target value within a sorted array. It works by repeatedly dividing the search interval in half:

1. **Initialize Pointers**: `left` at index 0 and `right` at index `n-1`.
2. **Calculate Midpoint**: `mid = left + (right - left) // 2`.
3. **Compare and Adjust**:
   - If `arr[mid]` equals the target, return `mid`.
   - If `arr[mid]` is greater than the target, move `right` to `mid - 1`.
   - If `arr[mid]` is less than the target, move `left` to `mid + 1`.
4. **Repeat** until `left` exceeds `right`.

## When to Use Binary Search

Binary search is most effective when:

1. **The Array is Sorted**: The fundamental requirement for binary search is that the array (or list) must be sorted. Without this, binary search cannot be applied.
2. **Constant Time Lookups Are Needed**: If you frequently need to perform lookups in a sorted dataset, binary search is a good choice due to its logarithmic time complexity.
3. **Finding Specific Boundaries**: It’s useful for problems requiring finding the lower or upper bound of a target element, or the insertion point for a target.
4. **Monotonic Functions**: Problems where a function's value increases or decreases monotonically (either always increasing or always decreasing) are suitable for binary search.

## Binary Search Template

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found
```

## LeetCode Problems and Solutions

### 1. Search Insert Position

**Problem**: Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if inserted in order.

**Solution**:

```python
def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Example usage
nums = [1, 3, 5, 6]
target = 5
print(search_insert_position(nums, target))  # Output: 2
```

### 2. Find Minimum in Rotated Sorted Array

**Problem**: Find the minimum element in a rotated sorted array.
**Solution**:

```python
def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# Example usage
nums = [4, 5, 6, 7, 0, 1, 2]
print(find_min(nums))  # Output: 0



```

### 3.Peak Element

**Problem**:Find a peak element in an array where a peak element is greater than its neighbors.

**Solution**:

```python

def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

# Example usage
nums = [1, 2, 3, 1]
print(find_peak_element(nums))  # Output: 2 (index of peak element 3)


```

## Additional Tips

### Lower and Upper Bound

- Lower Bound: First position where the target can be inserted.
- Upper Bound: Last position where the target can be inserted.

## Lower Bound:

```python

def lower_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Example usage
nums = [1, 2, 2, 2, 3]
target = 2
print(lower_bound(nums, target))  # Output: 1


```

## Upper Bound:

```python
def upper_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right

# Example usage
nums = [1, 2, 2, 2, 3]
target = 2
print(upper_bound(nums, target))  # Output: 3

```

</div>
