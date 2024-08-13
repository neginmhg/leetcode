""" [HARD]
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional
from ListNode import ListNode

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None

        def mergeSort(lists, start, end):
            if start == end: #If start equals end, it means there is only one list in the current range, so it returns that list directly.
                return lists[start]
            mid = (start + end) // 2
            left = mergeSort(lists, start, mid)
            right = mergeSort(lists, mid + 1, end)
            return mergeTwoLists(left, right)
        
        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            current = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            
            # Attach the remaining part if any list is non-empty
            if l1:
                current.next = l1
            elif l2:
                current.next = l2
            
            return dummy.next
        
        return mergeSort(lists, 0, len(lists) - 1)

            












"""def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a min-heap
        min_heap = []
        
        # Add the head of each linked list to the heap
        for l in lists:
            if l:
                tuple = (l.val, l)
                heapq.heappush(min_heap, tuple)
        
        # Create a dummy node to build the result list
        dummy = ListNode(0)
        current = dummy
        
        # While there are nodes in the heap
        while min_heap:
            # Get the smallest node
            val, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            
            # If the smallest node has a next node, add it to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, node.next))
        
        return dummy.next"""