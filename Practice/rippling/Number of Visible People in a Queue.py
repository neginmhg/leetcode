"""
There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.

 

Example 1:



Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]
Explanation:
Person 0 can see person 1, 2, and 4.
Person 1 can see person 2.
Person 2 can see person 3 and 4.
Person 3 can see person 4.
Person 4 can see person 5.
Person 5 can see no one since nobody is to the right of them.
Example 2:

Input: heights = [5,1,2,3,10]
Output: [4,1,1,1,0]
 

Constraints:

n == heights.length
1 <= n <= 105
1 <= heights[i] <= 105
All the values of heights are unique.
"""
#Key Observations:
    #A person can see another only if there is a monotonically decreasing sequence of heights between them. Once a taller person appears, it blocks the visibility for others beyond them.
from typing import List
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # Monotonic stack to keep track of visible persons
        stack = []
        # Result array initialized to zeros
        result = [0] * len(heights)
        
        # Traverse the heights array from right to left
        for i in range(len(heights) - 1, -1, -1):
            # Count the number of people visible to the right
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()  # Pop shorter people who are visible
                count += 1  # Increment visible count
            
            # If there's still a taller or equal person on the stack,
            # they are also visible but block further visibility.
            if stack:
                count += 1
            
            # Update the result for the current person
            result[i] = count
            
            # Push the current person onto the stack
            stack.append(heights[i])
        
        return result
"""
1. Stack: Keeps track of the heights of people to the right of the current person. It helps us determine visibility efficiently.


2. Why right to left?
This allows us to efficiently process the visibility of people to the right of each person, as the stack will contain only the heights of people to their right.


3. For each person at index i:

Count how many shorter people are visible:
While the stack is not empty, and the top of the stack is shorter than the current person, pop from the stack. Each person popped is visible to the current person.
Increment count for each person popped.
Check for taller people:
If the stack is not empty after the loop, the person at the top of the stack is taller and blocks further visibility. However, this person is also visible to the current person, so we increment count by 1.



4. Update Results

Store the count for the current person in the result array.

5. Push the Current Person

Add the current person's height to the stack. This ensures the stack always represents the people visible to the right of the next person being processed.

"""