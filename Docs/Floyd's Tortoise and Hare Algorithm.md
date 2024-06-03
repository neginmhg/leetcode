# Floyd's Tortoise and Hare Algorithm

The Floyd's Tortoise and Hare algorithm, also known as the cycle detection algorithm, is a pointer algorithm that uses two pointers which move at different speeds to detect a cycle in a sequence of values. This algorithm is commonly used in problems involving linked lists to detect if there's a cycle in the list, but it can also be applied to other scenarios where cycle detection is needed.

## Explanation

1. **Initialization**:

   - You have two pointers, `slow` (the tortoise) and `fast` (the hare).
   - Both pointers start at the beginning of the sequence.

2. **Movement**:

   - In each step, the `slow` pointer moves one step forward.
   - The `fast` pointer moves two steps forward.

3. **Cycle Detection**:
   - If there is a cycle, the `fast` pointer will eventually meet the `slow` pointer within the cycle.
   - If the `fast` pointer reaches the end of the sequence (i.e., it encounters a `None`), then there is no cycle.

## Example: Detecting a Cycle in a Linked List

Let's consider a linked list node structure and an implementation of the cycle detection algorithm:

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    if not head:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next         # Move slow by one step
        fast = fast.next.next    # Move fast by two steps

        if slow == fast:         # Cycle detected
            return True

    return False                # No cycle detected

# Example usage:
# Creating a linked list with a cycle
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a cycle

print(has_cycle(node1))  # Output: True
```

## reason why both pointers meet:

Once both pointers are inside the cycle, each step reduces the distance between them by one node because fast catches up to slow faster than slow can move away.
Since the number of nodes in the cycle is finite, slow and fast will eventually meet.
