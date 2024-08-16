"""
[HARD]
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from typing import List
class TrieNode():
    def __init__(self):
        self.children={}
        self.isWord=False
    def addWord(self, word):
        cur=self
        for c in word:
            if c not in self.children:
                cur.children[c]=TrieNode()
            cur= cur.children[c]
        cur.isWord=True   #once we go through the whole word mark the last node as the end
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # STEP1 = populate Trie with all words
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r,c, node, word):
            #current char is board[r][c]
            currentChar = board[r][c]
            #Get the node for currentChar
            node = node.children(currentChar) 

            #check base cases
            if r<0 or c<0 or r==ROWS or c==COLS or board[r][c] not in node.children or (r,c) in visited:
                return
            
            
            visited.add((r,c))   # add tuple as visited
            word += currentChar     #append the char to the word
            if node.isWord:             #if node is end then save the word
                res.append(word)  
            
            
            #explore 4 directions and continue the word          
            dfs(r+1,c,node,word)        
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            #for each direction now reset visited for the next direction
            visited.remove((r,c))

        for r in ROWS:
            for c in COLS:
                #search each possibility
                dfs(r,c, root , "")
        return list(res)
        
"""
1. Create a Trie, add words to it, and initialize variables.
2. Explore all possible paths from each cell using DFS, building words and checking against the Trie.
3. Start DFS from every cell on the board and collect found words.
4. Return the list of found words.
"""