package linkedList;
/*You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1] */
/**
 * Definition for singly-linked list.
 * 
 */
class AddTwoNumbers.java {
    public class ListNode {
             int val;
           ListNode next;
             ListNode() {}
             ListNode(int val) { this.val = val; }
            ListNode(int val, ListNode next) { this.val = val; this.next = next; }
         }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        //for the new linkedlist need dummy node
        ListNode dummy = new ListNode();
        ListNode cur =dummy;
        int carry =0;
        while(l1!=null || l2!=null || carry!=0 ){
            int val1 = l1!=null? l1.val :0;
            int val2 = l2!=null ? l2.val :0;

            int sum = val1+val2 +carry;
            //cealn up sum in case >10
            carry = sum/10;
            sum = sum%10;
            
            ListNode sumNode =new ListNode(sum);
            cur.next = sumNode;
            cur= cur.next;
            //update l1 and l2 pointer
            l1 = l1!=null? l1.next:null;
            l2=l2!=null? l2.next:null;
        }
        return dummy.next;
    }
}
