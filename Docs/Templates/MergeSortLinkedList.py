class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def merge_sort(head):
    if not head or not head.next:
        return head

    # Find the middle point to divide the list into two halves
    mid = get_middle(head)
    next_to_mid = mid.next
    mid.next = None

    # Apply merge_sort to the two halves
    left = merge_sort(head)
    right = merge_sort(next_to_mid)

    # Merge the sorted halves
    sorted_list = merge(left, right)
    
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(l1, l2):
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

    current.next = l1 if l1 else l2
    
    return dummy.next
