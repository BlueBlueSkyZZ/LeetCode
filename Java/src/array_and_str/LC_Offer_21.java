package array_and_str;
import java.util.Arrays;
import java.util.Collections;

public class LC_Offer_21 {

    public int[] exchange(int[] nums) {
        if (nums.length == 0) {
            return nums;
        }
        int odd = 0, even = nums.length - 1;
        while (odd < even) {
            while (odd < even && nums[odd] % 2 == 1) {
                odd++;
            }
            while (odd < even && nums[even] % 2 == 0) {
                even--;
            }
            swap(nums, odd, even);
        }
        return nums;
    }

    private void swap(int[] nums, int x, int y) {
        int temp = nums[x];
        nums[x] = nums[y];
        nums[y] = temp;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{2,16,3,5,13,1,16,1,12,18,11,8,11,11,5,1};
        LC_Offer_21 sl = new LC_Offer_21();
        sl.exchange(nums);
        System.out.println(Arrays.toString(nums));
    }

}
