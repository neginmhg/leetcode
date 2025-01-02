"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100≈
"""
from typing import List
from collections import Counter, deque
import heapq

from collections import deque
from typing import Counter, List
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count each task and store the counts in a hashmap (Counter)
        count = Counter(tasks)

        # Create a max heap by negating the counts (since heapq is a min heap by default)
        maxHeap = [-cnt for cnt in count.values()]

        # Convert the list into a heap (priority queue)
        heapq.heapify(maxHeap)

        # Initialize time counter
        time = 0

        # Queue to track count of task and the next available time it can be executed
        # Pairs of [-cnt, idleTime]
        q = deque()

        # While there are tasks waiting to be processed in the maxHeap or in the queue
        while maxHeap or q:
            # Increment time at each step
            time += 1

            # If there are tasks in the maxHeap, process the most frequent task
            if maxHeap:
                # Remove the task with the highest count from the heap
                cnt = 1 + heapq.heappop(maxHeap)  # Increment cnt since we use negative counts

                # If there are still instances of this task left, add it to the queue with its next available time
                if cnt != 0:
                    q.append([cnt, time + n])

            # If the task at the front of the queue is ready to be processed (its idle time is up)
            if q and q[0][1] == time:
                # Push the task count back into the maxHeap to be processed again
                heapq.heappush(maxHeap, q.popleft()[0])

        # Return the total time taken to complete all tasks
        return time


"""
- Max-Heap: 
    This holds the tasks that are ready to be processed (i.e., tasks that can be executed now because their cooldown period has passed).
- Queue (or Cooldown list):
    This holds tasks that aren't ready to be processed yet because they are still within their cooldown period. These tasks will only be added back to the max-heap once their cooldown expires
"""      

# Example usage
s = Solution()
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
output = s.leastInterval(tasks, n)
print(output)  # Output: 8

