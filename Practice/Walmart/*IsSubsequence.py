"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #s =abc , t =adbgdc
        #i=0 j=0    a=a -> i=1, j=1
        # i=1, j=1   b=d -> j=2 , i=1
        #  j=2 , i=1 -> b=b -> j=3, i=2
        # j=3, i=2 , -> g=c -> i=2, j=4
        #i=2, j=4   , -> c =d -> i=2, j=5
        #i=2, j=5 -> c=c -> i=3, j=6
        #move s forward only if match
        if(len(s)==0 and len(t)==0):
            return True
        if(len(t)==0 ):
            return False
        if(len(s)==0 ):
            return True
        
        j=0
        i=0
        while(j<len(t) and i<len(s)):
            if(s[i]==t[j]):
                i+=1
            if( i==len(s)):
                return True
            j+=1
        return False
