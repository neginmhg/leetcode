""" [MEDUIM]
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False


        #We initialize two arrays, s1Count and s2Count, each containing 26 elements initialized to 0. These arrays will store the counts of characters in s1 and the current window of s2.
        s1Count , s2Count=[0]*26, [0]*26
        for i in range(len(s1)):
            #set the map/array for s1
            #map each character to an index in the arrays. This works because ASCII values for lowercase letters start from 97 ('a').
            s1Count[ord(s1[i])-ord('a')]+=1     #ascii of each char is the index of s1Count
            #set the map/array for s2 - ONLY THE FIRST len(s1) chars
            s2Count[ord(s2[i])-ord('a')]+=1     #ascii of each char is the index of s1Count
        
        
        #We initialize a variable matches to keep track of the number of matches between s1Count and s2Count. If matches reaches 26, it means s2 contains a permutation of s1.
        matches=0       #if matches=26 then we return true

        #initialize the matches for the first characters s1 had
        for i in range(26):
            matches+=(1 if s1Count[i]==s2Count[i] else 0)

        #SLIDING WINDOW TECHNIQUE
        l=0
        for r in range(len(s1), len(s2)):           #start at length of s1 and end at length of s2
            if matches==26:  return True
            #move the right pointer
            index= ord(s2[r])- ord('a')
            s2Count[index] +=1
            if s1Count[index]==s2Count[index]:
                matches+=1
            elif s1Count[index]+1==s2Count[index]:
                matches-=1
            #move the left pointer
            index= ord(s2[l])- ord('a')
            s2Count[index] -=1
            if s1Count[index]==s2Count[index]:
                matches+=1
            elif s1Count[index]-1==s2Count[index]:
                matches-=1
            l+=1
        return matches==26



        