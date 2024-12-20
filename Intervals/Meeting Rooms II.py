"""

You are given a list of employee working hours, where each employee's working hours are represented as a list of intervals. Each interval consists of a start time and an end time. Your task is to find the free time slots between the employees' working hours that can be used for scheduling a meeting.

Example:

Input:

schedules = [
    [[1, 3], [6, 7]], 
    [[2, 4]], 
    [[2, 5], [9, 12]]
]
Output:

[[5, 6], [7, 9]]
Explanation:

The employees' busy times are [1, 3], [2, 4], [2, 5], [6, 7], [9, 12].
The merged busy times are [1, 5], [6, 7], and [9, 12].
The gaps (free time) between the busy times are:
[5, 6] (after 5 and before 6).
[7, 9] (after 7 and before 9).
"""


from typing import List

class Solution:
    def find_free_time(schedules: List[List[List[int]]]) -> List[List[int]]:
        # 3D->2D Flatten all intervals into a single list
        intervals = [interval for employee in schedules for interval in employee]
    
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        # Merge intervals to get the busy schedule
        merged = []
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        
        # Find gaps (free time)
        free_time = []
        #start from second interval compare its start to the previous's end
        for i in range(1, len(merged)):
            prev_end = merged[i - 1][1]
            curr_start = merged[i][0]
            if prev_end < curr_start:
                free_time.append([prev_end, curr_start])
        
        return free_time

