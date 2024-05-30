"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore

        # Create a dummy node to serve as the starting point of the merged list
        dummy =ListNode() # type: ignore
        tail= dummy

        # Traverse both lists while both are non-empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next=list1 # Append the node from list1 to the merged list
                list1=list1.next    # Move to the next node in list1
            else:
                tail.next=list2      # Append the node from list2 to the merged list
                list2=list2.next        # Move to the next node in list2
            tail=tail.next      # Move the tail pointer
        
        # If there are remaining nodes in list1, append them
        if list1:
            tail.next=list1
        # If there are remaining nodes in list2, append them
        elif list2:
            tail.next=list2
        

         # The head of the merged list is the next node of the dummy
        return dummy.next
    
"""
The algorithm efficiently merges two sorted linked lists by iterating through both lists only once, resulting in an O(n) time complexity where n is the total number of nodes in both lists.
"""