"""[HARD]
Minimum Window Substring :

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If the target string t is empty, there's no substring to find, return an empty string
        if t == "":
            return ""
        
        # Initialize maps to count characters in t and the current window
        countT, countWindow = {}, {}
        
        # Count the occurrences of each character in t and store in countT dictionary
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        # Initialize variables to track the number of characters we have and need
        have, need = 0, len(countT)
        
        # Initialize variables to store the result indices and length
        res, resLen = [-1, -1], float("infinity")
        
        # Initialize left pointer of the window
        l = 0
        
        # Loop through each character in s
        for r in range(len(s)):
            c = s[r]  # Current character in s
            
            # Update count of current character in the window
            countWindow[c] = countWindow.get(c, 0) + 1
            
            # If the current character is in t and its count in the window matches its count in t
            if c in countT and countT[c] == countWindow[c]:
                have += 1  # Increment the count of characters we have
            
            # While we have all characters from t in the window
            while have == need:
                # Update result indices and length if the current window is smaller than the previous result
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]  # Update result indices
                
                #pop left and update have and countWindow and left pointer
                # Decrease the count of character at left pointer and update 'have' if necessary
                countWindow[s[l]] -= 1
                if s[l] in countT and countWindow[s[l]] < countT[s[l]]:
                    have -= 1
                
                # Move left pointer to shrink the window
                l += 1
        
        # Extract the minimum window substring based on result indices
        "By unpacking res using the assignment l, r = res, you're assigning the first element of res to the variable l and the second element to the variable r. This is a concise way to extract the starting and ending indices of the minimum window substring from the res list."
        l, r = res
        #need to do r+1 since to get the r index we need to include it by adding 1
        return s[l:r + 1] if resLen != float("infinity") else ""

