"""
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
 

Constraints:

2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
"""

from typing import List

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        shortestDistance = len(words)
        position1, position2 = -1, -1
        for i in range(len(words)):
            if words[i]==word1:
                position1 = i
            elif words[i]==word2:
                position2 = i

            if position1!=-1 and position2!=-1:
                shortestDistance = min(shortestDistance, abs(position1 - position2))

        return shortestDistance