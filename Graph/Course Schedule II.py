"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct
"""
#To solve this problem, we need to determine a valid order to complete the courses based on the prerequisites. This problem is essentially about finding a topological order in a directed graph, where nodes represent courses and edges represent prerequisites. If there's a cycle in the graph, it's impossible to complete all courses, so we should return an empty array.
from typing import List
from collections import defaultdict,deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #map for adjacent/neighbor 
        neighborMap = defaultdict(list)
        #list for incoming degrees
        inDegrees=[0] * numCourses

        #populate neighborMap and inDegrees
        for dest,src in prerequisites:
            neighborMap[src].append(dest)
            inDegrees[dest] +=1
        
        #queue to order courses
        resultOrder = []
        q = deque([i for i in range(numCourses) if inDegrees[i]==0])
        
        while q:
            course=q.popleft()
            resultOrder.append(course)
            for neighbor in neighborMap[course]:
                inDegrees[neighbor] -=1
                if inDegrees[neighbor]==0:
                    q.append(neighbor)
        

         # Step 4: Check if we have a valid topological ordering
        if len(resultOrder) == numCourses:
            return resultOrder
        else:
            return []