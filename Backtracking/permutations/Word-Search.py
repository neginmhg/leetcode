"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

"""
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Dimensions of the board
        rows, cols = len(board), len(board[0])
        
        # Directions for moving up, down, left, and right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(r, c, index):
            # If the entire word is found
            if index == len(word):
                return True
            
            # If out of bounds or not matching the current character
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            # Temporarily mark the cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all possible directions
            for dr, dc in directions:
                if dfs(r + dr, c + dc, index + 1):
                    return True
            
            # Backtrack: restore the original value of the cell
            board[r][c] = temp
            return False
        
        # Try to find the word starting from each cell in the grid
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False


"""
Order Matters: The word must be formed by sequentially adjacent cells, which means the order of letters is crucial. For example, to form the word "ABC", you must go from 'A' to 'B' to 'C' in that specific order.

To solve the problem of finding if a word exists in a given grid of characters, we can use Depth-First Search (DFS) with backtracking. 


### Explanation of the Code

1. **Initialization:**
   - `rows, cols` store the dimensions of the board.
   - `directions` define the four possible movements (right, down, left, up).

2. **DFS Function:**
   - **Base Case:** If `index` equals the length of the word, the entire word is found, return `True`.
   - **Out of Bounds or Mismatch:** If the current cell is out of bounds or doesn't match the character at the current `index` of the word, return `False`.
   - **Mark Visited:** Temporarily mark the cell as visited by changing its value to `'#'`.
   - **Explore Directions:** Recursively call `dfs` for all possible directions. If any call returns `True`, the word is found.
   - **Backtrack:** Restore the original value of the cell to allow for other possible paths.

3. **Main Function:**
   - Iterate through each cell in the grid.
   - Call the `dfs` function if the cell matches the first character of the word.
   - If `dfs` returns `True` for any cell, the word exists in the grid, return `True`.
   - If no valid path is found after checking all cells, return `False`.

This approach ensures that all possible paths are explored while avoiding revisiting cells within a single path, thanks to the backtracking mechanism.
"""