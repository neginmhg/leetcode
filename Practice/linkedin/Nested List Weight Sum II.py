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
from typing import List
from collections import defaultdict, deque
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = 1
        sum_of_elements = 0
        queue = deque(nestedList)
        depth = 0
        res = 0

        while queue:
            depth += 1
            max_depth = max(max_depth, depth)
            for _ in range(len(queue)):
                nested = queue.popleft()
                if nested.isInteger():
                    val = nested.getInteger()
                    res -= val * depth
                    sum_of_elements += val
                elif nested.getList():
                    queue.extend(nested.getList())
        res += sum_of_elements * (max_depth + 1)
        return res

#time complexity : O(n)
#space complexity: O(n)

"""
The `extend` method in Python is used to add multiple elements to a list (or any collection that supports it, like a deque). When you call `list.extend(iterable)`, it appends each element from the `iterable` to the end of the list.

### Example:
Here's a quick demonstration:

```python
# Using a list
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Using a deque
from collections import deque
my_deque = deque([1, 2, 3])
my_deque.extend([4, 5, 6])
print(my_deque)  # Output: deque([1, 2, 3, 4, 5, 6])
```

### Key Points:
- **Add Elements**: It adds each element from the provided iterable to the end of the list or deque.
- **In-place Modification**: Unlike `append`, which adds the entire iterable as a single element, `extend` iterates through the iterable and adds each element individually.
- **No Return Value**: The `extend` method modifies the list in place and returns `None`.

In the context of your code, using `extend` allows you to add all the elements of a nested list to the queue in one operation, making it efficient for processing each level of the nested structure.
"""