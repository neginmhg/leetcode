"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize variables
        carry = 0  # Carry for addition
        result = []  # List to store the result
        
        # Pad the shorter string with zeros at the beginning
        max_length = max(len(a), len(b))
        a = a.zfill(max_length)
        b = b.zfill(max_length)
        
        # Add binary digits from right to left
        for i in range(max_length - 1, -1, -1):
            # Calculate the sum of current digits and carry
            total = int(a[i]) + int(b[i]) + carry
            # Determine the new digit and carry
            result.append(str(total % 2))  # Current digit
            carry = total // 2  # Update carry for next position
        
        # If there's a carry left, add it to the result
        if carry:
            result.append('1')
        
        # Reverse the result and join to form the final string
        return ''.join(result[::-1])

# Example usage:
sol = Solution()
print(sol.addBinary("1010", "1011"))  # Output: "10101"
