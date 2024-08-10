"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countEachChar={}   #hashmap to store frequency of each char IN WINDOW
        res=0   #result for max length

        #sliding window by having left=0 and right looping from 0 to length.
        l=0
        for r in range(len(s)):
            countEachChar[s[r]]=countEachChar.get(s[r],0) +1
            if((r-l+1)- max(countEachChar.values()) > k):  #if not valid, then move left by one
                countEachChar[s[l]]-=1    #decrease the count of the char by 1
                l+=1                #reduce the window
            res=max(r-l+1, res)         
        return res
    
    def optimized_characterReplacement(self, s: str, k: int) -> int:
        countEachChar={}   #hashmap to store frequency of each char
        res=0   #result for max length

        #sliding window by having left=0 and right looping from 0 to length.
        l=0
        maxFrequency=0
        for r in range(len(s)):
            countEachChar[s[r]]=countEachChar.get(s[r],0) +1
            maxFrequency=max(maxFrequency, countEachChar[s[r]])
            if((r-l+1)- maxFrequency > k):  #if not valid, then move left by one
                countEachChar[s[l]]-=1    #decrease the count of the char by 1
                l+=1
            res=max(r-l+1, res)
        return res



s=Solution()
print(s.characterReplacement("AABABBA",1))
print(s.optimized_characterReplacement("AABABBA",1))



"""
Lessons learned:
- to get the value of a key in map use .get  --> myMap.get(KEY,0)
- In sliding window we set l=0 then loop with r from 0 to length.
- We store fequency of each r in map
- Getting maximum key value from a map --> max(myMap.values()) 
"""