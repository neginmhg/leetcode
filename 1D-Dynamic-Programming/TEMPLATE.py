from typing import List
class Solution:
    #Bottom-Up DP (Iterative)
    def dp_bottom_up(n):
        #edge case
        if n==0: 
            return 0
        dp = [0] * (n + 1) #use 2 vars instead if you can        
        # base case(s)
        dp[0] = 0 
        dp[1]=1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2] 
        
        return dp[n]
    
    #Top-Down DP (Recursive with Memoization)
    def dp_top_down(self, n: int) -> int:
        memo = {} 
        
        def dp(n: int) -> int:
            if n == 0:  # Base case(s)
                return 0
            if n == 1:  # Base case(s)
                return 1
            
            if n in memo:  # Return cached result if exists
                return memo[n]
            
            # Recurrence relation
            memo[n] = dp(n - 1) + dp(n - 2)
            return memo[n]  # Return the computed result
        
        return dp(n)
