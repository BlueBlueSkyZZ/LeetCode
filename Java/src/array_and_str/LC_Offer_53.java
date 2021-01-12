package array_and_str;

public class LC_Offer_53 {

    public int search(int[] nums, int target) {
        int start = 0, end = nums.length - 1, mid = (start + end) / 2;
        int count = 0;
        while (start <= end) {
            if (nums[mid] == target) {
                //left and right search
                start = mid - 1;
                end = mid + 1;
                count++;
                while (start >= 0 && nums[start] == target) {
                    start--;
                    count++;
                }
                while (end < nums.length && nums[end] == target) {
                    end++;
                    count++;
                }
                break;
            } else if (nums[mid] < target) {
                start = mid + 1;
                mid = (start + end) / 2;
            } else {
                end = mid - 1;
                mid = (start + end) / 2;
            }
        }
        return count;
    }

    public int search2(int[] nums, int target) {
        return getRightMargin(nums, target) - getRightMargin(nums, target-1);
    }

    private int getRightMargin(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        int mid = (left + right) / 2;

        while (left <= right) {
            if (nums[mid] <= target) {
                left = mid + 1;
                mid = (left + right) / 2;
            } else {
                right = mid - 1;
                mid = (left + right) / 2;
            }
        }

        return left;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{5,7,7,8,8,10};
        int target = 9;
        LC_Offer_53 lc = new LC_Offer_53();
        System.out.println(lc.search2(nums, target));
    }

}
