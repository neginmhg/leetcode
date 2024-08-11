"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle
        #Use the two-pointer technique (slow and fast pointers) to find the middle of the linked list.
        #How it works: The slow pointer moves one step at a time, while the fast pointer moves two steps. By the time fast reaches the end, slow will be at the middle of the list.
        slow , fast = head, head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #reverse second half
        #Reverse the second half of the list starting from the node after the middle.
        #How it works: Use a standard list reversal technique. Iterate through the second half, reversing the links as you go. prev will eventually point to the new head of the reversed second half.
        second =slow.next #this is the middle point
        slow.next= None
        prev=None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        
        #merge 2 halfs
        first,second= head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2