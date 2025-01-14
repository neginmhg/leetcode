"""
Amazon is offering a discount on every purchase of a pair of products whose price sum is divisible by X.

Given the price of n products in the store, find the number of pairs (i, j) where i < j and price[i] + price[j] is divisible by X.

Example:

There are n = 5 products, x = 60 and price = [31, 25, 85, 29, 35].

The answer is 3, based on the pairs:
    (31,29)
    (25,35)
    (85,35)
Each pair sums to a number divisible by X (in this case, 60).

Function description:Complete the function getDiscountPairs in the editor below. 
getDiscountPairs  has the followig params:
    int x: sum of pairs of integers should be divisble by this number
    int price[n] : the prices of the products

    

Returns: integer which is the number of pairs in the array whose sum is divisible by X


Constraints:

2 <= n <= 10^5 (where n is the length of the price list)
1 <= x <= 10^6
1 <= price[i] <= 10^6
"""
from typing import List
from collections import defaultdict
class Solution:
    def getDiscountPairs(self, x: int, price: List[int]) -> int:
        #{remainder : freq}
        remainderCount =defaultdict(int)
        resultPairs=0
        for p in price:
            #1. caulcualte remainder and complement
            remainder = p%x
            complement  = (x-remainder)%x

            #2. add count of complement to result
            #The count of such complements will give the number of valid pairs up to that point.
            resultPairs += remainderCount[complement]

            #3. update count of remainder 
            remainderCount[remainder]+=1

        return resultPairs

#time : O(n) because of for loop
#space : o(n) because of defaultdict
#------------------------------------------------------------


    #Bad solution
    def bruteforce(self,x: int, price: List[int]) -> int:
        resultSet = set()
        N=len(price)
        for i in range(N):
            for j in range(i+1,N):
                if (price[i]+price[j]) % x==0:
                    if (i,j) not in resultSet:
                        resultSet.add((i,j))
                
        return len(resultSet)



# Test cases
solution = Solution()

# Test Case 1
x = 60
price = [31, 25, 85, 29, 35]
print(solution.getDiscountPairs(x, price))  # Expected Output: 3

# Test Case 2
x = 10
price = [10, 20, 30, 40]
print(solution.getDiscountPairs(x, price))  # Expected Output: 6

# Test Case 3
x = 5
price = [3, 8, 12, 17]
print(solution.getDiscountPairs(x, price))  # Expected Output: 4