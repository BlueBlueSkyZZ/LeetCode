package stack_and_queue;

import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

public class LC_Offer_59II {
    Queue<Integer> queue;
    Deque<Integer> deque;

    public LC_Offer_59II() {
        queue = new LinkedList<>();
        deque = new LinkedList<>();
    }

    public int max_value() {
        if (deque.isEmpty())
            return -1;

        return deque.peekFirst();
    }

    public void push_back(int value) {
        queue.add(value);
        while (!deque.isEmpty() && deque.peekLast() < value) {
            deque.removeLast();
        }
        deque.add(value);
    }

    public int pop_front() {
        if (queue.isEmpty())
            return -1;

        int pop_result = queue.remove();
        if (deque.peekFirst().equals(pop_result)) {
            deque.removeFirst();
        }
        return pop_result;
    }

}
