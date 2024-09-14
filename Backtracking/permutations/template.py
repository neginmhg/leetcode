from typing import List
class Permutation:
    def permute(self, nums: List[int])-> List[List[int]]:
        def backtrack(curPerm, result):
            if len(curPerm)==len(nums):
                result.append(curPerm.copy())
                return
            for n in nums:
                if n not in curPerm:
                    curPerm.append(n)
                    backtrack(curPerm,result)
                    curPerm.pop()
        result=[]
        backtrack([], result)
        return result