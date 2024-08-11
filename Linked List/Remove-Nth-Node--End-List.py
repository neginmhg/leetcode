"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""



from ListNode import ListNode
from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode(0, head)
        left =dummy
        right = head

        "Step 1: Loop to create distance between left and right"
        #create a distance in size n between left and right pointer
        #move the right pointer n times
        while n>0 and right:
            right=right.next
            n -=1
        
        
        "Step 2 : loop to move both pointers to the end of list"        
        #now move both left and right until we reach the end of list
        while right:
            left=left.next
            right=right.next
        
        "Step 3: now left.next is node that needs to be dislinked from the list"     
        #delete
        left.next=left.next.next        #update the pointer in left.next to left.next.next
        #this make sures 1 node is skipped/removed from list 
        return dummy.next       #return the head of the list