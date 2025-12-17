/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode final_head;
        ListNode final_ptr;
        ListNode l1_ptr = list1;
        ListNode l2_ptr = list2;

        // null check
        if (list2 == null){
            return list1;
        }
        if (list1 == null){
            return list2;
        }

//        Determine node to start from
        if (list2.val < list1.val) {
            final_head = list2;
            l2_ptr = list2.next;
        } else {
            final_head = list1;
            l1_ptr = list1.next;
        }
        final_ptr = final_head;

//        Iterate through lists and splice together
        while (l1_ptr != null && l2_ptr != null) {
            if (l2_ptr.val > l1_ptr.val) {
                final_ptr.next = l1_ptr;
                l1_ptr = l1_ptr.next;
                final_ptr = final_ptr.next;
            } else {
                final_ptr.next = l2_ptr;
                l2_ptr = l2_ptr.next;
                final_ptr = final_ptr.next;
            }
        }

//        Check for unfinished list
        if (l2_ptr != null) {
            final_ptr.next = l2_ptr;
        }

        if (l1_ptr != null) {
            final_ptr.next = l1_ptr;
        }

        return final_head;
    }
}