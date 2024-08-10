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

#defaultdict = If you access a key that is not yet present in the dictionary, defaultdict automatically creates a new value using this factory function. For defaultdict(list), the factory function is list(), which creates an empty list.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # {[1][3]..26.[0]:}
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
            #By converting count (a list) into count_tuple (a tuple), you create an immutable representation of character frequencies. This immutability is essential for using it as a key in the res dictionary.
        return list(res.values())

    


solution=Solution()
strs1 = ["eat","tea","tan","ate","nat","bat"]
r=solution.groupAnagrams(strs1)
print(r)






"""
if sorting is allowed then:
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=defaultdict(list)
        for s in strs: #get the string
            sorted_s=''.join(sorted(s))
             # Append the string to the corresponding list in the dictionary
            dict[sorted_s].append(s)        #{'aet',['eat','ate']}
        return list(dict.values())

"""
