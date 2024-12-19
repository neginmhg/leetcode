"""
Given an array of points where points[i] = [xi, yi]
 represents a point on the X-Y plane and an 
 integer k, return the k closest points to 
 the origin (0, 0).

The distance between two points on the X-Y 
plane is the Euclidean distance 
(i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. 
The answer is guaranteed to be unique 
(except for the order that it is in).

 

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 
"""

#The distance formula between two points 
# ((x_1, y_1)) and ((x_2, y_2)) is:
# d = SQRT{  (x_2 - x_1)^2 + (y_2 - y_1)^2  }
from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Ege case: if K == size of points or there's 1 or 0 points
        if k == len(points) or len(points)==1 or len(points)==0:
            return points
        #if points is null
        if not points:
            return []
        hp = []
        for x,y in points:
            d = x**2 +y**2
            heapq.heappush(hp, [d,x,y])

        result=[]
        while k>0:
            d,x,y=heapq.heappop(hp)
            result.append([x,y])
            k-=1
        return result

#Why Sorting Isn't Used:
#Sorting all points would take O(nlogn), 
#but using a heap allows us to extract only the necessary k 
# points after inserting all points, which is more flexible for larger datasets.


#Space complexity: O(n)
#Time Complecity: O(n log n) for push and  O(k log n) for pop = O(n log n) cause k<n
