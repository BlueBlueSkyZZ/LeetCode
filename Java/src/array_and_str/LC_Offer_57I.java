package array_and_str;

import java.util.Arrays;

public class LC_Offer_57I {

    public int[] twoSum(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            if (nums[left] + nums[right] == target) {
                break;
            } else if (nums[left] + nums[right] < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[]{nums[left], nums[right]};
    }

    public static void main(String[] args) {

        int[] nums = new int[]{10,26,30,31,47,60};
        int target = 40;

        LC_Offer_57I lc = new LC_Offer_57I();
        int[] result = lc.twoSum(nums, target);
        System.out.println(Arrays.toString(result));
    }

}
