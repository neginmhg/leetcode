"""
Part 1: Find a Scrambled Word in a String
Problem Explanation:

You are given a list of words and a "scrambled" string of letters.
The task is to determine if any word from the list can be formed using the letters in the scrambled string.
The letters in the scrambled string can appear in any order, and you can use each letter at most once.
If a word from the list can be formed, return it. Otherwise, return None.
Example:

Input: words = ["cat", "baby", "dog"], scrambled = "tcabnihjs"
Explanation: The word "cat" can be formed using the letters t, c, and a from the scrambled string.
Output: "cat"

--------------------------------------------
"""
# Need t check if all char of word exists in scrambled string
#without repeating chars so use HashMap
#Frequency counter hashmap

from typing import List
from collections import Counter
class Solution:
    def containsWord(self,words:List[str], scrambledStr:str)->str:
        #String to hashmap frequency
        scrambledCounter=Counter(scrambledStr)

        for word in words:
            wordCounter= Counter(word)
            ## Use subtraction of Counters to check if the word can be formed
            if not (wordCounter-scrambledCounter):  #When you subtract one Counter object from another, the result is a new Counter object that contains only the positive differences in counts.
                return word
            
        return ""
#Time : O(k.m)  k is #of words, m is average length of words
#Space: O(n+m)  n is length of scrambled str, m is length of current word being checked

"""
Part 2: Find a Word in a 2D Grid
Problem Explanation:

You are given a 2D grid of letters and a target word.
The word may appear in the grid either:
Horizontally to the right, or
Vertically downward.
The letters must be consecutive but don’t need to wrap or change direction.
The task is to return the coordinates of the letters in the grid that form the word.
If there are multiple matches, return any one.
[['c', 'c', 'x', 't', 'i', 'b'],
 ['c', 'c', 'a', 't', 'n', 'i'],
 ['a', 'c', 'n', 'n', 't', 't'],
 ['t', 'c', 's', 'i', 'p', 't'],
 ['a', 'o', 'o', 'o', 'a', 'a']]

 Word: "catnip"

Explanation: Starting from (1, 1), the word "catnip" is found by moving:
Right: (1, 1) -> (1, 2) -> (1, 3)
Down: (1, 3) -> (2, 3) -> (3, 3) -> (3, 4)
Output: [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)]


--------------------------------------------
"""
# Letters must be consecutive rightward or downward
# So traversal of grid is necessary
# DFS to track path forming
from typing import List, Tuple
class Solution:
    def findWord(self,grid:List[List[str]], word:str)-> List[Tuple[int,int]]:
        rows ,cols = len(grid), len(grid[0])

        def dfs(x,y, dx, dy):
            coordiantes=[]
            for char in word:
                if 0<=x<rows and 0<=y<cols and grid[x][y]==char:
                    coordiantes.append((x,y))
                    x,y =x+dx, y+dy
                else:
                    return [] # Word not found in this direction
            return coordiantes
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==word[0]:
                    #search to right
                    result = dfs(r,c,0,1)
                    if result:
                        return result
                    #search downward
                    result= dfs(r,c,1,0)
                    if result:
                        return result

        return []# Return an empty list if no match is found
#Time : O(rows * cols * len(w))   
#Space: O(len(w))  
"""
Part 3: Find Multiple Words in a 2D Grid
Problem Explanation:

This is an extension of Part 2.
You are given a grid and a list of words. The goal is to find the coordinates of all words in the grid.
Each letter in the grid can only be used once across all words.
If multiple matches are possible for a word, return any valid one.
Example:

Grid:
[['b', 'a', 'b'],
 ['y', 't', 'a'],
 ['x', 'x', 't']]

 Words: ["by", "bat"]

Explanation:
Word "by" can be formed as:
(0, 0) -> (1, 0) (Down)
Word "bat" can be formed as:
(0, 2) -> (1, 2) -> (2, 2) (Down)
Output: [(0, 0), (1, 0)] for "by" and [(0, 2), (1, 2), (2, 2)] for "bat".


"""

# Letters cannot be used across words so 
#backtracking allocate letters uniquely
#DFS + BACKTRACKING to search all words
#maintain a set of visited cells to avoid overlap



from typing import List, Tuple, Dict
class Solution:
    def findMultipleWords(self,grid: List[List[str]], words: List[str]) -> Dict[str, List[Tuple[int, int]]]: 
        rows, cols = len(grid), len(grid[0])

        wordLocation = {}       #{  "bay": [ (0,0),(1,0),(2,0) ]  }

        def dfs(w, x,y,dx,dy):
            coordiantes=[]
            for char in w:
                if 0<=x<rows and 0<=y<cols and grid[x][y]==char:
                    coordiantes.append((x,y))
                    x,y = x+dx, y+dy
                else:
                    return []# Word not found in this direction
            return coordiantes


        def findWord(w):
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == w[0]:
                        #Search left - add 1 to col
                        result=dfs(r,c,0,1)
                        if result:
                            return result

                        #search down - add 1 to row
                        result= dfs(r,c,1,0)
                        if result:
                            return result
            return []  #if no match found



        for w in words:
            wordLocation[w]=findWord(w) #set dictionary key to list from findWord
        

        return wordLocation
    
#Time : O(n * rows * cols * len(w))      #n is number of words
#Space: O(n * len(w))                    #n is number of words