"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""



from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open<n
        # only add closing parenthesis if closed<open
        #valid iff open==closed==n

        stack=[]
        res=[]
        def backtrack(open, closed):
            #base case
            if open==closed==n:
                res.append("".join(stack))
                return   
            #condition       
            if open<n:
                stack.append("(")
                backtrack(open+1,closed)
                stack.pop() #roll back
            #condition
            if closed<open:
                stack.append(")")
                backtrack(open,closed+1)
                stack.pop()     #roll back

        backtrack(0,0)
        return res

s=Solution()
print(s.generateParenthesis(3))