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
# rSize=len(matrix[0])
#while i<rSize and j< len(matrix)
#i=0 rSize=len(matrix[0])
# SET --> l = matrix[i][0] and R = matrix[i][rSize-1]
#Do binary search for target
    # if not in the range L and R and target<R then return false
    # if not in the range L and R then i+=1
    # if in the range L and R found target on binary search then return true

