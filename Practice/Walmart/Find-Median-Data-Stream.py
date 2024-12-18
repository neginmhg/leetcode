""" [HARD]
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
"""
#Use two heaps to efficiently maintain the order of numbers, with a max-heap for the lower half and a min-heap for the upper half, to quickly find the median.
"""
- Insertion: Both insertion and rebalancing operations are O(logn), making it efficient for large datasets.

- Median Finding: Finding the median is O(1) since it only requires accessing the roots of the heaps
"""
import heapq
class MedianFinder:

    def __init__(self):
        #small heap is maxHeap 
        #large heap is minHeap
        self.small ,self.large = [], []

    """O(log n)"""
    def addNum(self, num: int) -> None:
        #Push to small by default
        heapq.heappush(self.small, -1*num)
        #Check Peeks and see if they're correct
        if self.small and self.large and (-1)*self.small[0] > self.large[0]:
            #Pop from small
            peek=heapq.heappop(self.small)
            #Push it to large
            heapq.heappush(self.large, (-1)*peek)
        
        #Check if size of small is TOO BIG
        if len(self.small)> len(self.large) +1:
            #Pop from small
            peek=heapq.heappop(self.small)
            #Push it to large
            heapq.heappush(self.large, (-1)*peek)
        
        #Check if size of large is TOO BIG
        if len(self.large)> len(self.small) +1:
            peek = heapq.heappop(self.large)
            heapq.heappush(self.small, (-1)*peek)

    """O(1)"""
    def findMedian(self) -> float:
        #Edge case
        if not self.small and not self.large:
            raise ValueError("No numbers added yet")

        if len(self.small) >len(self.large):
            return (-1)*(self.small[0])
        elif len(self.large) >len(self.small):
            return (self.large[0])
        else:
            return ((-1)*(self.small[0]) + (self.large[0]))/2
        

        


# Time Complexity
    #   Each insertion or removal from a heap takes O(log n)
    #   Accessing the root of a heap is O(1)


#Space Complexity
# Two heaps  large and small have n elements : O(n)

"""
Edge Cases:
   - No numbers added.
   - Single number.
   - Odd vs. even numbers.
   - Duplicate numbers.
   - Sorted input (ascending/descending).
   - Large range of numbers.
"""