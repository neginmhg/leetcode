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
