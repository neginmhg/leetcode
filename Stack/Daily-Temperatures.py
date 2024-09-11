"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #We can use a stack to keep track of the indices of temperatures we've encountered so far. We'll maintain a monotonically decreasing stack, meaning the temperatures in the stack will be in decreasing order from bottom to top.
        # we need result to store the differenes
        # we need stack to do computations - will be a pair
        # top of the stack is stack[-1]
        res= [0] * len(temperatures)
        stack=[] #par [temp, index]
        for i in range(len(temperatures)):
            print("\nAt == "+str(i))
            print(" stack is = "+str(stack))
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_index=stack.pop() 
                print("found a bigger num"+str(temperatures[i]))
                res[prev_index]=(i-prev_index)
            print("appending to stack "+str(i))
            stack.append(i)
        return res



    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        res = [0] *len(temperatures)
        stack = []  #[temp, index]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                colderTeemp, colderIndex=stack.pop()
                diff = i-colderIndex
                res[colderIndex]=diff
            stack.append([t,i])
        return res

s=Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))


"""
This is a popular argorithm:

for i in range(len(array)):
    while stack and condition(array[i] and array[stack[-1]]):
        stack_val=stack.pop() 
        //something here
    stack.append(val)

"""