"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

"""
from typing import List
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Create Adjacency List
        edge = defaultdict(list)
        for u,v,w in times:
            edge[u].append((w,v))       #(time, node)
        
        #Visit Set
        visit=set()
        
        #Result time
        t=0

        #minHeap for Dijkastra's Algo
        minHeap=[(0,k)]

        while minHeap:
            #pop minimum time
            w1 ,n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t,w1)
            #check neighbors
            for w2,n2 in edge[n1]:
                if n2 in visit:
                    continue
                heapq.heappush(minHeap,(w1+w2, n2))

        return t if len(visit)==n else -1
    
# Time complexity:  O((E + V) log V)
# O(log V) comes from heap operations (push and pop)  
# and the O(E) accounts for processing all edges.

"""We use Dijkstra's Algorithm to find the shortest paths from the starting node to all 
other nodes in the graph. The algorithm is efficient for this problem because it works 
well for graphs with non-negative edge weights (like our times array)"""