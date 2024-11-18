from typing import List
class Solution:
    def solveProblem(self, data: List[int]) -> int:
        # Step 1: Handle base cases
        if not data:
            return 0
        if len(data) == 1:
            return data[0]

        # Step 2: Initialize DP variables (or array for memoization)
        # These track the optimal solution for subproblems
        dp = [0] * len(data)  # This can also be optimized to two variables for space optimization

        # Step 3: Set initial conditions (base cases)
        dp[0] = data[0]
        dp[1] = data[1] if len(data) > 1 else data[0]  # Example for 2 base cases

        # Step 4: Iterate through the array or state space
        for i in range(2, len(data)):
            # Transition function: Solve the subproblems
            dp[i] = min(dp[i - 1], dp[i - 2]) + data[i]  # Change 'min' and transition as per the problem

        # Step 5: Return the final solution (usually the last element of the dp array)
        return min(dp[-1], dp[-2])  # Depending on whether the final state is at dp[-1] or another state

# Example usage
# solver = Solution()
# print(solver.solveProblem([10, 15, 20]))  # Output depends on the problem specifics
