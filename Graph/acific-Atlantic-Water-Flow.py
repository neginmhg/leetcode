"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
"""
#DFS or BFS from cells would be O(m*n)^2
#better solution? DFS or BFS from the oceans O(m*n)
    #have 2 visit sets one for pacific one for atlantic
    #add the cell to coresponding set based on which direction we goin
    #once we go through all, then check each cell and see if that cell is in both sets then it mean the cell can reach both oceans
        #then add to result

from typing import List
from collections import deque
class Solution:
    def pacificAtlantic(self,matrix: List[List[int]]) -> List[List[int]]:
        # Check if the matrix is empty or if the first row is empty
        # Return an empty list if either condition is true
        if not matrix or not matrix[0]:
            return []

        # Define a BFS function to explore reachable cells from given starting points
        def bfs(starting_points):
            rows, cols = len(matrix), len(matrix[0])  # Get the number of rows and columns
            queue = deque(starting_points)  # Initialize the queue with starting points
            reachable = set(starting_points)  # Initialize the set of reachable cells
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Directions for moving down, up, right, and left
            
            # Perform BFS
            while queue:
                r, c = queue.popleft()  # Dequeue the next cell to process
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc  # Compute the neighboring cell's coordinates
                    # Check if the neighboring cell is within bounds, not visited yet, and has a height >= current cell
                    if (0 <= nr < rows and 0 <= nc < cols and
                        (nr, nc) not in reachable and
                        matrix[nr][nc] >= matrix[r][c]):
                        reachable.add((nr, nc))  # Mark the neighboring cell as reachable
                        queue.append((nr, nc))  # Enqueue the neighboring cell for further exploration
            
            return reachable  # Return the set of reachable cells

        rows, cols = len(matrix), len(matrix[0])  # Get the number of rows and columns
        
        # Initialize starting points for the Pacific Ocean (top and left borders)
        pacific_starts = [(0, i) for i in range(cols)] + [(i, 0) for i in range(rows)]
        
        # Initialize starting points for the Atlantic Ocean (bottom and right borders)
        atlantic_starts = [(rows - 1, i) for i in range(cols)] + [(i, cols - 1) for i in range(rows)]
        
        # Perform BFS from the Pacific Ocean starting points
        pacific_reachable = bfs(pacific_starts)
        
        # Perform BFS from the Atlantic Ocean starting points
        atlantic_reachable = bfs(atlantic_starts)
        
        # Find the intersection of cells reachable from both oceans and return as a list
        return list(pacific_reachable & atlantic_reachable)



    # Example usage
    matrix = [
        [1, 2, 3, 4, 5],
        [16,17,24,23,6],
        [15,18,25,22,7],
        [14,19,20,21,8],
        [13,12,11,10,9]
    ]
    print(pacificAtlantic(matrix))
