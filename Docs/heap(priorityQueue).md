### 1. Introduction to Heaps

#### What is a Heap?

A heap is:

1. a complete binary tree
2. one of 2 types: min heap or max heap
   A heap is a specialized tree-based data structure that satisfies the heap property:

- **Min-Heap**: The value of each node is greater than or equal to the value of its parent, with the smallest value at the root.
- **Max-Heap**: The value of each node is less than or equal to the value of its parent, with the largest value at the root.

Heaps are commonly implemented using arrays. For a node at index `i`:

- The left child is at `2*i + 1`
- The right child is at `2*i + 2`
- The parent is at `(i - 1) // 2`

#### Applications of Heaps

-- whenever you need the max or min value quickly

- **Priority Queues**: A priority queue is an abstract data type where each element has a priority. Elements are served based on their priority.
- **Heap Sort**: An efficient sorting algorithm with O(n log n) time complexity.
- **Dijkstra's Graph Algorithms**: Such as Dijkstra's shortest path and Prim's minimum spanning tree.

### 2. Using Heaps in Python

Python's `heapq` module provides an implementation of the min-heap.

#### Basic Operations with `heapq`

```python
import heapq

# Initialize an empty heap
heap = []

# Push elements into the heap
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
heapq.heappush(heap, 2)

# Pop the smallest element
print(heapq.heappop(heap))  # Output: 1

# Peek the smallest element without popping
print(heap[0])  # Output: 2

# Convert a list into a heap
arr = [3, 1, 4, 2]
heapq.heapify(arr)
print(arr)  # Output: [1, 2, 4, 3]
```

#### Max-Heap using `heapq`

Since `heapq` only supports min-heap, you can use negative values to simulate a max-heap.

```python
import heapq

# Initialize an empty max-heap
max_heap = []

# Push elements into the heap with negative values
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -2)

# Pop the largest element (remember to negate it back)
print(-heapq.heappop(max_heap))  # Output: 4
```

### 3. Solving LeetCode Problems with Heaps

Let's solve a common LeetCode problem using heaps.

#### Problem: Kth Largest Element in an Array

Find the kth largest element in an unsorted array.

**Example:**

```
Input: [3, 2, 1, 5, 6, 4], k = 2
Output: 5
```

**Approach:**

1. Use a min-heap to maintain the top `k` largest elements.
2. Iterate through the array, and for each element:
   - If the heap size is less than `k`, push the element into the heap.
   - If the heap size is `k`, push the element into the heap and pop the smallest element.
3. The root of the heap is the kth largest element.

```python
import heapq

def findKthLargest(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # Output: 5
```

### 4. Practice Problems

Here are some additional LeetCode problems to practice with heaps:

1. **Merge k Sorted Lists**: Merge `k` sorted linked lists and return it as one sorted list.
2. **Top K Frequent Elements**: Given a non-empty array of integers, return the `k` most frequent elements.
3. **Find Median from Data Stream**: The median is the middle value in an ordered integer list.

### Summary

- Understand the heap properties and how to use the `heapq` module in Python.
- Practice basic heap operations: push, pop, and heapify.
- Apply heap concepts to solve common LeetCode problems like finding the kth largest element.
