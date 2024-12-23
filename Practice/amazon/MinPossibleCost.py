"""
Amazon Go Store Minimum Cost Problem

In an Amazon Go store, there are n items, each associated with 2 positive values a[i] and b[i]. There are infinitely many items of each type numbered from 1 to infinity, and the j-th item of the i-th type costs:

a[i]+(j-1)*b[i]

Note: each item of each type can be purchase at most once. 
Determine the minimum possible cost to purchase exactly m items. 


ex. 
Input:

n = 3
a = [2, 1, 1]
b = [1, 2, 3]
m = 4

the optimal types to buy are:
    - Choose type i = 1: This is the first purchase of this type, so j = 1. The cost of this item is:
            a[1]+(j-1)*b[i] =1+(1-1)*2=1
    - Choose type i = 2: This is the first purchase of this type, so j = 1. The cost of this item is:
            1 + (1-1)*3 =1
    - Choose type i = 0: This is the first purchase of this type, so j = 1. The cost of this item is:
            2 +(1-1)*1 =2
    - Choose type i = 0: This is the second purchase of this type, so j = 2. The cost of this item is:
            2+(2-1)*(1)=3

    - When a second item of any type is purchased, j=2. 
    - THE TOTAL COST to puchase 1+1+2+3 = 7 


Constraints:
1<=n<=10^5
1<=a[i],b[i]<=10^5
1<=m<=10^5
"""
from typing import List
import heapq
class Solution:
    def getminimumcost(self,a: List[int], b: List[int], m: int) -> int:
        heap =[]

        #populate heap for 1st time
        j=1
        for i in range(len(a)):
            cost= a[i]
            heapq.heappush(heap, (cost,i,j))
        

        totalCost=0

        #Select m items
        for _ in range(m):
            cost,i,j = heapq.heappop(heap)
            totalCost+=cost

            #push the next item of this type
            nextCost= a[i] + (j) * b[i]
            heapq.heappush(heap,(nextCost,i,j+1))
        return totalCost
    
solution = Solution()
n = 3
a = [2, 1, 1]
b = [1, 2, 3]
m = 4
print(solution.getminimumcost(a, b, m))  # Output: 7
