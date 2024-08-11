"""[easy]
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore


        # ---- we need 2 pointers prev and current ------
        prev = None      # Initialize previous pointer to None
        current = head  # Initialize current pointer to the head of the list
        
        # Traverse the list
        while current:
            # Store the next node
            next_node = current.next
            
            #reverse direction
            current.next = prev # Reverse the current node's pointer
            
            #---- move pointers ------
            prev = current    # Move the prev pointer to the current node
            current = next_node # Move the current pointer to the next node
        


        # At the end, prev will be the new head of the reversed list
        return prev