from typing import List
class Solution:
    def combine(nums:List[int],k:int)-> List[list[int]]:
        def backTrack(start, curComb, res):
            if len(curComb)==k:
                res.append(curComb.copy())
                return
            for i in range(start, len(nums)):
                curComb.append(nums[i])
                backTrack(i+1, curComb, res)
                curComb.pop()
        res=[]
        backTrack(0,[],res)
        return res