"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
from typing import Counter
#1. solution(uses memory) = use hashmaps cause we need to make sure the same count of each char exists in both strings.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS, countT={},{}
        #loop through strings and store the count 
        #of their chars
        for i in range(len(s)):
            countS[s[i]]=1+ countS.get(s[i],0)
            countT[t[i]]=1+ countT.get(t[i],0)
        print(countS)
        for key in countS:
            if countS[key] != countT.get(key,0):
                return False
        return True     
#2. solution (efficient)= use python Count() function which counts the number of chars 
    def isAnagram2(self, s:str, t:str) -> bool:
        return Counter(s) == Counter(t)
#3. solution (saves memory)= sort the strings, if they are the same then return True. The only thing is that sorting algorithms have O(n^2) or O(nlogn) complexities.
    def isAnagram3(self, s:str, t:str) -> bool:
        return sorted(s) == sorted(t)



#--------------------------------------
#calling
solution = Solution()
s = "anagram"
t = "nagaram"
r=solution.isAnagram(s, t)
print(r)  
r2=solution.isAnagram2(s, t)
print(r2) 
r3=solution.isAnagram2(s, t)
print(r3) 