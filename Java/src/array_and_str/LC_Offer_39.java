package array_and_str;

public class LC_Offer_39 {

    public int majorityElement(int[] nums) {
        int candidate = nums[0];
        int count = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == candidate) {
                count++;
            } else if (count == 0) {
                candidate = nums[i];
                count = 1;
            } else {
                count--;
            }
        }
        return candidate;
    }

    //TODO 分治算法完成一次

    public static void main(String[] args) {
        int[] nums = new int[]{1, 2, 3, 2, 2, 2, 5, 4, 2};
        LC_Offer_39 lc = new LC_Offer_39();
        System.out.println(lc.majorityElement(nums));
    }

}
