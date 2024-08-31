"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]
"""
#reverse thinking
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS,COLS = len(board), len(board[0])
        # 1. DFS - capture unsurrounded(border) O -> T
        # 2. FOR LOOP - capture all region from O -> X
        # 3. FOR LOOP - uncapture unsurrounded region from T -> O

        def dfs(r , c):
            if (r<0 or c<0 or r==ROWS or c ==COLS or board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            dfs[r+1][c]
            dfs[r-1][c]
            dfs[r][c+1]
            dfs[r][c-1]
        #1
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" 
                    and (r in [0,ROWS-1] or c in [0, COLS-1])):
                    dfs(r,c)
        #2
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] =="O":
                    board[r][c] ="X"
        #3
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] =="T":
                    board[r][c] ="O"


