class Solution:
    # Bottom-Up DP Approach
    # DP Array, Edge & Base Cases, Iterate, Return
    def botomUp(self, n: int) -> int:
        # Edge case
        if n == 0:
            return 0

        # 1. DP Initialization
        dp = [0] * (n + 1)
        
        # 2. DP Base Case
        dp[0] = 0
        dp[1] = 1

        # 3. Iteration (Bottom-Up DP)
        for i in range(2, n + 1):
            # 4. DP function
            dp[i] = dp[i - 1] + dp[i - 2]
        # Step 5: Return the final result
        return dp[n]

    # Top-Down DP Approach (Memoization)
    # Memo, DP (base, check memo, recursion fill memo) ,  start dp
    # 3 returns inside the DFS
    # 2 return outside to start DFS
    def topDown(self, n: int) -> int:
        # 1. Memoization table
        memo = {}

        # 2. DFS with memoization
        def dp(n: int) -> int:
            # 3. Base case
            if n == 0:
                return 0
            if n == 1:
                return 1

            # 4. Check memo, return if exists
            if n in memo:
                return memo[n]

            # 5. Recursion function to populate memo
            memo[n] = dp(n - 1) + dp(n - 2)

            return memo[n]
        # Step 6: Start recursion with initial value
        return dp(n)


"""
Time Complexity:
Both approaches have O(n) time complexity, because in the bottom-up approach, we process each state once, and in the top-down approach, each Fibonacci number is computed once and stored in the memo dictionary.


Space Complexity:
The bottom-up approach has O(n) space complexity due to the dp array storing the intermediate Fibonacci results.
The top-down approach has O(n) space complexity due to the recursion stack and the memo dictionary.

"""