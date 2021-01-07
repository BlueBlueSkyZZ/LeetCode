package stack_and_queue;

import java.util.Stack;

public class LC_Offer_31 {

    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int push_index = 0, pop_index = 0;
        int push_length = pushed.length, pop_length = popped.length;

        Stack<Integer> stack = new Stack<>();

        while (push_index < push_length || pop_index < pop_length) {
            if (stack.isEmpty() || (stack.peek() != popped[pop_index] && push_index < push_length)) {
                stack.push(pushed[push_index]);
                push_index++;
            } else if (pop_index < pop_length && stack.peek() == popped[pop_index]) {
                stack.pop();
                pop_index++;
            } else {
                break;
            }
        }

        return push_index == push_length && pop_index == pop_length;

    }

    public boolean validateStackSequences2(int[] pushed, int[] popped) {
        int pop_index = 0;
        Stack<Integer> stack = new Stack<>();

        for (int push_e : pushed) {
            stack.push(push_e);
            while (!stack.isEmpty() && stack.peek() == popped[pop_index]) {
                stack.pop();
                pop_index++;
            }
        }
        return stack.isEmpty();
    }


    public static void main(String[] args) {

        int[] pushed = new int[]{1,2,3,4,5};
        int[] poped = new int[]{4,3,5,1,2};

        LC_Offer_31 lc = new LC_Offer_31();
        System.out.println(lc.validateStackSequences2(pushed,poped));

    }
}
