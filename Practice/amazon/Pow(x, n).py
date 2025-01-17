"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n==0:
                return 1
            if n<0:
                n = -1 * n 
                x = 1.0/x
            result =1 
            while n!=0:
                #odd power
                #x*result =result
                #n-=1
                #odd n then store the extra x in result
                if n%2==1:
                    result*=x
                    n-=1
                #now n is even
                #square X
                #even n then square x and halve n and proceed
                x *=x
                n //=2
            return result
        return helper(x,n)
