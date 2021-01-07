package stack_and_queue;

import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class LC_Offer_06 {

    public int[] reversePrint(ListNode head) {

        Stack<Integer> stack = new Stack<>();
        while (head != null) {
            stack.push(head.val);
            head = head.next;
        }

        int length = stack.size();

        int[] result = new int[length];

        for (int i = 0; i < length; i++) {
            result[i] = stack.pop();
        }

        return result;

    }

    public static void main(String[] args) {
        ListNode n3 = new ListNode(3);
        ListNode n2 = new ListNode(2);
        n2.next = n3;
        ListNode n1 = new ListNode(1);
        n1.next = n2;

        LC_Offer_06 lc = new LC_Offer_06();
        System.out.println(Arrays.toString(lc.reversePrint(n1)));

    }

}
