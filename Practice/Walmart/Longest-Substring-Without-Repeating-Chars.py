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
#Time :O(n)
#Space: O(K) , k size of set

#LONGEST SUBSTRING WITHOUT REPEATING CHARS= SLIDING WINDOW
    #If a duplicate is found at r, 
    # move l to the right, removing characters from the set, 
    # until the character at r is no longer a duplicate.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()      #to manage duplciate chars
        res=0
        l=0
        for r in range(len(s)):
            newChar = s[r]
            while newChar in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(newChar)
            res = max(res, r-l+1)   #by here we have a fresh set
        return res
    
    
    
    
    def ls2(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        l, r =0,0
        dups =set()
        res = 0
        while r < len(s):
            while s[r] in dups:
                #found duplicate
                dups.remove(s[l])
                l+=1
            dups.add(s[r])
            r+=1
            res =max(res, r-l)           
        return res


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))