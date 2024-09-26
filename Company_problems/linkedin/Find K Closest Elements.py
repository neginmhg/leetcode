"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]

 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize two pointers for binary search window
        left, right = 0, len(arr) - 1
        
        # We will keep shrinking the window size to k closest elements
        while right - left >= k:
            # Check which side is farther from x and shrink the farther side
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1  # Shrink from the left
            else:
                right -= 1  # Shrink from the right
                
        # Now the window from left to right contains k elements closest to x
        return arr[left:right + 1]
    
    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        # Perform binary search on the window of size k
        left, right = 0, len(arr) - k
        
        # Binary search to find the correct left boundary for the k closest elements
        while left < right:
            mid = (left + right) // 2
            
            # Compare the distances between arr[mid] and arr[mid + k] to x
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1  # Move right
            else:
                right = mid  # Move left
        
        # The window starting at 'left' has the k closest elements
        return arr[left:left + k]
    
"""
1. Two-pointer Shrinking Window Approach:
Time Complexity: 
O(n−k)
The two-pointer approach involves iterating over the array to shrink the window from both ends. This happens until the window size becomes exactly k.
In the worst case, we might have to shrink the window from both sides until we've reduced the array by n - k elements, leading to a complexity of O(n−k).
Best Use Case: This approach is efficient when n (the size of the array) and k (the number of elements to return) are relatively small and close to each other (e.g., k≈n). For cases where 
k is large relative to 
n, the two-pointer approach can be acceptable.




2. Binary Search Approach:
Time Complexity: 
O(logn+k)
Binary search is used to find the starting index of the k closest elements, which takes

O(logn) time. After finding the starting point, extracting the subarray of k elements takes 
O(k).
Best Use Case: This approach is more efficient when k is much smaller than n (e.g., when you're only looking for a small window within a very large array). It takes advantage of the sorted property of the array and reduces the initial search space to a logarithmic time complexity.
Efficiency Comparison:
Binary Search Approach (O(logn+k)) is more efficient when:
The array is large (n is big), and you need to find only a few elements (k is small relative to n).
The complexity reduces drastically when you need only a small portion of the array, as the binary search quickly narrows down the search space in logarithmic time.

- Binary Search Approach is generally more efficient in most practical scenarios, especially when the input size is large.
- For smaller inputs or cases where k is close to n, both approaches perform similarly, but the two-pointer approach might be slightly simpler in implementation.
"""