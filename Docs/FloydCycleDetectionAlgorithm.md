## Floyd's Tortoise and Hare Algorithm

Floyd's Tortoise and Hare algorithm, also known as Floyd's cycle-finding algorithm, is a pointer algorithm used to detect cycles in a linked list. It was proposed by Robert W. Floyd in 1967.

### Concept

The algorithm uses two pointers, often referred to as the "tortoise" and the "hare", which move through the linked list at different speeds. The tortoise moves one step at a time, while the hare moves two steps at a time.

1. **Detection of Cycle**: If there's a cycle in the linked list, eventually the hare will meet the tortoise within the cycle. This is because the hare moves faster and will catch up with the tortoise eventually if there's a cycle.

2. **Finding the Entrance of the Cycle**: Once the cycle is detected, resetting one pointer to the beginning of the list and moving both pointers at the same speed will eventually lead them to the entrance of the cycle. This is a consequence of mathematical analysis and is not immediately intuitive.

### Application

Floyd's Tortoise and Hare algorithm is not only applicable to linked lists but can also be adapted to solve various problems, including finding duplicate elements in an array, as long as the problem can be modeled as having a cycle.

### Complexity Analysis

- Time Complexity: O(N), where N is the number of elements in the linked list or the array.
- Space Complexity: O(1), as only a constant amount of extra space is required.

### Pseudocode

```
tortoise = head
hare = head

while True:
    tortoise = tortoise.next
    hare = hare.next.next

    if tortoise == hare:
        break

tortoise = head
while tortoise != hare:
    tortoise = tortoise.next
    hare = hare.next

return tortoise  // or hare, both will point to the entrance of the cycle

```

## Typcal Scenario:

Given HEAD of the LinkedList, determine if it has a CYCLE.
Return the node where the cycle starts.

This return the end node if there are no cycles

```python
ListNode current=head
while current != NULL:
    current = current.next
return current
```

<hr/>

### Does the LinkedList have a cycle?

```python
  def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast =head, head
        while fast and fast.next:
            slow = slow.next
            fast =fast.next.next
            if slow == fast:
                return True
        return False
```
