"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is "0", the result is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # Create an array to store the multiplication result
        result = [0] * (m + n)
        
        # Reverse iterate through num1 and num2
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply digits and add to the result array
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                # Position in the result array
                #p1 is for the carry, and p2 is for the current digit.
                p1, p2 = i + j, i + j + 1
                # Sum the product with the existing value at result[p2]
                sum_ = mul + result[p2]
                # Update result array with carry and digit
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10
        
        # Convert result array to string and remove leading zeros
        result_str = ''.join(map(str, result))

        #Remove any leading zeros from the result string and return it. This ensures that the result is formatted correctly without unnecessary zeros at the beginning.
        return result_str.lstrip('0')

# Example usage:
sol = Solution()
print(sol.multiply("123", "456"))  # Output: "56088"
