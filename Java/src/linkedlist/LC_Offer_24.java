package linkedlist;

public class LC_Offer_24 {

    public ListNode reverseList(ListNode head) {

        ListNode new_head = null;
        ListNode now_pointer = head;
        ListNode temp;
        while (now_pointer != null) {
            temp = now_pointer;
            now_pointer = now_pointer.next;
            temp.next = new_head;
            new_head = temp;
        }
        return new_head;
    }

}
