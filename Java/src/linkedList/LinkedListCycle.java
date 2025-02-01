package linkedList;
import linkedList.ListNode;
public class LinkedListCycle {
    public static boolean hasCycle(ListNode head){
        //edge case
        //if no node or 1 node
        if(head==null || head.next==null){
            return false;
        }
        ListNode slow=head;
        ListNode fast =head;

        while(fast!=null && fast.next!=null){
            slow= slow.next;
            fast = fast.next.next;
            if(slow==fast){
                return true;
            }
        }
        return false;    // If fast reaches null, there's no cycle
    }
}
