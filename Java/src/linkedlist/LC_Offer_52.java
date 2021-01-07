package linkedlist;

public class LC_Offer_52 {

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

        if (headA == null || headB == null) {
            return null;
        }

        ListNode pointerA = headA;
        ListNode pointerB = headB;

        while (pointerA != pointerB) {
            pointerA = pointerA.next;
            pointerB = pointerB.next;

            if (pointerA == null && pointerB == null) {
                return null;
            }
            if (pointerA == null) {
                pointerA = headA;
            }
            if (pointerB == null) {
                pointerB = headB;
            }
        }

        return pointerA;
    }

    public ListNode getIntersectionNode2(ListNode headA, ListNode headB) {

        ListNode curA = headA;
        ListNode curB = headB;

        while (curA != curB) {
            curA = curA != null ? curA.next : headB;
            curB = curB != null ? curB.next : headA;
        }
        return curA;

    }

}
