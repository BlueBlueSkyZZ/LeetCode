package hash;

public class LC_Offer_03 {

    public int findRepeatNumber(int[] nums) {
        int pointer = 0;
        int temp=0;

        while (pointer < nums.length) {

            if (nums[pointer] != pointer) {
                temp = nums[nums[pointer]];

                if (nums[temp] == temp) {
                    break;
                }

                nums[nums[pointer]] = nums[pointer];
                nums[pointer] = temp;
            } else {
                pointer++;
            }

        }

        return temp;
    }

}
