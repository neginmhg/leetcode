from collections import defaultdict, deque
class Solution:
    def topSort(self, graph):
        #1. Indegree {node:2} population
        inDegree= defaultdict(int)
        for node in graph:
            for nei in graph[node]:
                inDegree[nei]+=1
        
        res=[]
        #2. quueue
        q = deque([node for node in graph if inDegree[node]==0])
        #3. while q pop q
        while q:
            node =q.popleft()
            res.append(node)

            #for each nei  , -1 degree and push to q if independent
            for nei in graph[node]:
                inDegree[nei]-=1
                if inDegree[nei]==0:
                    q.append(nei)

        return res