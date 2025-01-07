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

class Solution:
    def maxSubstringLength(self, s: str) -> int:
        n = len(s)
        res = -1
        totalCount = [0] * 26

        # Count total number of characters in the string
        for char in s:
            totalCount[ord(char) - ord('a')] += 1

        for i in range(1, 27):  # i is the number of unique chars in the substring
            valid = 0
            unique = 0
            left = 0
            count = [0] * 26

            for right in range(n):
                char_right = ord(s[right]) - ord('a')
                count[char_right] += 1

                if count[char_right] == 1:
                    unique += 1  # We've seen a new character
                if count[char_right] == totalCount[char_right]:
                    valid += 1  # All occurrences of this character are in the substring

                while unique > i:
                    char_left = ord(s[left]) - ord('a')
                    count[char_left] -= 1
                    if count[char_left] == 0:
                        unique -= 1  # We lost one of the new chars
                    if count[char_left] == totalCount[char_left] - 1:
                        valid -= 1  # Not all of the character is in this substring anymore
                    left += 1

                if valid == i and right - left + 1 != n:  # Make sure it's not the entire string
                    res = max(res, right - left + 1)

        return res
