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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROW, COL = len(grid), len(grid[0])
        visit =set()
        def bfs(r,c):
            if (r,c) in visit:
                return 0
            visit.add((r,c))
            direction=[(1,0),(0,1),(0,-1),(-1,0)]
            q = deque([(r,c)])
            while q :           
                r,c = q.popleft() 
                for dr,dc in direction:
                    nr,nc = r+dr , c+dc
                    if nr<ROW and nr>=0 and nc<COL and nc>=0 and grid[nr][nc]=='1' and (nr,nc) not in visit:
                        visit.add((nr,nc))
                        q.append([nr,nc])
            return 1

        islands=0
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visit and grid[r][c] =='1':
                    islands+=bfs(r,c)
        return islands
    
#One optimization would be to not have a set and mark grid[r][c]=0 to show it is visited
#Time = O(ROW * COL)
#Space = O(ROW * COL)