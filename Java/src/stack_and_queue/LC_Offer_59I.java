package stack_and_queue;

import java.util.*;

public class LC_Offer_59I {

    public int[] maxSlidingWindow(int[] nums, int k) {

        if (nums.length == 0 || k == 0) {
            return new int[]{};
        }

        Deque<Integer> queue = new LinkedList<>();
        int[] result = new int[nums.length-k+1];
        for (int left = 1-k, right=0; right < nums.length; left++, right++) {

            if (left > 0 && queue.peekFirst() == nums[left-1]) {
                queue.removeFirst();
            }

            while (!queue.isEmpty() && queue.peekLast() < nums[right]) {
                queue.removeLast();
            }
            queue.add(nums[right]);
            if (left >= 0) {
                result[left] = queue.peek();
            }
        }
        return result;
    }

    public static void main(String[] args) {

        int[] nums = new int[]{1,3,-1,-3,5,3,6,7};
        int k = 3;
        LC_Offer_59I lc = new LC_Offer_59I();
        System.out.println(Arrays.toString(lc.maxSlidingWindow(nums, k)));
    }

}
