package stack_and_queue;

import java.util.Stack;

public class LC_Offer_30 {

    Stack<Integer> stack1;
    Stack<Integer> stack2;

    /** initialize your data structure here. */
    public LC_Offer_30() {

        stack1 = new Stack<>();
        stack2 = new Stack<>();

    }

    public void push(int x) {

        stack1.push(x);
        if (stack2.isEmpty() || x <= stack2.peek()) {
            stack2.push(x);
        }

    }

    public void pop() {

        int popItem = stack1.pop();
        if (popItem == stack2.peek()) {
            stack2.pop();
        }

    }

    public int top() {
        return stack1.peek();
    }

    public int min() {
        return stack2.peek();
    }

}
