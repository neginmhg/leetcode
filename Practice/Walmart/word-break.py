"""Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence of one or more 
dictionary words.

Note that the same word in the dictionary may be reused multiple 
times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique."""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #create dp array with length s+1, default as False
        dp = [False] * (len(s)+1)

        #Base Case: empty strings can always be segmented
        dp[len(s)]=True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i + len(w))<=len(s) and s[i:i+len(w)]==w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]

#Given a string and bunch of words, can the string be created by words?

#DP: Iterate from the last character in s, then for each word in the dictionary, check if s[i:i+len(word)] == word, and if it matches, update the DP array to reflect that the substring up to i can be segmented.