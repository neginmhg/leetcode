"""[easy]
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
"""

from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total_perimeter=0
        visit =set()
        ROWS, COLS= len(grid), len(grid[0])
        def dfs(i,j):
            #base case(at edge or at water) then add 1 perim
            if i<0 or j<0 or i>=ROWS or j>=COLS or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            
            #now go to each direction
            visit.add((i,j))
            perim=dfs(i+1,j)
            perim+=dfs(i,j+1)
            perim+= dfs(i-1,j)
            perim+=dfs(i,j-1)
            return perim
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:       #if the cell is water then calculate perim
                    total_perimeter+= dfs(i,j)
        return total_perimeter