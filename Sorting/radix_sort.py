"""
Radix Sort is an integer sorting algorithm that processes digits of numbers from the least significant digit to the most significant digit (LSD).

Radix Sort:

Sorts numbers digit by digit, from the least significant digit to the most significant digit.
Uses Counting Sort as a subroutine to sort based on each digit's place value.
"""

def countingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count array to contain the position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to arr
    for i in range(n):
        arr[i] = output[i]

def radixSort(arr):
    # Find the maximum number to know the number of digits
    max_val = max(arr)
    
    # Apply counting sort to sort elements based on place value
    exp = 1
    while max_val // exp > 0:
        countingSort(arr, exp)
        exp *= 10

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
print("Sorted array:", arr)
