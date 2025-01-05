"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1+1"
Output: 2
Example 2:

Input: s = "6-4/2"
Output: 4
Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
 

Constraints:

1 <= s <= 104
s consists of digits, '+', '-', '*', '/', '(', and ')'.
s is a valid expression.
"""


class Solution:
    def calculate(self, s:str)->int:
        if not s :
            return 0
        if len(s)==1:
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
        
        stack = []
        prevOp = '+'
        curNum =0 
        s += "@"
        for c in s:
            #if digit
            if c.isdigit():
                curNum = 10*curNum + int(c)
            #if ( means reset prevop to +
            elif c=='(':
                stack.append(prevOp)
                prevOp='+'  #reset prev op   
            #if +-/* or end of string @
            else:
                if prevOp in '*/':
                    stack.append(evaluate(stack.pop(), curNum, prevOp))     
                else:
                    stack.append(evaluate(curNum,0,prevOp))
                prevOp = c
                curNum=0

                if c==')':
                    while type(stack[-1])==int:
                        curNum +=stack.pop()
                    prevOp = stack.pop()
        return sum(stack)
    