# Linked Lists in Python

<div style="font-size:25px;">

## 1. Basics of Linked Lists

A linked list is a data structure where each element (node) contains a value and a reference (or link) to the next node in the sequence. The main types of linked lists are:

- **Singly Linked List**: Each node has a reference to the next node.
- **Doubly Linked List**: Each node has references to both the next and the previous nodes.
- **Circular Linked List**: The last node points back to the first node.

### Singly Linked List

Lets start by implementing a basic singly linked list:

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
```

## 2. Common Operations

- **Insertion**: You can insert a node at the beginning, middle, or end of the list.
- **Deletion**: You can remove a node by its value.
- **Traversal**: You can traverse the list to read or update values.

## 3. Tips and Tricks

### Understanding the Structure

- Visualize the nodes and their connections. Draw diagrams to understand the pointers and their changes.
- Use dummy nodes to simplify edge cases, especially for head manipulations.

### Edge Cases

- Empty list (head is `None`).
- Single element list.
- Deleting the head node.
- Handling cycles (circular linked lists).

### Efficient Coding

- Use a two-pointer technique for problems like finding the middle node or detecting cycles.
- Practice recursion for problems involving reverse or flattening lists.

## 4. Example LeetCode Problems

### Problem 1: Reverse a Linked List

```python
# Iterative approach
def reverseList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Recursive approach
def reverseListRecursive(head):
    if not head or not head.next:
        return head
    p = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return p
```

### Problem 2: Merge Two Sorted Lists

```python
# Iterative approach
def mergeTwoLists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

```

### Problem 3: Detect Cycle in a Linked List

```python
def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

<hr/><br/><hr/><br/><hr/>

# When to Use Linked Lists in LeetCode

Linked lists are a fundamental data structure that are especially useful in certain situations. Here are scenarios and problem types where using a linked list can be advantageous in solving LeetCode problems:

## 1. Dynamic Size and Frequent Insertions/Deletions

- **Use Case:** When you need a data structure that can grow or shrink dynamically, and you need to frequently insert or delete elements.
- **Reason:** Unlike arrays, linked lists do not require shifting elements when inserting or deleting, making operations like insertion and deletion \(O(1)\) when you have a pointer/reference to the node.

## 2. Constant Time Insertions/Deletions

- **Use Case:** When the problem involves a lot of insertions and deletions in the middle of the data structure.
- **Reason:** Arrays require shifting elements which is \(O(n)\), whereas linked lists can insert or delete nodes in \(O(1)\) if the position is known.

## 3. Iterating Over Nodes

- **Use Case:** When you need to iterate over elements and the order is important.
- **Reason:** Linked lists maintain order and allow sequential access.

## 4. Complex Data Structures

- **Use Case:** Implementing more complex data structures like stacks, queues, or even more complex structures like adjacency lists for graphs.
- **Reason:** Linked lists provide the flexibility needed for these structures.

## 5. Memory Efficient

- **Use Case:** When memory efficiency is crucial.
- **Reason:** Linked lists do not require contiguous memory allocation, which can be more efficient in certain scenarios.

## Common LeetCode Problems Involving Linked Lists:

1. **Reverse a Linked List** (e.g., [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/))
2. **Cycle Detection** (e.g., [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/))
3. **Merge Two Sorted Lists** (e.g., [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/))
4. **Remove Nth Node from End** (e.g., [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/))
5. **Add Two Numbers** (e.g., [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/))
6. **Copy List with Random Pointer** (e.g., [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/))
7. **Intersection of Two Linked Lists** (e.g., [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/))

## When Not to Use Linked Lists:

- **Random Access:** If you need frequent access to random elements, arrays (or array-based structures like dynamic arrays) are more suitable because they provide \(O(1)\) access time, whereas linked lists provide \(O(n)\) access time.
- **Memory Overhead:** If memory overhead is a concern (each element in a linked list requires additional storage for the pointer/reference).

## Summary:

Use linked lists on LeetCode when you need dynamic resizing, frequent insertions/deletions, or to implement other data structures. Avoid them when you need random access or minimal memory overhead. Practice common linked list problems to gain confidence in recognizing these scenarios during coding interviews.
