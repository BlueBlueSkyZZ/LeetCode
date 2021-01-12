package dp;

public class LC_Offer_46 {

    public int translateNum(int num) {

        String num_str = Integer.toString(num);
        int[] num_array = new int[num_str.length()];

        for (int i = 0; i < num_array.length; i++) {
            num_array[i] = num_str.charAt(i) - '0';
        }

        if (num_str.length() < 2)
            return 1;


        int[] dp = new int[num_str.length()];
        dp[0] = 1;
        String sub_str;
        int sub_num;
        sub_str = num_str.substring(0, 2);
        sub_num = Integer.parseInt(sub_str);
        if (sub_num <= 25) {
            dp[1] = 2;
        } else {
            dp[1] = 1;
        }

        for (int i = 2; i < num_array.length; i++) {
            sub_str = num_str.substring(i-1, i+1);
            sub_num = Integer.parseInt(sub_str);
            if (10 <= sub_num && sub_num <= 25) {
                dp[i] = dp[i-1] + dp[i-2];
            } else {
                dp[i] = dp[i-1];
            }
        }

        return dp[num_str.length()-1];

    }

    public int translateNum2(int num) {

        String num_str = Integer.toString(num);

        int dp_0 = 1, dp_1 = 1;
        int dp_i = dp_1;
        for (int i = 2; i <= num_str.length(); i++) {
            String sub = num_str.substring(i-2, i);
            if (sub.compareTo("10") >= 0 && sub.compareTo("25") <= 0) {
                dp_i = dp_0 + dp_1;
            } else {
                dp_i = dp_1;
            }
            dp_0 = dp_1;
            dp_1 = dp_i;
        }
        return dp_i;

    }


    public static void main(String[] args) {
        int num = 12257;
        LC_Offer_46 lc = new LC_Offer_46();
        System.out.println(lc.translateNum2(num));
    }

}
