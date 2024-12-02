"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}     #cache for top down recurssion

        def dfs(i, j):
            # If already computed, return the value
            if (i, j) in dp:
                return dp[(i, j)]

            # Base case: both strings are fully matched
            if i >= len(s) and j >= len(p):
                return True
            
            # Edge case: pattern is exhausted but string is not
            if j >= len(p):
                return False

            # Check if characters match (including '.')
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # Check for *: Handle '*' pattern
            if (j + 1) < len(p) and p[j + 1] == '*':
                # Skip '*' or use '*' (consume character in `s` if match)
                dp[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return dp[(i, j)]  # Return result immediately after processing '*'

            # Handle normal match with dot or same character
            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]  # Return result immediately after processing match

            # If no match is found
            dp[(i, j)] = False
            return False

        return dfs(0, 0)
