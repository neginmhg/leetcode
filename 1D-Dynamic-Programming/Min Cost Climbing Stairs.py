""""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""

from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #bottom up approach
        cost.append(0)   # [10,15,20]0
        for i in range(len(cost)-3, -1,-1):
            cost[i] = min(cost[i]+cost[i+1],cost[i]+cost[i+2])
        return min(cost[0],cost[1])

"""
Dynamic Programming (Bottom-Up): You are calculating the minimum cost to reach the top starting from the second-to-last step and moving backward to the beginning. This avoids redundant calculations and ensures that each step knows the optimal path to the top.

Efficient Space Usage: Instead of creating a separate DP table, the solution modifies the input array cost in place to store the minimum costs dynamically.

Time Complexity: The algorithm runs in O(n) time, where n is the number of steps (length of the cost array)."""