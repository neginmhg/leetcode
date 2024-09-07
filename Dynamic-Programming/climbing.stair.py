"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""
#using Space Optimization
#BOTTOM-UP (iterative)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
    
        # Initialize the base cases
        prev2, prev1 = 1, 1
        
        # Iterate and update variables
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current
        
        return prev1
    
    
    # Example usage
    print(climbStairs(5))  # Output: 8