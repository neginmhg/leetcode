"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        def backtrack(index, curStr):
            # If the path length is the same as digits length, we have a complete combination
            if index == len(digits):
                res.append(curStr)
                return
            
            # Get the letters that the current digit maps to, and loop through them
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                backtrack(index + 1, curStr + letter)
        
        # List to hold the combinations
        res = []
        # Initiate backtracking
        backtrack(0, "")
        
        return res
