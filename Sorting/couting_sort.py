"""Counting Sort is a non-comparison-based sorting algorithm that works by counting occurrences of each unique element.

Counting Sort:

Counts the frequency of each element within a given range.
Builds the sorted array based on these counts.
Efficient for a range of integer values and where the maximum value is not excessively large relative to the array size.


"""

def countingSort(arr):
    if not arr:
        return arr

    # Find the maximum and minimum values
    max_val = max(arr)
    min_val = min(arr)
    
    # Create count array with range from min_val to max_val
    range_size = max_val - min_val + 1
    count = [0] * range_size
    
    # Count the occurrences of each value
    for num in arr:
        count[num - min_val] += 1

    # Build the sorted output array
    output = []
    for i in range(range_size):
        output.extend([i + min_val] * count[i])
    
    return output

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = countingSort(arr)
print("Sorted array:", sorted_arr)
