"""
You are given an m x n integer matrix matrix with the following two properties:

    -- Each row is sorted in non-decreasing order.
    -- The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

#-----------This was my thought-----------
# rSize=len(matrix) colSize=len(matrix[0])
#while i<rSize and j< len(matrix)
#i=0 rSize=len(matrix[0])
# SET --> l = matrix[i][0] and R = matrix[i][rSize-1]
#Do binary search for target
    # if not in the range L and R and target<R then return false
    # if not in the range L and R then i+=1
    # if in the range L and R found target on binary search then return true
        # m = l+r //2
#---------------------------------
#-----------better solution-----------
    #instead of doing log(n) for finding the correct row, do binary search
    #to find the row
    #onoce the row is found then another binary search inside the row
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS =len(matrix), len(matrix[0])
        top, bot = 0, ROWS-1
        
        targetRow=0
        while top <= bot:
            curRow=(top+bot)//2     #make sure to put the (), or you will get index out of range
            if target > matrix[curRow][-1]:
                top=curRow+1
            elif target< matrix[curRow][0]:
                bot=curRow-1
            else:
                targetRow=curRow
                break

        if not top<= bot:
            return False
        
        l,r = 0, COLS-1
        while l<=r:
            m=(r+l)//2       #make sure to put the (), or you will get index out of range
            if target> matrix[targetRow][m]:
                l=m+1
            elif target<matrix[targetRow][m]:
                r=m-1
            else: 
                return True
        return False
