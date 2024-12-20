""" [MEDUIM]
Given two strings s1 and s2, return true if s2 contains a
 permutation of s1, or false otherwise.

In other words, return true if one of s1's 
permutations is the substring of s2.

 

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
        if len(s1) > len(s2):  # If s1 is longer than s2, return False
            return False

        # Arrays to count frequency of each letter (26 letters in total)
        s1Count, s2Count = [0] * 26, [0] * 26

        # Populate the frequency arrays for s1 and the first window in s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1  # Counting letters in s1
            s2Count[ord(s2[i]) - ord('a')] += 1  # Counting letters in the first window of s2

        # Variable to count how many characters match between s1 and s2 window
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1  # Initial match count for the first window

        # Sliding window approach
        l = 0  # Left pointer for the window
        for r in range(len(s1), len(s2)):  # Right pointer moves over s2
            if matches == 26:  # If all characters match, return True
                return True

            # Add the right character (expand the window)
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove the left character (shrink the window)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1  # Move the left pointer

        return matches == 26  # If all 26 characters match, return True
    


#Time :O(N), where N is the length of s2
#Space: O(1), because we only use a fixed amount of extra space for the two frequency arrays.