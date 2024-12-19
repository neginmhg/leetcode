"""
The "Camping Problem" is a classic algorithmic challenge that involves determining the maximum number of non-overlapping intervals, or "campsites," that can be scheduled given a set of intervals. Each interval represents the start and end times of a campsite, and the objective is to find the maximum number of campsites that can be scheduled without any overlap.

Problem Statement:

You are given a list of intervals, where each interval represents the start and end times of a campsite. Your task is to determine the maximum number of non-overlapping campsites that can be scheduled.

Example:

Consider the following list of intervals:
[[1, 3], [2, 4], [3, 5], [4, 6]]
In this example:

The first campsite starts at time 1 and ends at time 3.
The second campsite starts at time 2 and ends at time 4.
The third campsite starts at time 3 and ends at time 5.
The fourth campsite starts at time 4 and ends at time 6.
The maximum number of non-overlapping campsites that can be scheduled is 2, which can be achieved by selecting the first and fourth campsites.

Approach:

This problem can be efficiently solved using a greedy algorithm. The key idea is to:

Sort the intervals based on their end times.
Iterate through the sorted intervals and select each interval that starts after the last selected interval ends.
Count the number of selected intervals.




"""


from typing import List

class Solution:
    def maxCampsites(intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals based on end times
        intervals.sort(key=lambda x: x[1])

        # Step 2: Initialize variables
        count = 0
        last_end_time = float('-inf')

        # Step 3: Iterate through sorted intervals
        for start, end in intervals:
            if start >= last_end_time:
                count += 1
                last_end_time = end

        return count
    
    
#Time Complexity: The time complexity is O(n log n), where n 
# is the number of intervals. This is due to the sorting step.
#  The subsequent iteration through the intervals takes O(n) time.


#Space Complexity: The space complexity is O(1) if the sorting
#  is done in-place. If additional space is used for sorting, 
# the space complexity would be O(n).