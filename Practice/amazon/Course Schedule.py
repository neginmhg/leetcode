"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
#1.  Adjacency list needed
#2. visit array of size numcourses
#3. DFS to explore neigbors
#First solution: DFS iwth visit array
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a map to store the list of prerequisites (neighbors) for each course
        neighborMap = { i :[] for i in range(numCourses)}
        
        # Populate the map with the prerequisites for each course
        for course, prereq in prerequisites:
            neighborMap[course].append(prereq)
        
        # Track the visit state of each node (0 = unvisited, 1 = visiting, 2 = visited)
        visitState = [0] * numCourses # index:course | value:status

        # Function to detect a cycle in the course dependency graph
        def DetectCycle(course):
            # Base case: If the course is currently being visited, a cycle is detected
            if visitState[course] == 1:
                return False
            
            # If the course has already been fully visited, no need to check again
            if visitState[course] == 2:
                return True
            
            # Mark the course as being visited
            visitState[course] = 1
            
            # Perform DFS on all neighbors (prerequisite courses)
            for n in neighborMap[course]:
                noCycle = DetectCycle(n)
                # If a cycle is detected in any neighbor, return False
                if not noCycle:
                    return False
            
            # Mark the course as fully visited
            visitState[course] = 2
            return True
        
        # Check each course to see if there's a cycle
        for c in range(numCourses):
            noCycle = DetectCycle(c)
            # If a cycle is detected, return False
            if not noCycle:
                return False
            
        # If no cycles are detected in any course, return True
        return True

# Solution #2 : Kahn Algorithm -Topological Sort
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #adj list
        adjList = {i:[] for i in range(numCourses)}
        indegree =[0]*numCourses
        for second, first in prerequisites:
            adjList[first].append(second)
            indegree[second]+=1
        

        queue = deque([i for i in range(numCourses) if indegree[i]==0])
        visited =0

        while queue:
            node = queue.popleft()
            visited +=1
            for nei in adjList[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        
        return visited ==numCourses