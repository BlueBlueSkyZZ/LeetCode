package array_and_str;

public class LC_Offer_11 {
    public int minArray(int[] numbers) {
        int left = 0, right = numbers.length - 1, mid = (left + right) / 2;

        while (left <= right) {
            mid = (left + right) / 2;
            if (numbers[mid] > numbers[right]) {
                left = mid + 1;
            } else if (numbers[mid] < numbers[right]){
                right = mid;
            } else {
                right--;
            }
        }

        return numbers[mid];

    }

    public static void main(String[] args) {
        int[] numbers = new int[]{2,2,2,0,1,1};
        LC_Offer_11 lc = new LC_Offer_11();
        System.out.println(lc.minArray(numbers));
    }
}
