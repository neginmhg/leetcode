"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.

"""
class Solution:
    def calculate(self, s: str) -> int:
        if not s or len(s) == 0:  # Check for empty input
            return 0
        if len(s) == 1 and s.isdigit():  # Handle single-digit input
            return int(s)
        def evaluate(x,y, op):
            if op=='+':
                return x
            if op =='-':
                return -x
            if op=='*':
                return x*y
            if op =='/':
                return int(x/y)
        #get rid of all spaces
        s = s.replace(" ", "")  # Remove all spaces
        N = len(s)-1
        curNum =0 
        op ='+'
        stack = []


        for i,c in enumerate(s):
            #if digit
            if c in '0123456789':
                curNum = (curNum*10)+int(c)
            #not digit
            if c in '*+-/' or i==N: 
                if op in '*/':
                    stack.append(evaluate(stack.pop(), curNum, op))     
                else:
                    stack.append(evaluate(curNum,0,op))
                curNum=0
                op =c
        return sum(stack)