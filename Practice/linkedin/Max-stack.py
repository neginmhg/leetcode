"""The "Max Stack" problem involves designing a data structure that supports the following operations efficiently:

Push: Push an element onto the stack.
Pop: Remove the element on the top of the stack.
Top: Get the top element of the stack.
PeekMax: Retrieve the maximum element in the stack.
PopMax: Remove the maximum element from the stack and return it.
Here's a concise explanation of how to implement a solution:

Approach
To handle these operations efficiently, especially PeekMax and PopMax, we can use two stacks:

Main Stack: To store the elements in the order they are pushed.
Max Stack: To keep track of the maximum values. This stack will store pairs of values where the second element is the maximum value up to that point in the Main Stack."""


from sortedcontainers import SortedDict

class Node:
    def __init__(self, val, prev = None):
        self.val = val
        self.prev = prev
        self.next = None
        
class MaxStack:
    def __init__(self):
        self.hash = SortedDict()
        self.root = None
        self.end = None
        
    def push(self, x: int) -> None:
        if not self.root:
            self.root = Node(x, None)
            self.end = self.root
        else:
            if not self.end: self.end = self.root
            self.end.next = Node(x, self.end)
            self.end = self.end.next
        if x not in self.hash:
            self.hash[x] = deque([self.end])
        else:
            self.hash[x].append(self.end)
        
    def pop(self) -> int:
        x = self.end.val
        self.end = self.end.prev
        if self.end: self.end.next = None;
        self.hash[x].pop()
        if not self.hash[x]: self.hash.pop(x);
        return x
    
    def top(self) -> int:
        return self.end.val
        
    def peekMax(self) -> int:
        return self.hash.keys()[-1]
    
    def popMax(self) -> int:
        x = self.hash.keys()[-1]
        topnode = self.hash[x].pop()
        if topnode.prev and topnode.next:
            p = topnode.prev
            n = topnode.next
            p.next = n
            n.prev = p
        if not topnode.prev:
            self.root = topnode.next
            if self.root:
                self.root.prev = None
        if not topnode.next:
            self.end = self.end.prev
            if self.end:
                self.end.next = None
        if not self.hash[x]:
            self.hash.pop(x)
        return x
            
            

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()









"""
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        # Push the element onto the main stack
        self.stack.append(x)
        # Update the max stack
        if self.max_stack:
            # Push the maximum of the current value and the top of the max stack
            self.max_stack.append(max(x, self.max_stack[-1]))
        else:
            self.max_stack.append(x)

    def pop(self) -> int:
        # Pop the element from the main stack and max stack
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        # Get the top element of the main stack
        return self.stack[-1]

    def peekMax(self) -> int:
        # Get the top element of the max stack
        return self.max_stack[-1]

    def popMax(self) -> int:
        # Retrieve the maximum element
        max_val = self.peekMax()
        buffer = []

        # Remove elements until the max element is found
        while self.top() != max_val:
            buffer.append(self.pop())

        # Remove the maximum element
        self.pop()

        # Push the elements back to the stack
        while buffer:
            self.push(buffer.pop())

        return max_val
"""