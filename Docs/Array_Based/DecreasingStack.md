# 3. **Monotonically Decreasing Stack**

### visualization:

Bottom of stach(Biggest) [ [ ] .. [ ] .. [ ] .. [ ] .. [ ] ] Top of stack(Tiny)

### Overview

<h2>Smallest element at the top.</h2>

It maintains a stack of elements where each element is smaller than the elements above it, resulting in a decreasing order from bottom to top.

### Properties

- **Decreasing Order**: Elements in the stack are stored in decreasing order, with the smallest element at the top.

- **Efficient for Finding Next Greater/Smaller Elements**: It efficiently finds the next greater or smaller element for each element in an array or list.

### Steps to Implement

1.  **Initialize an Empty Stack**: Start with an empty stack.
2.  **Iterate Through the Array/List**: For each element in the array/list:
    - Compare the current element with the top element of the stack.
    - If the current element is smaller, push it onto the stack.
    - If the current element is larger, pop elements from the stack until the condition is met, then push the current element onto the stack
      (this ensures the biggest always resides at the bottom ).
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
      stack.pop()    #ex:  pop whenever current_element is bigger than top of the stack
   stack.append(current_element)
```

#### In the implementation, `condition` is a function that determines whether to pop elements from the stack based on the comparison between the top element of the stack and the current element being processed.
