""" [HARD]
You are given an array of strings ideas where each string represents a word. A valid name can be formed by swapping the first letter of two different words in the list. 
However, you can only count the name as valid if it does not already exist in the list.

Example:
ideas = ["coffee", "donuts", "time", "toffee"]

Possible valid new names:

Swap "c" (from "coffee") with "t" (from "time") → "toffee", "cime"
Swap "d" (from "donuts") with "t" (from "time") → "tonuts", "dime"
However, since "toffee" is already in the list, it cannot be counted again.



"""
from collections import defaultdict  # Import defaultdict to create a dictionary with default values for non-existent keys
from itertools import combinations  # Import combinations to generate pairs of elements from a list

class Solution:
    def distinctNames(self, ideas):
        wordMap = defaultdict(set)  # Create a defaultdict where each key will map to a set of suffixes
        
        # Group words by their first character
        for w in ideas:
            wordMap[w[0]].add(w[1:])  # Add the suffix (word without the first character) to the set corresponding to the first character
        
        res = 0  # Initialize the result variable to store the total number of valid name pairs
        
        # Iterate over all pairs of different first characters using combinations
        for char1, char2 in combinations(wordMap, 2):
            intersect = 0  # Initialize intersect to count common suffixes between the two character groups

            # Count the number of common suffixes between the two character groups
            for w in wordMap[char1]:
                if w in wordMap[char2]:
                    intersect += 1  # Increment the count if the suffix is found in both groups

            # Calculate the number of distinct suffixes for char1 and char2
            distinct1 = len(wordMap[char1]) - intersect  # Suffixes in char1 that are not in char2
            distinct2 = len(wordMap[char2]) - intersect  # Suffixes in char2 that are not in char1

            # Multiply the distinct counts to get the number of valid name pairs for this character pair
            res += distinct1 * distinct2

        # Multiply the result by 2 to account for the fact that each pair can be swapped
        return res * 2

# Example usage:
ideas = ["coffee", "donuts", "time", "toffee"]
sol = Solution()  # Instantiate the Solution class
print(sol.distinctNames(ideas))  # Output the result, expected: 6



"""
Explanation of Comments:
The 2 in combinations(wordMap, 2) specifies that you want to generate pairs (i.e., combinations of 2 elements).
 
Imports: The defaultdict and combinations are imported to simplify dictionary handling and pair generation.

Grouping Words: Words are grouped by their first character, storing the suffixes in a set for efficient lookup.

Counting Pairs: The combinations function generates pairs of different characters, ensuring that each pair is only considered once.

Calculating Valid Pairs: For each character pair, common suffixes are subtracted to find distinct suffixes, and the product of these distinct counts is added to the result.

Final Adjustment: The result is doubled at the end to account for name pairs being valid in both directions (e.g., ab and ba).
"""