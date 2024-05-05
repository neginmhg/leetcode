The terms "two pointers" and "sliding window" are often used interchangeably in algorithmic contexts, but they refer to slightly different concepts. Here's a breakdown of each:

# 1. **Two Pointers Technique:**

- The two pointers technique involves using two pointers to solve a problem. These pointers typically start at different positions and move through the array or string in some way.
- Two pointers are often used to find a certain subsequence or to solve problems where we need to compare elements in the array or string in a specific way.
- Examples of problems that can be solved using the two pointers technique include finding pairs in a sorted array that sum up to a target value or determining if a string is a palindrome.
- https://interviewing.io/two-pointers-interview-questions

# 2. **Sliding Window Technique:**

- The sliding window technique involves using a window that slides along the array or string to solve a problem.
- The window keeps track of a subarray or substring that satisfies certain conditions. The size and position of the window change as the algorithm progresses.
- Sliding window is often used to solve optimization problems, especially those that involve finding a maximum or minimum value among all possible subarrays or substrings.
- Examples of problems that can be solved using the sliding window technique include finding the longest substring without repeating characters or finding the smallest subarray with a sum greater than or equal to a given value.
- How to Identify Sliding Window Problems:
  These problems generally require Finding Maximum/Minimum Subarray, Substrings which satisfy some specific condition.
  The size of the subarray or substring ‘K’ will be given in some of the problems.
  These problems can easily be solved in O(N2) time complexity using nested loops, using sliding window we can solve these in O(n) Time Complexity.
  Required Time Complexity: O(N) or O(Nlog(N))
  Constraints: N <= 106 , If N is the size of the Array/String.
  - https://www.geeksforgeeks.org/window-sliding-technique/

In summary, while the two pointers technique involves using two pointers to traverse the array or string, the sliding window technique involves using a window that moves along the array or string to solve optimization problems. However, both techniques can be used together in certain situations, and the distinction between them can sometimes be blurred.

# 3. **Monotonically Decreasing Stack**

### Overview

A monotonically decreasing stack is a data structure commonly used in algorithmic problem-solving. It maintains a stack of elements where each element is smaller than the elements above it, resulting in a decreasing order from bottom to top.

### Properties

- **Decreasing Order**: Elements in the stack are stored in decreasing order, with the smallest element at the top.

- **Efficient for Finding Next Greater/Smaller Elements**: It efficiently finds the next greater or smaller element for each element in an array or list.

### Steps to Implement

1.  **Initialize an Empty Stack**: Start with an empty stack.
2.  **Iterate Through the Array/List**: For each element in the array/list:
    - Compare the current element with the top element of the stack.
    - If the current element is smaller, push it onto the stack.
    - If the current element is larger, pop elements from the stack until the condition is met, then push the current element onto the stack.
3.  **Process Remaining Elements**: After iterating through all elements, any remaining elements in the stack can be processed as necessary.

### Example Applications

1.  **Next Greater Element**: Find the next greater element for each element in an array.
2.  **Next Smaller Element**: Find the next smaller element for each element in an array.
3.  **Temperature Problems**: Find the next warmer temperature for each day in a list of temperatures.

### Implementation in Python

```python
stack = []
for current_element in elements:
   while stack and condition(stack[-1], current_element):
      stack.pop()
   stack.append(current_element)
```

#### In the implementation, `condition` is a function that determines whether to pop elements from the stack based on the comparison between the top element of the stack and the current element being processed.
