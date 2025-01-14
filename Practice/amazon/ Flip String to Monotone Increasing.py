"""
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

 

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.

"""
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = 0
        for c in s:
            if c == '0':
                m += 1
        ans = m
        for c in s:
            if c == '0':
                m -= 1
                ans = min(ans, m)
            else:
                m += 1
        return ans
    def minFlipsMonoIncr2(self, s: str) -> int:
        # Step 1: Pre-compute total number of zeros (count0Right)
        countZeros = 0
        for c in s:
            if c == '0':
                countZeros += 1
        
        # Step 2: Initialize variables
        count1Left = 0  # Number of 1s to the left
        count0Right = countZeros  # Number of 0s to the right
        flips = countZeros  # Start with all 0s flipped to 1s
        
        # Step 3: Iterate through the string
        for c in s:
            if c == '0':
                count0Right -= 1  # A 0 moves from right to left
            else:
                count1Left += 1  # A 1 is added to the left
            flips = min(flips, count1Left + count0Right)  # Update minimum flips
        
        return flips
    
"""
Solution Explanation

To solve the problem efficiently, we use the idea of a pivot to divide the string into two parts:

The left side of the pivot should consist of only 1s.
The right side of the pivot should consist of only 0s.
For any pivot i, the total number of flips needed can be expressed as:
            Flips(i) = count1Left(i) + count0Right(i)
Where:
count1Left(i): The number of 1s in the left part (to be flipped to 0s).
count0Right(i): The number of 0s in the right part (to be flipped to 1s).



Example of 00110 with output as 2:

**Iteration 1**  
- Index: 0, Character: `0`  
- `count1Left = 0`, `count0Right = 2`  
- Flips at this point: `count1Left + count0Right = 0 + 3 = 3`  
- Minimum flips so far: `3`


**Iteration 2**  
- Index: 1, Character: `0`  
- `count1Left = 0`, `count0Right = 1`  
- Flips at this point: `count1Left + count0Right = 0 + 2 = 2`  
- Minimum flips so far: `2`


**Iteration 3**  
- Index: 2, Character: `1`  
- `count1Left = 1`, `count0Right = 1`  
- Flips at this point: `count1Left + count0Right = 1 + 1 = 2`  
- Minimum flips so far: `2`


**Iteration 4**  
- Index: 3, Character: `1`  
- `count1Left = 2`, `count0Right = 1`  
- Flips at this point: `count1Left + count0Right = 2 + 1 = 3`  
- Minimum flips so far: `2`


**Iteration 5**  
- Index: 4, Character: `0`  
- `count1Left = 2`, `count0Right = 0`  
- Flips at this point: `count1Left + count0Right = 2 + 0 = 2`  
- Minimum flips so far: `2`  


"""