package linkedlist;

public class LC_Offer_25 {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }

        if (l1.val <= l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        } else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }


    public ListNode mergeTwoLists2(ListNode l1, ListNode l2) {
        ListNode prevHead = new ListNode(-1);
        ListNode prev = prevHead;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                prev.next = l1;
                prev = l1;
                l1 = l1.next;
            } else {
                prev.next = l2;
                prev = l2;
                l2 = l2.next;
            }
        }

        prev.next = (l1 == null) ? l2 : l1;

        return prevHead.next;
    }

}
