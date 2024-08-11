# Problems I studied

## Arrays:

- **contains-dup**
- **good-pair**
- **longest consecutice sequence** :since sorting has time complexity of NlogN , we cna use set to not only remove dups but also have o(1) lookup time
- **Group Angrams**: :since sorting has time complexity of NlogN , we cna use hashmap
  - Tuples are immutable and hashable, which makes them suitable as keys in a dictionary.
  - Lists, on the other hand, are mutable and not hashable, so they cannot be used as dictionary keys directly.
- **Top K frequent elements**:
  - brute force is using sort wich is NlogN - not good
  - next can be max Heap(heapify) but it is KlogN - not yet good
  - Bucket Sort with array length approach - log(N)
    - have hashmap to store frequency of each element
    - turn the hashmap to bucket sort
    - for loop from right to left until k frequent numbers are retireved

## 2 pointers

## sliding window

## Stack

- #### Valid parentheses:

  - Stack Initialization: stack = []
  - Mapping Dictionary: mapping = {')': '(', '}': '{', ']': '['}
  - Iteration: Opening brackets are pushed onto the stack.
  - Closing brackets trigger a pop operation and a check against the mapping dictionary.
  - Final Check: return not stack ensures that all opening brackets have been matched and the stack is empty.

- #### Min Stack:

  - Use two stacks to keep track of minimum values in constant time.
    - Main Stack (`self.stack`): Stores all elements.
    - Min Stack (`self.minStack`): Stores the minimum value at each level of the main stack.
  - Push:
    - Add value to `self.stack`.
    - Update `self.minStack` with the min of the new value and the top of `self.minStack`
  - Pop:
    - Remove the top element from both `self.stack` and `self.minStack`.
  - Top:
    - Return `self.stack[-1]`.
  - GetMin:
    - Return `self.minStack[-1]`

- #### Evaluate reverse polish notation - RPN
  - Use a Stack and iterator one by one
    - Push element onto the stack if not any of the operator
    - if element is (`+`, `-`, `*`, `/`):
      - Pop two numbers (a (first pop) and b(second pop))
      - Perform the op (order matters for `-` and `/`) => (b-a)
      - Push the result back onto the stack
  - Final Result
    - The stack's last item is the result
- #### Generate parenthesis

- ### dailyTemperatures

  - use monotonically decreasing stack
  - Initialize: Use a stack to store indices and an array `res` for results.
  - Iterate: For each temperature, pop from the stack until the current temperature is not greater than the temperature at the stack's top index.
    - top of stack should have coldest temp
  - Update Result: Set the result for each popped index to the difference between the current index and the popped index.
  - Push Index: Append the current index to the stack and continue.

- ### Car fleet:

  - Pair and Sort Combine car positions & speeds into pairs, then sort by position in descending order to handle cars starting from the furthest position first.
  - Calculate Time: Compute the time each car needs to reach the target using `(target - p) / s`.
  - Use a Stack: Track the time to reach the destination for the last car in each fleet using a stack; push a new time if it forms a new fleet.
    - no pops.
  - Count Fleets The number of unique times in the stack represents the number of car fleets arriving at the destination.
    - return len of stack

- ### Largest rectangle histogram:
  - Stack for Indices and Heights: Use a stack to keep track of bar indices and heights to efficiently calculate rectangle areas as heights decrease.
  - Pop and Calculate Areas: When encountering a shorter bar, pop from the stack and calculate possible rectangle areas using the height of the popped bar, updating the maximum area found.
  - Push Current Bar: Push the current bar's height and its starting index onto the stack, adjusting the starting index if necessary when popping bars.
  - Final Area Calculation: After processing all bars, calculate the area for any remaining bars in the stack, ensuring to consider rectangles extending to the end of the histogram.

## Binary search

- used for searching for a specific element in a sorted array.
- set up l=0 r=len(arr)-1 and mid =l+r//2 then while l<=r: condition to compare target with arr[mid], adjust l and r based on m+1 or m-1

## Linked List

- reverse linkedlist
  - have 2 pointers: prev=None and current=head
  - iterate (while current):
    - save current.next in nextNode
    - switch direction current.next=prev
    - move pointers: prev = current and current=nextNode
- merge 2sorted linked list in O(n):
  - one dummy node created (&saved as tail) for result
  - traverse both and compare vals
    - which ever smaller, save to dummy next
    - update list1/2 = list1/2.next
    - update result pointer tail=tail.next
  - once traverse done, then check if list1: else if list2
    - put the remaining in tail.next=list1 or tail.next=list2
- Reorder List
  - Find the Middle: Use the two-pointer technique (slow and fast pointers) to locate the middle of the linked list, splitting it into two halves.
  - Reverse the Second Half: Reverse the second half of the list in-place by changing the `next` pointers of its nodes.
  - Merge the Two Halves: Merge the first half and the reversed second half by alternately linking nodes from each half.
- Remove Nth node from end

  - Create Distance: Use two pointers (left and right) to create a gap of n nodes between them by moving the right pointer n steps ahead.
  - Traverse to End: Move both left and right pointers together until right reaches the end of the list. At this point, left will be right before the node to be removed.
  - Remove Node: Update the next pointer of left to skip the node to be removed, effectively deleting it from the list
    - left.next= left.next.next
  - Return Head: Return the modified list starting from dummy.next to handle edge cases like removing the head node.

- Deep copy a linked list:
  - Initialize hashmap
  - Iterate over the old linkedin list (cur=head):
    - Populate hashmap by creating new Node() for each old node
  - Again, Iterate over the old linked list ,set cur =head
    - this time get each new Node out of the map and set the connections:
      - .next and .random need to be set
  - Return map[head]
- Find cycle in linkedlist<br>
  `slow, fast =head, head` <br>
  `while fast and fast.next:`<br>
  `slow = slow.next`<br>
  `fast =fast.next.next`<br>
  `if slow == fast:`<br>
  ` return True`<br>
  `return False`<br>
  - Floyd's Tortoise and Hare algorithm, also known as the cycle detection algorithm, is a pointer algorithm that uses two pointers which move at different speeds to detect a cycle in a sequence of values. This algorithm is commonly used in problems involving linked lists to detect if there's a cycle in the list, but it can also be applied to other scenarios where cycle detection is needed.
