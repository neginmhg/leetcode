/*
 * Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

 */

public class Reverse {
    public int reversef(int x) {
        boolean negative = false;
        
        // Handle negative number
        if (x < 0) {
            negative = true;
            //Need to check if making it negative would overflow
            if(x < -1* Integer.MAX_VALUE)
                return 0;
            x = -x; // Make the number positive for easier handling
        }

        int res = 0;
        while (x != 0) {
            int remainder = x % 10;
            x = x / 10;
            //before updating res we need to check if would overflow
            // Overflow check: before multiplying res by 10
            if (res > Integer.MAX_VALUE / 10 || (res == Integer.MAX_VALUE / 10 && remainder > 7)) {
                return 0; // Return 0 if it exceeds the 32-bit integer range
            }

            res = res * 10 + remainder;
        }

        // If the number was negative, make the result negative
        return negative ? -res : res;
    }
}