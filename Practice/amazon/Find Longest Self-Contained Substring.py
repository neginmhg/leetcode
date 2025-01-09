"""
Find Longest Self-Contained Substring
[Hard]


A substring t of a string s is called self-contained if t != s and for every character in t, it doesn't exist in the rest of s.

Return the length of the longest self-contained substring of s if it exists, otherwise, return -1.

 

Example 1:

Input: s = "abba"

Output: 2

Explanation:
Let's check the substring "bb". You can see that no other "b" is outside of this substring. Hence the answer is 2.

Example 2:

Input: s = "abab"

Output: -1

Explanation:
Every substring we choose does not satisfy the described property (there is some character which is inside and outside of that substring). So the answer would be -1.

Example 3:

Input: s = "abacd"

Output: 4

Explanation:
Let's check the substring "abac". There is only one character outside of this substring and that is "d". There is no "d" inside the chosen substring, so it satisfies the condition and the answer is 4.

 
"""
from collections import Counter

class Solution:
    def maxSubstringLength(self, s: str) -> int:
        n = len(s)
        longest = -1
        totalC = Counter(s)  # Count total occurrences of each character in the string

        #for each fixed window size
        for windowSize in range(1, len(totalC) + 1):  # Only loop up to the unique characters in the string
            res = 0
            unique = 0
            l = 0
            #window count 
            count = Counter()  # Counter to track characters in the current window
            print(windowSize)
            for r in range(n):
                newChar = s[r]
                count[newChar] += 1

                if count[newChar] == 1:
                    unique += 1  # We've seen a new character
                if count[newChar] == totalC[newChar]:
                    res += 1  # All occurrences of this char found

                while unique > windowSize:  # Shrink window if unique characters exceed `i`
                    char_l = s[l]
                    count[char_l] -= 1
                    if count[char_l] == 0:
                        unique -= 1  # We lost one of the unique characters
                    if count[char_l] == totalC[char_l] - 1:
                        res -= 1  # Not all occurrences of the character are in the window
                    l += 1

                if res == windowSize and r - l + 1 != n:  # Ensure it's not the entire string
                    print("res found "+str(res)+ s[l:r+1])
                    longest = max(longest, r - l + 1)

        return longest


s = Solution()
out =s.maxSubstringLength("abacd")
print(out)