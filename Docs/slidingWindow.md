# 2. **Sliding Window Technique:**

- Using a window that slides along the array or string to solve a problem.
- The window **keeps track of a subarray** or substring that satisfies certain conditions.
- The size and position of the window change as the algorithm progresses.
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

- 2 pointers **L and R start at 0 and then R loops until we need to do L+=1**
- May require additional **memory to store frequency maps**.
- window keep track of a subarray/substring that satisfies certain condition.
- The size and position of window changes.
- Problem example: Find longest susbstring without repeating chars or finding smallest subarray with a sum greater than a value.
- Purpose: optimization problems
- O(n)
- Maintains a window of fixed size that slides along the array on string.
