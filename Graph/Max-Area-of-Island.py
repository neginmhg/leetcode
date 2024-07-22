"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 
"""
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns
        rows, cols = len(grid), len(grid[0])
        # Set to keep track of visited cells
        visit = set()
        
        def dfs(r, c):
            # If the cell is out of bounds, is water, or already visited, return 0
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visit:
                return 0
            # Mark the cell as visited
            visit.add((r, c))
            # Initialize area as 1 for the current cell
            area = 1
            # Explore all 4 directions (up, down, left, right) and add their areas
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area
        
        max_area = 0
        # Traverse each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land and not visited, compute the area of the island
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
