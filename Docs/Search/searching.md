### Key Points:

- **Binary Search**: Efficient for searching in a sorted array, with logarithmic time complexity in all cases.
- **Quick Select**: Average-case linear time complexity, but can degrade to quadratic in the worst case. Space complexity is minimal.
- **2 Pointer**: Linear time complexity suitable for many problems involving arrays or linked lists.
- **Sliding Window**: Linear time complexity, efficient for subarray or substring problems.

| Algorithm          | Average Time Complexity | Best Time Complexity | Worst Time Complexity | Space Complexity |
| ------------------ | ----------------------- | -------------------- | --------------------- | ---------------- |
| **Binary Search**  | O(log n)                | O(log n)             | O(log n)              | O(1)             |
| **Quick Select**   | O(n)                    | O(n)                 | O(n^2)                | O(1)             |
| **2 Pointer**      | O(n)                    | O(n)                 | O(n)                  | O(1)             |
| **Sliding Window** | O(n)                    | O(n)                 | O(n)                  | O(1)             |

### **1. Binary Search**

- **Use When**:

  - You have a **sorted array** or list, and you need to find the position of a target value or check for its existence.
  - The problem involves **searching for a specific value** in a sorted data structure.
  - You are given a **search space that can be represented as a sorted array** (e.g., searching for the first or last occurrence of a value).

- **Examples**:
  - Finding an element in a sorted array.
  - Finding the smallest element greater than or equal to a given value.
  - Finding the square root of a number using binary search.

### **2. Quick Select**

- **Use When**:

  - You need to **find the k-th smallest or largest element** in an unsorted array.
  - The problem involves **order statistics** rather than just searching for an exact value.
  - You need an efficient solution for selecting elements by rank in an unordered list.

- **Examples**:
  - Finding the median of an unsorted array.
  - Finding the k-th smallest element in an array.

### **3. 2 Pointer Technique**

- **Use When**:

  - You are working with **sorted arrays** or lists and need to find pairs or subarrays with specific properties (e.g., two numbers that sum to a target).
  - You need to **optimize the solution** to avoid nested loops by using two pointers moving from opposite ends or in the same direction.
  - The problem involves finding a pair or subset that meets certain criteria within a linear scan.

- **Examples**:
  - Finding two numbers in a sorted array that add up to a specific target.
  - Merging two sorted arrays.
  - Checking if a string is a palindrome by comparing characters from both ends.

### **4. Sliding Window**

- **Use When**:

  - You need to find or optimize solutions for **subarrays** or **substrings** of varying or fixed sizes.
  - The problem involves **calculating properties** of contiguous subarrays or substrings (e.g., maximum sum, average, longest substring with distinct characters).
  - You need to efficiently process ranges or windows of elements within an array or string.

- **Examples**:
  - Finding the maximum sum of a contiguous subarray of size k.
  - Finding the longest substring without repeating characters.
  - Finding the smallest window in a string that contains all characters of another string.

### Summary:

- **Binary Search**: Use for searching in sorted data.
- **Quick Select**: Use for finding the k-th smallest or largest element in unsorted data.
- **2 Pointer Technique**: Use for problems involving pairs or ranges in sorted arrays or lists.
- **Sliding Window**: Use for problems involving contiguous subarrays or substrings.

If you have specific LeetCode problems you’re tackling, I can help match these techniques to those problems more precisely!
