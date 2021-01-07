package bit;

import hash.LC_Offer_50;

import java.util.Arrays;

public class LC_Offer_56 {

    public int[] singleNumbers(int[] nums) {
        int xor_result = 0;
        for (int num : nums) {
            xor_result ^= num;
        }

        int first_one = 1;
        while ((first_one & xor_result) == 0) {
            first_one <<= 1;
        }

        int num1=0, num2=0;

        for (int num : nums ) {
            if ((first_one & num) == 0) {
                num1 ^= num;
            } else {
                num2 ^= num;
            }
        }
        return new int[]{num1, num2};
    }


    public static void main(String[] args) {
        int[] nums = new int[]{1, 2, 5, 2};
        LC_Offer_56 lc = new LC_Offer_56();
        System.out.println(Arrays.toString(lc.singleNumbers(nums)));
    }
}
