"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
"""
#Use cache for each position since we might visit it cache[i][j]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bottom row will always have just 1s
        # At the last row of the grid, the robot can only move right to reach the end. 
        # Thus, all cells in this row have 1 unique path to the destination.
        row = [1]* n        

        #go to all row except last one
        for i in range(m - 1):
            newRow = [1] * n  # Initialize newRow with 1's.
            for j in range(n - 2, -1, -1):  # Loop through the row from right to left.
                newRow[j] = newRow[j + 1] + row[j]  # Update newRow[j] with the sum of the cell below and to the right.
            row = newRow  # Move newRow to row for the next iteration.
        return row[0]  # Return the number of paths from the top-left corner.

    

        #O(m*n) time complexity
        #O(n) memory complexity

"""
The core idea is that for each cell in the grid, we compute how many unique paths there are to the destination. You can only move right or down, so at each position, the number of paths comes from two possible places:
    The cell directly below (down).
    The cell directly to the right.
"""