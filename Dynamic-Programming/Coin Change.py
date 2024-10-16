"""
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.
Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.
You may assume that you have an unlimited number of each coin.

Example 1:
Input: coins = [1,5,10], amount = 12
Output: 3
Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

Example 2:
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount of 3 cannot be made up with coins of 2.

Example 3:
Input: coins = [1], amount = 0
Output: 0
Explanation: Choosing 0 coins is a valid way to make up 0.

Constraints:

1 <= coins.length <= 10
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10000

"""

#brute force: DFS/backtracking
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #bottom up start from 0
        dp = [float('inf')]* (amount+1)
        dp[0]=0

        for a in range(1, amount+1):
            for c in coins:
                if a-c >=0:
                    dp[a] = min(dp[a], dp[a-c] +1 )
        
        return dp[amount] if dp[amount]!= float('inf') else -1
    
solution=Solution()
coins = [1,5,10]
amount = 12
print(solution.coinChange(coins, amount))