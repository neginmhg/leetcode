"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
"""
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = [0]       #output 
        tilesFreq = Counter(tiles)  #count the frequency of each char
        def backtrack(tilesFreq):
            for char in tilesFreq: 
                if tilesFreq[char]>0:
                    res[0]+=1           
                    tilesFreq[char]-=1
                    backtrack(tilesFreq)
                    tilesFreq[char]+=1
    
        backtrack(tilesFreq)
        return res[0]