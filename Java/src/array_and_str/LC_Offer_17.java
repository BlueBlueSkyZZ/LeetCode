package array_and_str;

public class LC_Offer_17 {

    public int[] printNumbers(int n) {
        int max_num = (int)Math.pow(10, n) - 1;
        int[] result = new int[max_num];
        for (int i = 1; i <= max_num; i++) {
            result[i-1] = i;
        }
        return result;
    }

    //TODO add string solution
    int[] result;

    public int[] printNumbers2(int n) {
            return new int[]{};
    }
}
