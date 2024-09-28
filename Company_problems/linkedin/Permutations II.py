""""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

"""
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        perm=[]
        count= {n:0 for n in nums}
        for n in nums:          #store count of each number
            count[n] +=1
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())     #don't forget to COPY
                return
            for c in count:
                if count[c]>0:
                    perm.append(c)
                    count[c]-=1

                    dfs()

                    count[c]+=1
                    perm.pop()
        dfs()
        return res
    
    """
Why This Works
    -Avoiding Duplicates: By using a count dictionary, you ensure that each unique number is used only as many times as it appears in the input. This prevents generating duplicate permutations because the same number won't be chosen multiple times in the same depth level of the recursive call.
    -Backtracking: The use of backtracking allows you to explore all possible configurations of numbers in perm while being able to revert to the previous state easily.


Summary of the Logic and Pattern

    -Counting Occurrences: First, count the occurrences of each number to manage how many times you can use it in permutations.
    - DFS Approach: Use a recursive function to build permutations. When a complete permutation is formed, store it in the results.
    - Backtracking: After exploring a path (adding a number), backtrack by removing the number and restoring its count, allowing exploration of other potential paths."""