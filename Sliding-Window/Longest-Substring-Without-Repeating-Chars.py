"""

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring."""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #dealing with duplicates? try SETs
        charSet=set()
        left=0
        res=0
        for right in range(len(s)):
            print(left,right,s[left],s[right],charSet)
            while s[right] in charSet: #if find duplicate then remove until duplicate char is removed
                #print(s[left],s[right],charSet)
                charSet.remove(s[left])     #remove the left pointer from set
                left+=1
            #print(s[left],s[right])
            charSet.add(s[right])       #if not duplicate add it to the set
            res=max(res, right-left+1)      #update result
        return res


s=Solution()
print(s.lengthOfLongestSubstring("pwwkew"))

"""
l=0, r=0 charset=[,c,a,]
abcabcbb
"""