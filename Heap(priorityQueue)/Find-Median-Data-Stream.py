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
        self.small, self.large =[],[]
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1* num)
        #make sure every num in small is <= num in large
        if (self.small and self.large and -1*self.small[0]> self.large[0]):
            val=-1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        #uneven price
        if len(self.small) > len(self.large) +1:#if small gets too big
            val=-1*heapq.heappop(self.small) #pop from small
            heapq.heappush(self.large,val)  #push to large
        
        if len(self.large) > len(self.small) +1:#if large gets too big
            val=heapq.heappop(self.large)#pop from large
            heapq.heappush(self.small,-1*val)#push to small
    
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.large) >len(self.small):
            return self.large[0]
        return (self.large[0]+-1*self.small[0])/2  #if the size of small and large are equal then calculate the median





# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()