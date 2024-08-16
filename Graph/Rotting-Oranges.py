"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 
"""
from typing import List
#Best solution:
    # BFS simultaniously on all rotten oranges
        #add all rottens to Q
        #next level pop, and add neighbors to q
    #we should keep track of fresh oranges from beginning to end of bfs
    #we need to keep track of time too
#time complexity: O(m*n)    m,n are size of grid
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Initialize time and freshOranges
        #Initialize q for [r,c] of rotten oranges
        time, fresh =0,0
        q = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        # Go to each cell and if cell is rotten add to q
        # if cell was fresh , increment freshOranges
        for r in range(ROWS):
            for c in range(COLS):
                cell =grid[r][c]
                if cell == 2:
                    q.append([r,c])
                if cell ==1:
                    fresh+=1

        #have direction list for adjacents later
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        #BFS part
        #while q is not empty and we have fresh orages
            #for each level of q, pop it, 
            # then for each direction add the adjacent to q
                #if it is not out of bound or fresh , skip
                #else change the fresh to rotten
        while q and fresh>0:
            for i in range(len(q)):
                r, c=q.popleft()
                for rx,cx in directions:
                    row, col = r+rx, c+cx
                    if row<0 or col<0 or row>=ROWS or col >= COLS or grid[row][col] !=1:
                        continue
                    grid[row][col] = 2
                    fresh -=1
                    q.append([row,col])
            time +=1
        return time if fresh==0 else -1
