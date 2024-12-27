"""
Amazon sellers sometimes provide a link to documentation about a product they are offering. Documentation is usually large, so it is broken into an even number of volumes for download.
Each volume:
Is stored in a node instance as a SinglyLinkedListNode.
Has a page count stored in data.
Has a pointer to the next volume stored in next.
A customer will read the first and last volumes each day, removing the volumes from the list after reading them.
Task:
Given a reference to the head of a singly-linked list, calculate the maximum number of pages read on any day.
Notes:
Try to create a solution that has a space complexity of O(1).
Example:

The linked list is as follows:
1 -> 4 -> 3 -> 2

On the first day, the customer reads the volumes with page counts 1 and 2, and removes them from the list. The number of pages read on the first day is 
1+2=3.
The new list is:
4 -> 3




"""

# Data Structure/Algorithm: Singly Linked List + Two Pointer Technique
# Optimized solution to find the maximum number of pages read on any day.

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMaxDailyPages(head):
    """
    Optimized function to calculate the maximum number of pages read on any day.
    Uses the two-pointer technique with a single traversal of the list.
    """
    # Base case: If the list is empty or has one node
    if not head:
        return 0
    if not head.next:
        return head.data

    max_pages = 0  # Tracks the maximum pages read in a single day

    # Step 1: Find the middle and reverse the second half of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the list
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # Step 2: Traverse both halves of the list
    first, second = head, prev
    while second:
        # Calculate the pages read today
        pages_today = first.data + second.data
        max_pages = max(max_pages, pages_today)

        # Move pointers forward
        first = first.next
        second = second.next

    return max_pages

# Complexity Analysis
# Time Complexity: O(n), as we traverse the list twice (once to reverse, once to calculate sums).
# Space Complexity: O(1), as no additional data structures are used.
