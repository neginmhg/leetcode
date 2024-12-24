"""[HARD]
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""
import collections
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        q=collections.deque()
        l=r=0
        while r<len(nums):
            #pop smaller values from queue
            """
            This while loop ensures that the deque q maintains a decreasing order of elements. It iterates as long as q is not empty (q) and the last element in q (nums[q[-1]]) is smaller than the current element nums[r]. In that case, it removes elements from the right end of q until this condition is met. Then, it appends the current index r to q."""
            while q and nums[q[-1]]< nums[r]:
                q.pop()
            q.append(r)


            #remove left value from window
            if l>q[0]:
                q.popleft()
            
            if r+1 >=k:
                output.append(nums[q[0]])
                l+1
            r+=1
        return output

    def heap_maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
    
        # Max heap, Python's heapq is a min-heap by default so we negate the values
        max_heap = []
        result = []
        
        for i in range(len(nums)):
            # Add the current element to the heap (negate the value for max-heap behavior)
            heapq.heappush(max_heap, (-nums[i], i))
            
            # Remove elements that are out of the current window
            while max_heap[0][1] < i - k + 1:
                heapq.heappop(max_heap)
            
            # Once we have a window, append the max (negate the value back)
            if i >= k - 1:
                result.append(-max_heap[0][0])
        
        return result