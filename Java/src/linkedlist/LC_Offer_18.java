package linkedlist;


public class LC_Offer_18 {

    public ListNode deleteNode(ListNode head, int val) {
        ListNode prev = head;
        ListNode now_pointer = head;
        while (now_pointer.val != val) {
            prev = now_pointer;
            now_pointer = now_pointer.next;
        }

        if (now_pointer == head) {
            head = now_pointer.next;
            now_pointer.next = null;
        } else {
            prev.next = now_pointer.next;
            now_pointer.next = null;
        }
        return head;

    }

}
