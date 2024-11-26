"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

class Solution:
    def longestCommonSubsequence_BU(self, text1: str, text2: str) -> int:
        #Dynamic Programming (Bottom-Up)
        dp =[[0 for j in range(len(text2)+1)] 
                for i in range(len(text1)+1)]
        #Iterative
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]= 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
    
    #Dynamic Programming (Top-Down)
    def longestCommonSubsequence_TD(self, text1:str, text2:str)->int:
        #Recurssion
        memo ={}
        def dfs(i,j):
            #base case
            if i==len(text1) or j==len(text2):
                return 0
            #if already visited
            if (i,j) in memo:
                return memo[(i,j)]
            #if characters match then it's part of LCS
            if text1[i] == text2[j]:
                memo[(i,j)] = 1+ dfs(i+1,j+1)
            #if chars not match then either skip a char from text1 or text2
            else:
                memo[(i,j)] = max( dfs(i+1,j), dfs(i,j+1))
            
            return memo[(i,j)]
        return dfs(0,0)
            

    
    #Bottom Up
    #If space is a concern, you can reduce the DP table to a 1D array because each row depends only on the previous row. Let me know if you'd like to see the space-optimized version!
    def optimized_longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #ensuring text2 always smaller
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        prev = [0] * (len(text2)+1) #+1 is for base case
        cur = [0] * (len(text2)+1 )

        for i in range(len(text1)-1, -1,-1):
            for j in range(len(text2)-1, -1,- 1):
                #if found save in cur
                if text1[i]==text2[j]:
                    cur[j] = 1 + prev[j+1]
                
                #If the characters don’t match: 
                #LCS is max of Skipping the character in text1 (prev[j])
                #OR Skipping the character in text2 (curr[j + 1])
                else:
                    cur[j] = max(cur[j+1], prev[j])
            prev, cur = cur, prev

        return prev[0]
    



#Time complexity: O(m*n)