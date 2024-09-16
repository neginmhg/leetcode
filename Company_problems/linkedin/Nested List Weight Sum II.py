"""
The problem statement for **Nested List Weight Sum II** is as follows:

### Problem Statement:
You are given a nested list of integers, represented as `NestedInteger`. Each element is either an integer or a list whose elements may also be integers or other lists.

The **depth** of each integer is determined by how many levels of lists it is inside. For example, the integer `1` in `[[1,1],2,[1,1]]` has a depth of 2, while the integer `2` has a depth of 1.

Write a function to return the **inverse depth sum** of this nested list. The **inverse depth sum** is defined as the sum of each integer multiplied by its inverse depth. That is, the deeper the integer is, the less weight it has.

### Example 1:

```
Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a depth of 1, one 2 with a depth of 2.
Inverse depth sum = (1*1 + 1*1 + 2*2 + 1*1 + 1*1) = 8.
```

### Example 2:

```
Input: nestedList = [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3.
Inverse depth sum = (1*3 + 4*2 + 6*1) = 17.
```

### Constraints:
- The total number of integers in the nested list is in the range `[1, 50]`.
- The depth of the nested list is less than or equal to 50.
"""
#step1: traverse get the max depth
#step2: traverse again andd calculate the invers sum
from typing import List
from collections import defaultdict, deque
class Solution:
    def depthSumInverse(self,nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0
        maxDepth=0
        depthSumMap=defaultdict(int) #depth:sum
        q = deque([(nestedList, 1)])
        #O(n)
        while(q):
            currentList, depth=q.popleft()
            maxDepth=max(depth,maxDepth)
            for element in currentList:
                if element.isInteger():
                    # Add to depth sum map if element is an integer
                    depthSumMap[depth] = depthSumMap.get(depth, 0) + element.getInteger()
                else:
                    # If element is a list, enqueue it with incremented depth
                    q.append((element.getList(), depth + 1))
        
        result=0
        for d in depthSumMap:   #O(d)
            s= depthSumMap[d]
            result += s*(maxDepth-d+1)
        return result


#time complexity : O(n+d) since d<n ~ O(n)
#space complexity: O(n+d) since d<n ~ O(n)

#tricks: BFS, map, queu, isInteger()