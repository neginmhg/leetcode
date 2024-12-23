"""
Problem Statement: Faulty Server Detection
Some developers want to deploy their application on different servers with a load balancer in the front. There are n servers to choose from, where the number of requests that can be handled by the i-th server is server[i]. The number of requests served by any server is a power of 2, i.e., 1, 2, 4, 8, 16, etc.

Given the array server and an integer expected_load, find the minimum number of servers that must be chosen such that the total sum of requests served by all the chosen servers is exactly equal to the expected load. If there is no combination of servers that can serve exactly the expected_load requests, return -1.

Example:
Input:

n = 4
servers = [1, 1, 2, 4]
expected_load = 3
Output:

2
Explanation:

It is optimal to choose the first and the third server or the second and the third server, serving a total of 1 + 2 = expected_load = 3 requests.
Thus, the minimum number of servers needed is 2.
Constraints:
1 <= n <= 1000 (the number of servers),
1 <= server[i] <= 1000 (each server's request capacity),
1 <= expected_load <= 1000.


"""
#For each server, we update the minimum number of servers required to achieve each possible load by considering the current server and previously computed solutions.
class Solution:
    def min_servers_to_handle_load(self,servers, expected_load):
        dp = [float('inf')] * (expected_load+1) #added +1 for base case
        dp[0]=0

        for s in servers:
            for load in range(expected_load,s-1,-1):
                dp[load] = min(dp[load],dp[load-s]+1)
        
        return dp[expected_load] if dp[expected_load]!=float('inf') else -1
#time: O(n * expected_load)
#space: O(expected_load) 



servers = [1, 1, 2, 4]
expected_load = 3
s= Solution()
output=s.min_servers_to_handle_load(servers,expected_load)
print(output)


