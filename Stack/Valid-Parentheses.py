""" [EASY]
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]   #stack is a list in python
        mapping={')':'(',   '}':'{',    ']':'['} 

        for char in s:
            # if char is an opening, then push into stack
            if char in mapping.values():
                stack.append(char)
            #if char is a closing, then pop the last element and compare it to the map of char.
            elif char in mapping:
                #if stack is empty or comparison don't match then return false
                if not stack or mapping[char]!=stack.pop():
                    return False    
            else:
                return False

        #At the end of the function, if the input string is valid, the stack should be empty because all opening brackets should have been matched and popped by their corresponding closing brackets.
        return not stack
        """If the stack is empty, not stack evaluates to True, indicating that the input string is valid. If the stack is not empty, not stack evaluates to False, indicating that there are unmatched opening brackets in the input string, making it invalid."""
    
""""
Time complexity: O(n)
Space complexity: O(n)
"""

s=Solution()
print(s.isValid("()[]{}"))