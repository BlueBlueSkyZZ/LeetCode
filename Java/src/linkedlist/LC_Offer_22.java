package linkedlist;

public class LC_Offer_22 {

    public ListNode getKthFromEnd(ListNode head, int k) {
        ListNode post, prev;
        post = prev = head;
        while (k-- != 0) {
            post = post.next;
        }
        while (post != null) {
            post = post.next;
            prev = prev.next;
        }
        return prev;
    }

}
