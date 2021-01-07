package stack_and_queue;

import java.util.Stack;

public class LC_Offer_09 {

    Stack<Integer> stack1;
    Stack<Integer> stack2;

    public LC_Offer_09() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }

    public void appendTail(int value) {
        stack1.push(value);
    }

    public int deleteHead() {
        if (!stack2.isEmpty()) {
            return stack2.pop();
        }

        if (!stack1.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
            return stack2.pop();
        } else {
            return -1;
        }
    }
}
