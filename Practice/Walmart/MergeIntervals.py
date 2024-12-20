"""
Given an array of intervals where 
intervals[i] = [starti, endi], 
merge all overlapping intervals, 
and return an array of the non-overlapping 
intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] 
overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considere
 overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Sort intervals by Start point
        intervals.sort(key=lambda i: i[0])  # Step 1
        
        #2. Output result which is a list of lists
        output = [intervals[0]]  # Step 2

        #3. Loop through intervals and merge
        for interval in intervals[1:]:  # Step 3
            start, end = interval[0], interval[1]
            lastEnd = output[-1][1]
            if start <= lastEnd:
                # Overlap: update last interval
                output[-1][1] = max(lastEnd, end)
            else:
                # No overlap
                # Just add to output as new interval
                output.append([start, end])
                
        return output  # Step 4

#Total Time Complexity: O(n log n)
    #   Sorting: O(n log n)
    #   Looping through the intervals: O(n)
    #   Other operations: O(1)
#Space Complexity is O(n) due to output list of list