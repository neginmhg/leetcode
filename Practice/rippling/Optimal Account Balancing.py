"""
You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

Return the minimum number of transactions required to settle the debt.

 

Example 1:

Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
Example 2:

Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.
 

Constraints:

1 <= transactions.length <= 8
transactions[i].length == 3
0 <= fromi, toi < 12
fromi != toi
1 <= amounti <= 100

"""

from typing import List
from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # Calculate net balances for each person
        balance = defaultdict(int)
        for from_id, to_id, amount in transactions:
            # Decrease balance for the giver
            balance[from_id] -= amount
            # Increase balance for the receiver
            balance[to_id] += amount
        
        # Filter out people with zero balance since they don't affect the problem
        debts = list(filter(lambda x: x != 0, balance.values()))
        
        # Helper function for backtracking
        def dfs(index):
            # Skip settled debts (zero balance)
            while index < len(debts) and debts[index] == 0:
                index += 1
            # If all debts are settled, return 0 transactions
            if index == len(debts):
                return 0
            
            min_transactions = float('inf')
            # Try pairing current debt with others
            for i in range(index + 1, len(debts)):
                # Skip if debts[i] is the same sign as debts[index] (both owe or are owed)
                if debts[i] * debts[index] < 0:
                    # Settle part of the debt between index and i
                    debts[i] += debts[index]
                    # Recurse for the next index
                    min_transactions = min(min_transactions, 1 + dfs(index + 1))
                    # Backtrack to restore the original debt
                    debts[i] -= debts[index]
            
            return min_transactions
        
        # Start backtracking with the first debt
        return dfs(0)
