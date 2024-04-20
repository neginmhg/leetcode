""" [MEDIUM]
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=defaultdict(list)
        for s in strs: #get the string
            sorted_s=''.join(sorted(s))
             # Append the string to the corresponding list in the dictionary
            dict[sorted_s].append(s)        #{'aet',['eat','ate']}
        return list(dict.values())
    


solution=Solution()
strs1 = ["eat","tea","tan","ate","nat","bat"]
r=solution.groupAnagrams(strs1)
print(r)
