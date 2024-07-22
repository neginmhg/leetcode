""""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0  # If the grid is empty, return 0 as there are no islands
        
        def dfs(r, c):
            # If the current cell is out of bounds or is water, return immediately
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
                return
            grid[r][c] = '0'  # Mark the current cell as visited by setting it to '0'
            # Recursively call dfs for all adjacent cells (down, up, right, left)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        num_islands = 0  # Initialize a counter for the number of islands
        for r in range(len(grid)):  # Iterate over each row
            for c in range(len(grid[0])):  # Iterate over each column
                if grid[r][c] == '1':  # If a cell contains '1', it means we found an island
                    num_islands += 1  # Increment the island counter
                    dfs(r, c)  # Start a DFS to mark all parts of this island as visited
        
        return num_islands  # Return the total number of islands found
